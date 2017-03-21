#!/usr/bin/env python
# Find instances in Load Balancer

import os, sys, boto, time, urllib
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import InstanceState

import common
    
if len(sys.argv) != 2:
    print len(sys.argv), "USAGE: findInstancesInLB.py    ELB_NAME"
	sys.exit(1)
    
elb_conn = common.init_elb()
ec2_conn = common.init_ec2()
    
elb_name = sys.argv[1]

all_instances = elb_conn.describe_instance_health(elb_name)
active_instances = []
for instance in all_instances:
    if instance.state == "InService":
        active_instances.append(instance.instance_id)

if len(active_instances) < 1:
    print "FAIL no in-service instances in the target load balancer", elb_name
    sys.exit(1)

print ' '.join(active_instances) 