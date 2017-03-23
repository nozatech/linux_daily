from boto.ec2.cloudwatch import connect_to_region

import MySQLdb

import boto.ec2.cloudwatch

db = MySQLdb.connect("ravit.rdshostname.ap-northeast-1.rds.amazonaws.com", "username", "password", "databasename")

cursor = db.cursor()

n = cursor.execute("select * from GetActiveSessions")

n1 = cursor.fetchone()

s = str(n1)

table = string.maketrans('', '', )

number = s.translate(table, "(){}<>,L")

numbers = int(number)

reg = 'ap-northeast-1'

conn_cw = boto.ec2.cloudwatch.connect_to_region(reg,
                                                aws_access_key_id=’your_access_key’, aws_secret_access_key =’your_secret_key’)

conn_cw.put_metric_data(namespace='my_namespace', name='my_metric', value=numbers,
                        dimensions={'InstanceId': 'i-a1b2c3d4'})