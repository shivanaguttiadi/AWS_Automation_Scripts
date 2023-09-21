import boto3
from time import sleep
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudFormation client
cf_client = session.client('cloudformation')

# Create the CloudFormation stack
stack_name = 'MyEC2Stack'  # Replace with your desired stack name
template_file = 'ec2_instance_template.yaml'

# You can pass parameters if needed
parameters = [
    {
        'ParameterKey': 'KeyName',
        'ParameterValue': 'Your-Key-Pair'  # Replace with your EC2 key pair name
    },
    {
        'ParameterKey': 'SecurityGroups',
        'ParameterValue': 'Your-Security-Group'  # Replace with your security group name
    }
]

create_response = cf_client.create_stack(
    StackName=stack_name,
    TemplateBody=open(template_file).read(),
    Parameters=parameters,
    Capabilities=['CAPABILITY_IAM']
)

print(f"Creating stack {stack_name}. Please wait...")

# Wait for the stack creation to complete
while True:
    stack_info = cf_client.describe_stacks(StackName=stack_name)['Stacks'][0]
    stack_status = stack_info['StackStatus']
    
    if stack_status in ('CREATE_COMPLETE', 'CREATE_FAILED', 'ROLLBACK_COMPLETE', 'ROLLBACK_FAILED'):
        break
    
    print(f"Stack status: {stack_status}. Waiting for completion...")
    sleep(10)

# List the created EC2 instances
ec2_client = session.client('ec2')
instances = ec2_client.describe_instances()

# Create a table to store EC2 instance information
table_data = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        private_ip = instance['PrivateIpAddress']
        state = instance['State']['Name']
        table_data.append([instance_id, instance_type, private_ip, state])

# Define table headers
headers = ["Instance ID", "Instance Type", "Private IP", "State"]

# Print the table of created EC2 instances
print("\nList of Created EC2 Instances:")
print(tabulate(table_data, headers, tablefmt="grid"))
