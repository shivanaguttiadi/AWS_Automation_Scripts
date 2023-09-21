import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch client
cloudwatch_client = session.client('cloudwatch')

# List all AWS Billing Alarms
alarms = cloudwatch_client.describe_alarms(AlarmNamePrefix='AWS/Billing')

# Create a list to store alarm information
alarm_info = []

for alarm in alarms['MetricAlarms']:
    alarm_name = alarm['AlarmName']
    alarm_state = alarm['StateValue']
    alarm_created_time = alarm['StateUpdatedTimestamp'].strftime('%Y-%m-%d %H:%M:%S')

    alarm_info.append([alarm_name, alarm_state, alarm_created_time])

# Define table headers
headers = ["Alarm Name", "State", "Created Time (UTC)"]

# Print the table of AWS Billing Alarms
print("\nList of AWS Billing Alarms:")
print(tabulate(alarm_info, headers, tablefmt="grid"))
