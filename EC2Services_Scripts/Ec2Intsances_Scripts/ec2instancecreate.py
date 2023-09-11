import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace with your desired EC2 instance details
instance_count = 1
ami_id = 'ami-051f7e7f6c2f40dc1'  # Replace with a compatible AMI ID for the instance type
instance_type = 't2.micro'  # Choose an instance type that matches the AMI architecture
key_name = 'Adi_Admin_Ec2_Key'  # Replace with the name of your key pair
tag_name = 'Adi_AWS_Admin'
tag_value = 'Implement'
instance_name = 'Adi_AWS_Admin_ec2'  # Replace with your desired instance name

# Create EC2 instances with tags
response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    MinCount=instance_count,
    MaxCount=instance_count,
    KeyName=key_name,
)

# Extract the instance IDs of the newly created instances
instance_ids = [instance['InstanceId'] for instance in response['Instances']]

# Tag the instances with the desired tags
ec2.create_tags(
    Resources=instance_ids,
    Tags=[
        {
            'Key': 'Owner',
            'Value': 'Adi',
        },
        {
            'Key': 'Email_Id',
            'Value': 'adi.shiva@zapcg.com',
        },
    ],
)

# Prepare data for tabular format
table_data = [(instance_name, instance_id) for instance_id in instance_ids]

# Create a table and print it
table_headers = ["Instance Name", "Instance ID"]
table = tabulate(table_data, headers=table_headers, tablefmt="grid")
print("Created EC2 Instances:")
print(table)
