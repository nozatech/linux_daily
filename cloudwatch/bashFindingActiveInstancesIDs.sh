#!/bin/bash 
# Finding Active Instances IDs
#http://stackoverflow.com/questions/23936216/how-can-i-get-list-of-only-running-instances-when-using-ec2-describe-tags
# From Bash using AWS CLI tool

aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId]' --filters Name=instance-state-name,Values=running --output text

# Get instance IDs
# i-0bd698cc040d9a2d9 i-09ce42dc501dcf755
