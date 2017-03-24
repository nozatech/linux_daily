#!/usr/bin/env python
# Find active instances

import os, sys, boto, time, urllib
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import InstanceState

import common
    
if len(sys.argv) < 2:
    print len(sys.argv), "USAGE: findActiveInstances.py INSTANCE_ID [INSTANCE_ID...]"
    sys.exit(1)
    
ec2_conn = common.init_ec2()

instance_ids = sys.argv[1:]
instances = ec2_conn.get_only_instances(instance_ids)

for instance in instances:
    print instance.tags['Name']
	
	
	



