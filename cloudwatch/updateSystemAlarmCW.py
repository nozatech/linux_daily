#!/usr/bin/env python
# Creating EC2 system Alarm metric warning for CloudWatch
# Install AWS CLI and configure 
# Install Boto

# for SNS message VAR
MONOCLE_URGENT_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
MONOCLE_WARNING_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'
# arn : amazon resource name
# aws : aws
# sns : aws simple notification service
# us-west-2 : region
# 688595016292 : aws-mobiletools account id
# MONOCLE_Warning : resource

#------------------------------------------------------------------------------------------------
import os, sys, boto
# /python3x/Lib/site-packages/boto
# 'sys' module provides Python interpreter's constants, functions and methods

from boto.ec2.cloudwatch 		import CloudWatchConnection
from boto.ec2.cloudwatch.alarm 	import MetricAlarm
# from /python2x/Lib/site-packages/boto/ec2/cloudwatch/alarm.py  import 'MetricAlarm' function

import common				
# include common.py file for create, delete, and AWS connection


# Creating EC2 instance list txt file using AWS cli tool run from BASH 
#------------------------------------------------------------------------------------------------
import subprocess
getInstance = "aws ec2 describe-instances \
                --query 'Reservations[*].Instances[*].[InstanceId]' \
                --filters Name=instance-state-name,Values=running \
                --output text > \
                `pwd`/awsInstance.txt"
output = subprocess.check_output(['bash','-c', getInstance])

#------------------------------------------------------------------------------------------------
# Prints out AWS Instance IDs
print "Here are the list of EC2..."
print "---------------------------"

for i in open('awsInstance.txt', 'r').readlines():
    print i
#------------------------------------------------------------------------------------------------
	
# Usage
if len(sys.argv) != 4:
    print "USAGE: updateSystemAlarmCW.py          	ALARM_PREFIX   INSTANCE_ID    SEVERITY(urgent|warn)"
    print "\t"	"e.g. python   updateCloudWatch.py 	CPUUtilization i-0bd698cc040d9a2d9   		warn"
    sys.exit(1)			#return error code 1

#------------------------------------------------------------------------------------------------
# variables set from cmd line input arguments
alarm_prefix   = sys.argv[1]			# CPU 	 <- 1st argument as alarm_prefix
target_instance_id = sys.argv[2]			# i-xxxx <- 2nd argument as target_lb_name
severity       = sys.argv[3].lower()	# warn   <- 3rd and lower letter method for "==" comparison 
sns_topic      = None                  	# 'None' <- Reset original value

#------------------------------------------------------------------------------------------------
# sns_topic VAR and message set
if severity == 'urgent':
    sns_topic = MONOCLE_URGENT_TOPIC    #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
elif severity == 'warn':
    sns_topic = MONOCLE_WARNING_TOPIC   #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'
else:
    print "FATAL! invalid entry value(urgent|wan)", severity   # 'urgent|warn' only
    sys.exit(2)		
	# System exit 2 as error code
	# python updateCloudWatch.py http elb-01 test
	# echo $?  outputs  2   <- error code

#------------------------------------------------------------------------------------------------	
# Assigning a new alarm metric using Dictionary{key:value}
alarm_dimensions = {
    'InstanceName': target_instace_id
}

# Alarm templates LIST [{key:value}]
# CPU over 60 alarm and notification
alarm_templates = [
    { 
		'name': alarm_prefix + " - CPU Utilization spike over 40%",
		'description' : "CPU usage triggers above 40% for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "CPUUtilization",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 4.0,
		'period': 300,
		'evaluation_periods': 5,
		'alarm_actions': [sns_topic],
		'unit': "Percent",
		'dimensions': alarm_dimensions
	},
    { 
		'name': alarm_prefix + " - Disk Reads over 40%",
		'description' : "Disk Read triggers above 40% for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskReadBytes",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 4.0,
		'period': 300,
		'evaluation_periods': 5,
		'alarm_actions': [sns_topic],
		'unit': "Percent",
		'dimensions': alarm_dimensions
	},
	    { 
		'name': alarm_prefix + " - Disk Writes over 40%",
		'description' : "Disk Write triggers above 40% for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskWriteBytes",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 4.0,
		'period': 300,
		'evaluation_periods': 2,
		'alarm_actions': [sns_topic],
		'unit': "Percent",
		'dimensions': alarm_dimensions
	},
	    { 
		'name': alarm_prefix + " - CPU Utilization spike over 40%",
		'description' : "CPU usage triggers above 40% for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "CPUUtilization",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 4.0,
		'period': 300,
		'evaluation_periods': 2,
		'alarm_actions': [sns_topic],
		'unit': "Percent",
		'dimensions': alarm_dimensions
	}
]

#------------------------------------------------------------------------------------------------
# *** Real Program Starts here ***
#------------------------------------------------------------------------------------------------
# Check existing alarms 
def get_alarms(alarm_prefix):			# 'http' from command line input argument value
    existing_alarms = cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix)
																	# None to 'http'
    # /Python34/Lib/site-packages/boto/ec2/cloudwatch/__init__
	# def describe_alarms(self, action_prefix=None, alarm_name_prefix=None,
    #	                  alarm_names=None, max_records=None, state_value=None,
    #                     next_token=None):

	# if exiting_alarms > 0:   			<= missing?
	
	# Number of existing alarms found 
    print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix
    ''' 
	Found 4 existing alarms with prefix http_spike
    '''
	# List of alarms and prints out
    for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
        print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions
        '''
		http_spike - HTTP 4xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
		...  #'alarm_actions': [sns_topic]
        '''
    return existing_alarms
#------------------------------------------------------------------------------------------------
# connect to AWS 	
cloudwatch = common.init_cloudwatch()
	# invoke from common.py's 'init_cloudwatch()' function
	# def init_cloudwatch():
	#	access_key, secret_key = get_keys_from_env()
	#	return boto.ec2.cloudwatch.connect_to_region("us-west-2", aws_access_key_id=access_key, aws_secret_access_key=secret_key)
#------------------------------------------------------------------------------------------------
# Invoking def get_alarms() using Global var alarm_prefix	
existing_alarms = get_alarms(alarm_prefix)
print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix
'''
Found 4 existing alarms with prefix http_spike
'''
#------------------------------------------------------------------------------------------------
for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
    print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions
    '''
	http_spike - HTTP 4xx Spike : {u'LoadBalancerName': [u'elb1']} [u'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning']
    '''
#------------------------------------------------------------------------------------------------
# Declare to deleting existing alarms
print "Deleting existing alarms..."

# If there are more than 0, delete them all
if len(existing_alarms) > 0:
    cloudwatch.delete_alarms(existing_alarms)

    print "Existing alarms have been removed!"
#------------------------------------------------------------------------------------------------
	
# Declare to creating new alarms    
print "Now creating new alarms..."

# Creating new alarms from 4 templates
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
#------------------------------------------------------------------------------------------------

print "Checking alarm state after creation..."

# Check existing alarms same as 1st time checking existing alarm
get_alarms(alarm_prefix)

#################################################################################################################
"""
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
