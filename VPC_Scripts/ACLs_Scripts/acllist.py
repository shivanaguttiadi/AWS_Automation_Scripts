import boto3
from tabulate import tabulate

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all VPCs
vpcs = ec2.describe_vpcs()

# Create a table to store the ACL details
table_data = []

# Iterate through each VPC
for vpc in vpcs['Vpcs']:
    vpc_id = vpc['VpcId']
    vpc_name = f"VPC {vpc_id}"
    
    # Retrieve the list of ACLs in the VPC
    response = ec2.describe_network_acls(Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}])
    
    # Iterate through the ACLs in the VPC
    for acl in response['NetworkAcls']:
        acl_id = acl['NetworkAclId']
        is_default = acl['IsDefault']
        table_data.append([vpc_name, acl_id, is_default])

# Print the ACL details in table format
table_headers = ["VPC Name", "ACL ID", "Is Default"]
print(tabulate(table_data, headers=table_headers, tablefmt="pretty"))
