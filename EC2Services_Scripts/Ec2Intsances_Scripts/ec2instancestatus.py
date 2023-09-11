import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# List all EC2 instances
response = ec2.describe_instances()

# Create dictionaries to count instances by state
instance_counts = {'running': 0, 'terminated': 0, 'stopped': 0}

# Create a list to store the instance information
instance_info = []

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_name = "N/A"  # Initialize with "N/A" by default
        instance_type = instance['InstanceType']
        instance_state = instance['State']['Name']
        
        # Retrieve instance name from tags (if available)
        for tag in instance.get('Tags', []):
            if tag['Key'] == 'Name':
                instance_name = tag['Value']
                break

        # Increment the count for the instance state
        if instance_state in instance_counts:
            instance_counts[instance_state] += 1

        instance_info.append([
            instance_id,
            instance_name,
            instance_type,
            instance_state,
        ])

# Calculate the total instance count
total_instance_count = sum(instance_counts.values())

# Create a table and print it for instance information
table_headers = ["Instance ID", "Instance Name", "Instance Type", "Instance State"]
table = tabulate(instance_info, headers=table_headers, tablefmt="grid")
print("List of EC2 Instances:")
print(table)

# Create a table for instance counts, including the total instance count
counts_table_headers = ["Instance State", "Count"]
counts_table_data = list(instance_counts.items())
counts_table_data.append(("Total", total_instance_count))
counts_table = tabulate(counts_table_data, headers=counts_table_headers, tablefmt="grid")
print("\nInstance Counts:")
print(counts_table)
