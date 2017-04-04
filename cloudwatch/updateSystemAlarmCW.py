#!/usr/bin/env python
# Creating EC2 system Alarm metric warning for CloudWatch
# Install AWS CLI and configure 
# Install Boto

# for SNS message VAR
MONOCLE_URGENT_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
MONOCLE_WARNING_TOPIC='arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'


# Import modules and libraries
import os, sys, boto

from boto.ec2.cloudwatch 		import CloudWatchConnection
from boto.ec2.cloudwatch.alarm 	import MetricAlarm

# include common.py file for create, delete, and AWS connection
import common				



# Creating EC2 instance list txt file using AWS CLI tool run from BASH
import subprocess
getInstance = "aws ec2 describe-instances \
                --query 'Reservations[*].Instances[*].[InstanceId]' \
                --filters Name=instance-state-name,Values=running \
                --output text > \
                `pwd`/awsInstance.txt"
output = subprocess.check_output(['bash','-c', getInstance])


# Prints out AWS Instance IDs
print "Here are the list of EC2..."
print "---------------------------"

for i in open('awsInstance.txt', 'r').readlines():
    print i

	
# Usage
if len(sys.argv) != 4:
    print "USAGE: updateSystemAlarmCW.py        ALARM_PREFIX   			INSTANCE_ID    SEVERITY(urgent|warn)"
    print "e.g. python updateCloudWatch.py 	Dev:i-0bd698cc040d9a2d9    i-0bd698cc040d9a2d9   warn"
    print "e.g. python updateCloudWatch.py 	Sttag:i-0bd698cc040d9a2d9  i-0bd698cc040d9a2d9   warn"
    print "e.g. python updateCloudWatch.py 	Live:i-0bd698cc040d9a2d9   i-0bd698cc040d9a2d9   urgent"
    sys.exit(1)


# variables set from cmd line input arguments
alarm_prefix = sys.argv[1]			#  1st argument as alarm_prefix
target_instance_id = sys.argv[2]	#  2nd argument as target_lb_name
severity = sys.argv[3].lower()		#  3rd argument and lower() for "==" comparison
sns_topic = None                  	#  Reset original value


# sns_topic VAR and message set
if severity == 'urgent':
    sns_topic = MONOCLE_URGENT_TOPIC    #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Urgent'
elif severity == 'warn':
    sns_topic = MONOCLE_WARNING_TOPIC   #'arn:aws:sns:us-west-2:688595016292:MONOCLE_Warning'
else:
    print "FATAL! invalid entry value(urgent|warn)", severity   # 'urgent|warn' only
    sys.exit(2)


# Assigning a new alarm metric
alarm_dimensions = {
    'InstanceName': target_instance_id
}

# Alarm templates
alarm_templates = [
    { 
		'name': alarm_prefix + " - CPU Utilization spikes over 40%",
		'description' : "CPU usage spikes above 40% for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "CPUUtilization",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 40,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Percent",
		'dimensions': alarm_dimensions
	},
    { 
		'name': alarm_prefix + " - Disk Reads Bytes spike over 15MB",
		'description' : "Disk Reads Byte spikess above 15MB for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskReadBytes",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 15000000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Bytes",
		'dimensions': alarm_dimensions
	},
	    { 
		'name': alarm_prefix + " - Disk Reads Ops spikes over 2000 IOPS",
		'description' : "Disk Reads Ops spikes above 2000 for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskReadOps",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 2000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Count",
		'dimensions': alarm_dimensions
	},
	    { 
		'name': alarm_prefix + " - Disk Writes Bytes spikes over 15Mb",
		'description' : "Disk Writes Byptes spikes above 15MB for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskWriteBytes",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 15000000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Bytes",
		'dimensions': alarm_dimensions
	},
	    { 
		'name': alarm_prefix + " - Disk Writes Ops spikes over 2000 IOPS",
		'description' : "Disk Writes Ops spikes above 2000 IOPS for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "DiskWriteOps",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 2000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Count",
		'dimensions': alarm_dimensions
	},
		{ 
		'name': alarm_prefix + " - Network In spikes over 15MB",
		'description' : "Network In triggers above 15MB/sec for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "NetworkIn",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 15000000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Bytes",
		'dimensions': alarm_dimensions
	},
		{ 
		'name': alarm_prefix + " - Network Out spikes over 15MB",
		'description' : "Network Out spikes above 15MB/sec for 5 mins",
		'namespace': "AWS/EC2",
		'metric': "NetworkOut",
		'statistic':"Average",
		'comparison': ">=",
		'threshold': 15000000,
		'period': 300,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Bytes",
		'dimensions': alarm_dimensions
	},
	    {
		'name': alarm_prefix + " - System Check Failed",
		'description': "System Check Failed",
		'namespace': "AWS/EC2",
		'metric': "SystemCheckFailed",
		'statistic': "Average",
		'comparison': ">=",
		'threshold': 0,					# 0 passed, 1 failed
		'period': 60,
		'evaluation_periods': 1,
		'alarm_actions': [sns_topic],
		'unit': "Count",
		'dimensions': alarm_dimensions
	}
]

#------------------------------------------------------------------------------------------------
# *** Real Program Starts here ***
#------------------------------------------------------------------------------------------------
# Check existing alarms 
def get_alarms(alarm_prefix):
    existing_alarms = cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix)

    # if exiting_alarms > 0:   			<= missing?
	
	# Number of existing alarms found 
    print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix

    # List of alarms and prints out
    for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
        print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions

    return existing_alarms

# connect to AWS 	
cloudwatch = common.init_cloudwatch()

# Invoking def get_alarms() using Global var alarm_prefix	
existing_alarms = get_alarms(alarm_prefix)
print "Found", len(existing_alarms), "existing alarms with prefix", alarm_prefix

for alarm in cloudwatch.describe_alarms(alarm_name_prefix=alarm_prefix):
    print "\t", alarm.name, ":", alarm.dimensions, alarm.alarm_actions


print "Deleting existing alarms..."

# If there are more than 0, delete them all
if len(existing_alarms) > 0:
    cloudwatch.delete_alarms(existing_alarms)

    print "Existing alarms have been removed!"
#------------------------------------------------------------------------------------------------
	
# Declare to creating new alarms    
print "Now creating new alarms..."

# Creating new alarms from 7 templates
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



