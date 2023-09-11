import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of all Network ACLs
network_acls = ec2.describe_network_acls()['NetworkAcls']

# Retrieve a list of all subnets
subnets = ec2.describe_subnets()['Subnets']

# Create a set to store Network ACL IDs that are associated with a subnet
associated_network_acl_ids = set()

# Find Network ACLs that are associated with a subnet
for subnet in subnets:
    if 'NetworkAclId' in subnet:
        associated_network_acl_ids.add(subnet['NetworkAclId'])

# List to store Network ACL IDs that are not dependent
independent_network_acl_ids = []

# Find Network ACLs that are not associated with any subnet
for network_acl in network_acls:
    network_acl_id = network_acl['NetworkAclId']
    
    if network_acl_id not in associated_network_acl_ids:
        independent_network_acl_ids.append(network_acl_id)

# Print the list of independent Network ACL IDs
print("Network ACLs with No Subnet Dependencies:")
for network_acl_id in independent_network_acl_ids:
    print(network_acl_id)
