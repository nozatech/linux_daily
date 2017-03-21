#!/usr/bin/env python
# Preparing traffic split

import os, sys, boto, time, urllib
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import InstanceState

import common
    
if len(sys.argv) not in [5, 6]:
    print len(sys.argv), "USAGE: prepTrafficSplit.py ENV ELB_BASE_NAME ELB_INSTANCE_NAME PROTOCOL(http|https) [output_file]"
    sys.exit(1)
    
ec2_conn = common.init_elb()
    
env = sys.argv[1]
elb_base_name = sys.argv[2]
protocol = sys.argv[4]

if protocol != "http" and protocol != "https":
    print "FAIL unsupported protocol", protocol, "(must be http or https)"
    sys.exit(1)

elb_a_domain_name = elb_base_name + "-a.namcowireless.com"
elb_b_domain_name = elb_base_name + "-b.namcowireless.com"

elb_instance_base_name = sys.argv[3]
elb_a_instance_name = elb_instance_base_name + "-elb-01"
elb_b_instance_name = elb_instance_base_name + "-elb-02"

print "Prepping traffic split for ELBs at", elb_a_domain_name, "and", elb_b_domain_name

active_lb = urllib.urlopen("https://outcast-routing.s3.amazonaws.com/" + env.lower() + ".txt").read().lower()

status_a = urllib.urlopen(protocol + "://" + elb_a_domain_name + "/tcg/api/1/status").read()
status_b = urllib.urlopen(protocol + "://" + elb_b_domain_name + "/tcg/api/1/status").read()

active_elb = active_elb_name = active_elb_index = None
inactive_elb = inactive_elb_name = inactive_elb_index = None

if status_a != "ok" or status_b != "ok":
    print "FAIL both load balancers should be healthy (a =", status_a, "b =", status_b, ")"
    sys.exit(1)
    
if active_lb == 'a':
    active_elb_name = elb_a_instance_name
    inactive_elb_name = elb_b_instance_name
    active_elb_index = "A"
    inactive_elb_index = "B"
    print "Active load balancer is", elb_a_domain_name
    
elif active_lb == 'b':
    active_elb_name = elb_b_instance_name
    inactive_elb_name = elb_a_instance_name
    active_elb_index = "B"
    inactive_elb_index = "A"
    print "Active load balancer is", elb_b_domain_name
else:
    print "FAIL unexpected LB from routing file:", active_lb
    sys.exit(2)
    
all_lbs = ec2_conn.get_all_load_balancers([elb_a_instance_name, elb_b_instance_name])
if len(all_lbs) != 2:
    print "FAIL: got unexpected number of ELBs back:", len(all_lbs)
    sys.exit(1)
    
for lb in all_lbs:
    if lb.name == active_elb_name:
        print "Active ELB:", lb.name
        active_elb = lb
    else:
        print "Inactive ELB:", lb.name
        inactive_elb = lb

if active_elb == None:
    print "FAIL: didn't find active ELB"
    sys.exit(1)
elif inactive_elb == None:
    print "FAIL: didn't find inactive ELB"
    sys.exit(1)

def get_active_instances(elb_name):
    all_instances = ec2_conn.describe_instance_health(elb_name)
    active_instances = []
    for instance in all_instances:
        if instance.state == "InService":
            active_instances.append(instance)
            
    return active_instances
    
source_active_instances = get_active_instances(active_elb.name)
target_active_instances = get_active_instances(inactive_elb.name)

get_instance_ids = lambda i: i.instance_id

if set(map(get_instance_ids, source_active_instances)) != set(map(get_instance_ids, target_active_instances)):
    print "FAIL: the two LBs have a different set of instances before the traffic split has begun."
    sys.exit(3)

if len(source_active_instances) < 2:
    print "FAIL only found", len(active_instances), " in-service instances in the to-be deactivated load balancer", active_elb.name
    sys.exit(1)

moved_instance_ids = []
to_move_indexes = range(0,len(source_active_instances)/2)

for i in range(0, len(source_active_instances)):
    if i in to_move_indexes:
        common.deregister_instance(source_active_instances[i], active_elb)
        moved_instance_ids.append(source_active_instances[i].instance_id)
    else:
        common.deregister_instance(source_active_instances[i], inactive_elb)

output_filename = None
if len(sys.argv) == 6:
    output_filename = sys.argv[5]
else:
    output_filename = "prepTrafficSplit.report.properties"
    
output_file = open(output_filename, 'w')
output_file.write("active_lb_index=" + active_elb_index + "\n")
output_file.write("active_lb_name=" + active_elb_name + "\n")
output_file.write("inactive_lb_index=" + inactive_elb_index + "\n")
output_file.write("inactive_lb_name=" + inactive_elb_name + "\n")
output_file.write("moved_instance_ids=" + ' '.join(moved_instance_ids) + "\n")
output_file.close()

print "Done; wrote report to", output_filename