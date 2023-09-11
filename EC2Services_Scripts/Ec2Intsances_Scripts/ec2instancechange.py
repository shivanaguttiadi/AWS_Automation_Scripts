import boto3

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace 'your-instance-id' and 'new-instance-type' with the actual instance ID and the desired instance type
instance_id = 'i-0e314f16caac03c40'
new_instance_type = 't2.nano'  # Corrected instance type format

# Modify the instance type
ec2.modify_instance_attribute(
    InstanceId=instance_id,
    InstanceType={
        'Value': new_instance_type,
    }
)

print(f"Instance {instance_id} type has been changed to {new_instance_type}.")
