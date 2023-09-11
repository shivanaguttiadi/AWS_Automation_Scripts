import boto3
from tabulate import tabulate
from datetime import datetime, timedelta, timezone

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Calculate the date 30 days ago from the current date in UTC timezone
thirty_days_ago = datetime.now(timezone.utc) - timedelta(days=30)

# List all EC2 instances
response = ec2.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-name',
            'Values': ['stopped'],  # Filter for instances in a stopped state
        }
    ]
)

# Create a list to store the instance information
instance_info = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        launch_time = instance['LaunchTime'].replace(tzinfo=timezone.utc)  # Make launch_time offset-aware
        instance_state = instance['State']['Name']

        # Retrieve instance name from tags (if available)
        instance_name = 'N/A'
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break

        # Get the last time the instance was started
        instance_start_time = None
        for state_transition in instance.get('StateTransitionReason', '').split(';'):
            if 'Client.User' in state_transition and 'running' in state_transition:
                start_time_str = state_transition.split(' ')[0].strip()
                instance_start_time = datetime.strptime(start_time_str, '%Y-%m-%dT%H:%M:%S%z')

        # Check if the instance was launched in the last 30 days
        if launch_time >= thirty_days_ago:
            instance_info.append([
                instance_name,
                instance_id,
                launch_time.strftime('%Y-%m-%d %H:%M:%S %Z'),  # Format launch_time
                instance_start_time.strftime('%Y-%m-%d %H:%M:%S %Z') if instance_start_time else 'N/A',  # Last start time
            ])

# Create a table and print it
table_headers = ["Instance Name", "Instance ID", "Launch Time", "Last Start Time"]
table = tabulate(instance_info, headers=table_headers, tablefmt="grid")
print("List of EC2 Instances Launched in the Last 30 Days and Currently Stopped:")
print(table)
