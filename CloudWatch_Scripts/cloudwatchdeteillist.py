import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch client
cloudwatch_client = session.client('cloudwatch')

# List CloudWatch alarms
alarms = cloudwatch_client.describe_alarms()

# Create a list to store alarm information
alarm_info = []

for alarm in alarms['MetricAlarms']:
    alarm_name = alarm['AlarmName']
    creation_date = alarm['AlarmConfigurationUpdatedTimestamp']

    # Get alarm tags
    tags = cloudwatch_client.list_tags_for_resource(ResourceARN=alarm['AlarmArn'])['Tags']

    alarm_info.append([alarm_name, creation_date, tags])

# Define table headers
headers = ["Alarm Name", "Creation Date", "Tags"]

# Print the table of alarms
print("\nList of CloudWatch Alarms with Tags and Creation Dates:")
print(tabulate(alarm_info, headers, tablefmt="grid"))
