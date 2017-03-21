#!/usr/bin/env python
# Common 

import os, sys, boto, time, urllib
from boto.ec2.elb import ELBConnection
from boto.ec2.elb import InstanceState

from boto.s3.connection import S3Connection


def init_ec2():
    access_key, secret_key = get_keys_from_env()
    return boto.ec2.connect_to_region("us-west-2", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def init_elb():
    access_key, secret_key = get_keys_from_env()
    return boto.ec2.elb.connect_to_region("us-west-2", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def init_cloudwatch():
    access_key, secret_key = get_keys_from_env()
    return boto.ec2.cloudwatch.connect_to_region("us-west-2", aws_access_key_id=access_key, aws_secret_access_key=secret_key)

def init_s3():
    access_key, secret_key = get_keys_from_env()
    return S3Connection(access_key, secret_key)

def deregister_instance(instance, from_elb):
    print "De-registering instance", instance.instance_id, "from load balancer", from_elb.name
    from_elb.deregister_instances([instance.instance_id])
        
def register_instance(instance, to_elb):
    print "Registering instance", instance.instance_id, "into load balancer", to_elb.name
    to_elb.register_instances([instance.instance_id])

def move_instance(instance, from_elb, to_elb):
    deregister_instance(instance, from_elb)
    register_instance(instance, to_elb)

def get_keys_from_env():
#    access_key = "AKIAI24P4WR"
    access_key = os.environ.get("MONOCLE_AWS_ACCESS_KEY")
#    secret_key = "EDUnpsadm4z7a3T8feLF"
    secret_key = os.environ.get("MONOCLE_AWS_SECRET_KEY")
    
    if access_key == None or secret_key == None:
        print "FAILED! You must have MONOCLE_AWS_ACCESS_KEY and MONOCLE_AWS_SECRET_KEY in OS environment."
		print "\t"   "e.g. export access_key=x and export secret_key=x"
        sys.exit(1)
        
    return (access_key, secret_key)