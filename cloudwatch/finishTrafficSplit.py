#!/usr/bin/env python
# Finish ELB traffic split

import os, sys, boto, time, urllib
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import InstanceState

import common
    
if len(sys.argv) != 5:
    print len(sys.argv), "USAGE: finishTrafficSplit.py ELB_BASE_NAME ELB_INSTANCE_NAME PROTOCOL(http|https) ELB_TO_BE_ACTIVE(A|B)"
    sys.exit(1)
    
ec2_conn = common.init_elb()
    
elb_base_name = sys.argv[1]
protocol = sys.argv[3]

if protocol != "http" and protocol != "https":
    print "FAIL unsupported protocol", protocol, "(must be http or https)"
    sys.exit(1)

elb_a_domain_name = elb_base_name + "-a.namcowireless.com"
elb_b_domain_name = elb_base_name + "-b.namcowireless.com"

elb_instance_base_name = sys.argv[2]
elb_a_instance_name = elb_instance_base_name + "-elb-01"
elb_b_instance_name = elb_instance_base_name + "-elb-02"

active_index = sys.argv[4].lower()
if active_index != 'a' and active_index != 'b':
    print "FAIL active_index must be a or b"
    sys.exit(1)

status_a = urllib.urlopen(protocol + "://" + elb_a_domain_name + "/tcg/api/1/status").read()
status_b = urllib.urlopen(protocol + "://" + elb_b_domain_name + "/tcg/api/1/status").read()
target_status = None

#print "Status A:", status_a
#print "Status B:", status_b

active_elb = active_elb_name = None
inactive_elb = None

if active_index == 'a':
    active_elb_name = elb_a_instance_name
    active_status = status_a
    print "Active load balancer will be", elb_a_domain_name
    
else:
    active_elb_name = elb_b_instance_name
    active_status = status_b
    print "Active load balancer will be", elb_b_domain_name

if active_status != "ok":
    print "FAIL target active load balancer", active_index, "must be healthy, but currently a =", status_a, " and b =", status_b
    sys.exit(1)

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

inactive_instances = ec2_conn.describe_instance_health(inactive_elb.name)
if len(inactive_instances) < 1:
    print "FAIL insufficient instances in to-be inactive load balancer:", len(inactive_instances)
    sys.exit(1)
    
for instance in inactive_instances:
    if instance.state == "InService":
        common.register_instance(instance, active_elb)

active_instances = ec2_conn.describe_instance_health(active_elb.name)
for instance in active_instances:
    if instance.state == "InService":
        common.register_instance(instance, inactive_elb)
          
print "Done!"