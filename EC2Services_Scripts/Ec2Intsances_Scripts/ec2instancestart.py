import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of EC2 instance IDs that you want to start
instance_ids_to_start = ['i-060eff6ce9f491c4f']  # Replace with your instance IDs

# Start the EC2 instances
response = ec2.start_instances(InstanceIds=instance_ids_to_start)

# Create a table with proper formatting for the output
table = PrettyTable()
table.field_names = ["Instance ID", "Current State"]

# Check the response to verify if the instances were successfully started
if response['StartingInstances']:
    for instance in response['StartingInstances']:
        instance_id = instance['InstanceId']
        current_state = instance['CurrentState']['Name']
        table.add_row([instance_id, current_state])
else:
    print("No instances were started.")

# Print the table
print(table)

# Calculate and print the total count of started instances
total_started_instances = len(instance_ids_to_start)
print(f"Total started instances: {total_started_instances}")
