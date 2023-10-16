import boto3
import random
import datetime
AWS_REGION = "us-east-1"
client = boto3.client('logs', region_name=AWS_REGION)
response = client.get_log_events(
    logGroupName='/aws/lambda/Ec2Autoturnoff-TestLambdaFunction-fnUvc94DygKN',
    logStreamName='[$LATEST]a66503cbeb13499099db81e6adc9fe82',
    startTime=int(datetime.datetime(2023, 10, 8, 0, 0).strftime('%s'))*1000,
    endTime=int(datetime.datetime(2023, 10, 8, 0, 0).strftime('%s'))*1000,
    limit=123,
    startFromHead=True
)
log_events = response['events']
for each_event in log_events:
    print(each_event)