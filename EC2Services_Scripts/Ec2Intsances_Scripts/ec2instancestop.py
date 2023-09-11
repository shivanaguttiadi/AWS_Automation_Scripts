import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace 'your-instance-id-1' and 'your-instance-id-2' with the actual instance IDs you want to stop.
# You can provide multiple instance IDs in the list.
instance_ids_to_stop = ['i-01ccd888f0ac7f911','i-0071c78e659ff0bb1','i-0a2eb1289c559210e','	i-0c51211db8a6af7c3']

# Stop the EC2 instances
response = ec2.stop_instances(InstanceIds=instance_ids_to_stop)

# Print the response
print("Stopping instances:")
for instance_id in instance_ids_to_stop:
    print(f"Instance {instance_id}: Stopping requested")

# You can also wait for the instances to stop if needed
ec2.get_waiter('instance_stopped').wait(InstanceIds=instance_ids_to_stop)

# Print a message when the instances have stopped
print("All instances have been stopped.")
