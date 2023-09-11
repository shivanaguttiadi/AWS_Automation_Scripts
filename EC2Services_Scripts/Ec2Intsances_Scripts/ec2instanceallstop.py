import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Describe all EC2 instances
response = ec2.describe_instances()

# Create a list to store the instance IDs
instance_ids_to_stop = []

# Extract instance IDs and check if they are in a running state
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_state = instance['State']['Name']
        
        if instance_state == 'running':
            instance_ids_to_stop.append(instance_id)

# Check if there are instances to stop
if instance_ids_to_stop:
    # Stop the instances
    ec2.stop_instances(InstanceIds=instance_ids_to_stop)

    # Print a message
    print(f"Stopping {len(instance_ids_to_stop)} instances:")
    for instance_id in instance_ids_to_stop:
        print(f"Instance ID: {instance_id}")
else:
    print("No running instances found to stop.")
