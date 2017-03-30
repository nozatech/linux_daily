import boto.ec2.cloudwatch
from boto.ec2.cloudwatch import MetricAlarm
 
aws_conn = boto.ec2.cloudwatch.connect_to_region( 
												<required_region>, 
												aws_access_key_id=<api_key>, 
												aws_secret_access_key=<api_secret> 
												)
 
sns_topic = 'arn:aws:sns:eu-west-1:<acct_num>:cloudwatch-alarms'
 
# CPU over 60 alarm and notification
metric_alarm = MetricAlarm(
 name="CPU above 60%",
 metric="CPUUtilization",
 namespace="AWS/EC2",
 statistic="Average",
 comparison=">=",
 threshold=60,
 period=300,
 evaluation_periods=2,
 unit="Percent",
 description="Alarm that triggers when the instance CPU goes above 60% for 10 minutes",
 dimensions={"AutoScalingGroupName": "awseb-e-tut3pqp-stack-AWSEBAutoScalingGroup-3N4N80YX"},
 alarm_actions=[sns_topic]
)
 
aws_conn.create_alarm(metric_alarm)