import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# List of Network ACL IDs to delete
nacl_ids_to_delete = ['acl-07e96ccafcb5af4e0', 'acl-0cabe6e8388f1c77a']  # Replace with your NACL IDs

# Create a table to display the result
table = PrettyTable()
table.field_names = ["Network ACL ID", "Status"]

# Delete each Network ACL and record the result in the table
for nacl_id in nacl_ids_to_delete:
    try:
        ec2.delete_network_acl(NetworkAclId=nacl_id)
        status = "Deleted"
    except Exception as e:
        status = f"Failed: {str(e)}"
    
    table.add_row([nacl_id, status])

# Print the table with the result
print(table)
