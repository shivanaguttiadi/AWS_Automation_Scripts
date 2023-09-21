import boto3
from tabulate import tabulate

# Initialize the EC2 client
ec2_client = boto3.client('ec2')

# Initialize the EC2 resource
ec2_resource = boto3.resource('ec2')

# Get the list of running EC2 instances
instances = ec2_resource.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# Get the list of Elastic IPs
elastic_ips = ec2_client.describe_addresses()

# Get the list of Key pairs
key_pairs = ec2_client.describe_key_pairs()

# Get the list of Load balancers
elb_client = boto3.client('elbv2')
load_balancers = elb_client.describe_load_balancers()

# Get the list of Security groups
security_groups = ec2_client.describe_security_groups()

# Get the list of Volumes
volumes = ec2_client.describe_volumes()

# Prepare the data for the table
data = [
    ["Instances (running)", len(list(instances))],
    ["Auto Scaling Groups", 0],  # You can retrieve this information separately if needed
    ["Dedicated Hosts", 0],     # You can retrieve this information separately if needed
    ["Elastic IPs", len(elastic_ips['Addresses'])],
    ["Key pairs", len(key_pairs['KeyPairs'])],
    ["Load balancers", len(load_balancers['LoadBalancers'])],
    ["Placement groups", 0],    # You can retrieve this information separately if needed
    ["Security groups", len(security_groups['SecurityGroups'])],
    ["Snapshots", 0],           # You can retrieve this information separately if needed
    ["Volumes", len(volumes['Volumes'])]
]

# Define table headers
headers = ["Resource", "Count"]

# Print the table
print(tabulate(data, headers, tablefmt="grid"))
