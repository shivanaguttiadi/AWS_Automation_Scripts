import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Replace 'igw-0123456789abcdef0' with the ID of the Internet Gateway you want to delete
igw_ids = ['ID igw-09a22dab83ece3da0']  # Replace with your IGW IDs

# Create a table to display the results
table = PrettyTable()
table.field_names = ["IGW ID", "VPC ID", "State", "Name", "Detached"]

# Loop through the list of IGW IDs and process each one
for igw_id in igw_ids:
    try:
        # Describe the IGW to get its details
        igw = ec2.describe_internet_gateways(InternetGatewayIds=[igw_id])['InternetGateways'][0]
        
        # Check if the IGW is attached to a VPC
        if igw.get('Attachments'):
            vpc_id = igw['Attachments'][0]['VpcId']
            state = "Attached"
        else:
            vpc_id = "N/A"
            state = "Detached"

        # Attempt to delete the IGW
        ec2.delete_internet_gateway(InternetGatewayId=igw_id)
        detached = "Yes"
    except Exception as e:
        vpc_id = "N/A"
        state = "Error"
        detached = "No"
    
    igw_name = igw.get('Tags', [{'Key': 'Name', 'Value': 'N/A'}])[0]['Value']
    
    # Add IGW details to the table
    table.add_row([igw_id, vpc_id, state, igw_name, detached])

# Print the table with IGW details
print(table)
