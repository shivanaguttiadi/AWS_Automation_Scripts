import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Replace 'your-nat-gateway-id' with the ID of the NAT Gateway you want to delete
nat_gateway_id = 'your-nat-gateway-id'  # Replace with your NAT Gateway ID

# Delete the NAT Gateway
response = ec2.delete_nat_gateway(NatGatewayId=nat_gateway_id)

# Check if the NAT Gateway was deleted successfully
if response['ResponseMetadata']['HTTPStatusCode'] == 200:
    print(f'NAT Gateway with ID {nat_gateway_id} has been deleted successfully.')
else:
    print(f'Failed to delete NAT Gateway with ID {nat_gateway_id}.')
