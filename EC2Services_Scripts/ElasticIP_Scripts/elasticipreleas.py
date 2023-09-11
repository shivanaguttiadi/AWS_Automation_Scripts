import boto3
from prettytable import PrettyTable

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Replace 'your_elastic_ip' with the Elastic IP addresses you want to release
elastic_ip_addresses = ['44.197.35.29', '44.209.88.222']

# Initialize a table for displaying the results
table = PrettyTable()
table.field_names = ["Elastic IP Address", "Status"]

# Loop through the Elastic IP addresses and release each one
for elastic_ip_address in elastic_ip_addresses:
    try:
        # Describe the Elastic IP address to get the Allocation ID
        response = ec2.describe_addresses(Filters=[{'Name': 'public-ip', 'Values': [elastic_ip_address]}])

        if response['Addresses']:
            allocation_id = response['Addresses'][0]['AllocationId']
            ec2.release_address(AllocationId=allocation_id)
            table.add_row([elastic_ip_address, "Released"])
        else:
            table.add_row([elastic_ip_address, "Not Found"])
    except Exception as e:
        table.add_row([elastic_ip_address, f"Error: {str(e)}"])

# Print the table with the results
print(table)
