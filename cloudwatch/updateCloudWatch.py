#!/usr/bin/env python
# Creating ELB metric warning for CloudWatch

MONOCLE_URGENT_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
MONOCLE_WARNING_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'

""" 
arn : amazon resource name
aws : aws
sns : aws simple notification service
us-west-2 : region
688595016292 : aws-mobiletools account id
MONOCLE_Warning : resource
"""

import os, sys, boto
# /python3x/Lib/site-packages/boto
# 'sys' module provides information about constants, functions and methods of the Python interpreter

from boto.ec2.cloudwatch 		import CloudWatchConn ection
from boto.ec2.cloudwatch.alarm 	import MetricAlarm
#from /python3x/Lib/site-packages/boto/ec2/cloudwatch/alarm.py  import 'MetricAlarm' function

import common				
# include common.py file for 

# Synopsis (how to run)
if len(sys.argv) != 4:
    print "USAGE: updateCloudWatch.py    ALARM_PREFIX    LB_NAME    SEVERITY(urgent|warn)"
	print "\t"	"e.g. python   updateCloudWatch.py 	http  elb-01    warn"
    sys.exit(1)			#return 1 as error code?

	
# variables set	
alarm_prefix   = sys.argv[1]
target_lb_name = sys.argv[2]
severity       = sys.argv[3].lower()	# lower letters
sns_topic      = None                  	# Reset original value

# 
if severity == 'urgent':
    sns_topic = MONOCLE_URGENT_TOPIC #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
elif severity == 'warn':
    sns_topic = MONOCLE_WARNING_TOPIC #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'
else:
    print "FATAL invalid severity", severity
    sys.exit(2)		#return 2 as error code?

	
# Assigning a new metric    
alarm_dimensions = {
    'LoadBalancerName': target_lb_name
}

alarm_templates = [
    { 
        'name': alarm_prefix + " - Latency Spike",
        'description': "Latency Spike",
        'namespace': 'AWS/ELB',
        'metric': "Latency",
        'statistic': "Average",
        'comparison': '>=',
        'threshold': 6.5,
        'period': 60,
        'evaluation_periods': 5,
        'alarm_actions': [sns_topic],
        'dimensions': alarm_dimensions
    },
    { 
        'name': alarm_prefix + " - HTTP 4xx Spike",
        'description': "HTTP 4xx Spike",
        'namespace': 'AWS/ELB',
        'metric': "HTTPCode_Backend_4XX",
        'statistic': "Sum",
        'comparison': '>=',
        'threshold': 100,
        'period': 300,
        'evaluation_periods': 3,
        'alarm_actions': [sns_topic],
        'dimensions': alarm_dimensions
    },
    { 
        'name': alarm_prefix + " - HTTP 5xx Spike",
        'description': "HTTP 5xx Spike",
        'namespace': 'AWS/ELB',
        'metric': "HTTPCode_Backend_5XX",
        'statistic': "Sum",
        'comparison': '>=',
        'threshold': 500,
        'period': 300,
        'evaluation_periods': 2,
        'alarm_actions': [sns_topic],
        'dimensions': alarm_dimensions
    },
    { 
        'name': alarm_prefix + " - Healthy Host Count",
        'description': "Healthy Host Count",
        'namespace': 'AWS/ELB',
        'metric': "HealthyHostCount",
        'statistic': "Minimum",
        'comparison': '<',
        'threshold': 1,
        'period': 60,
        'evaluation_periods': 1,
        'alarm_actions': [sns_topic],
        'dimensions': alarm_dimensions
    }
]

# 
def get_alarms(alarm_prefix):
    existing_alarms = cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix)
	
    # /Python34/Lib/site-packages/boto/ec2/cloudwatch/__init__
	# def describe_alarms(self, action_prefix=None, alarm_name_prefix=None,
    #	                  alarm_names=None, max_records=None, state_value=None,
    #                    next_token=None):
	#					 ............

	
    print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix
	
    for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
        print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions
        
    return existing_alarms

	
cloudwatch = common.init_cloudwatch()
	# invoke from common.py's 'init_cloudwatch()' function
	# def init_cloudwatch():
	#	access_key, secret_key = get_keys_from_env()
	#	return boto.ec2.cloudwatch.connect_to_region("us-west-2", aws_access_key_id=access_key, aws_secret_access_key=secret_key)


existing_alarms = get_alarms(alarm_prefix)

print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix


for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
    print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions

print "Clearing existing alarms..."

if len(existing_alarms) > 0:
    cloudwatch.delete_alarms(existing_alarms)
    
print "Creating new alarms..."

for template in alarm_templates:
    alarm = MetricAlarm(
        name=template['name'],
        description=template['description'],
        namespace=template['namespace'],
        metric=template['metric'],
        statistic=template['statistic'],
        comparison=template['comparison'],
        threshold=template['threshold'],
        period=template['period'],
        evaluation_periods=template['evaluation_periods'],
        alarm_actions=template['alarm_actions'],
        dimensions=template['dimensions']
    )
    
    print "\t", alarm
    cloudwatch.create_alarm(alarm)

print "Checking alarm state after creation..."

get_alarms(alarm_prefix)



#################################################################################################################
"""
Output of this script

Found 4 existing alarms with prefix http_spike
        http_spike - HTTP 4xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - HTTP 5xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Healthy Host Count : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Latency Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
		
Found 4 existing alarms with prefix http_spike
        http_spike - HTTP 4xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - HTTP 5xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Healthy Host Count : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Latency Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
		
Clearing existing alarms...

Creating new alarms...
        MetricAlarm:http_spike - Latency Spike[Latency(Average) GreaterThanOrEqualToThreshold 6.5]
        MetricAlarm:http_spike - HTTP 4xx Spike[HTTPCode_Backend_4XX(Sum) GreaterThanOrEqualToThreshold 100.0]
        MetricAlarm:http_spike - HTTP 5xx Spike[HTTPCode_Backend_5XX(Sum) GreaterThanOrEqualToThreshold 500.0]
        MetricAlarm:http_spike - Healthy Host Count[HealthyHostCount(Minimum) LessThanThreshold 1.0]
		
Checking alarm state after creation...

Found 4 existing alarms with prefix http_spike
        http_spike - HTTP 4xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - HTTP 5xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Healthy Host Count : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
        http_spike - Latency Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']

"""
