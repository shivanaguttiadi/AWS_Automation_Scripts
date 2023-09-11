import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of VPC endpoint IDs that you want to delete
endpoint_ids_to_delete = ['vpce-0ce4bd4b691a5d7da', 'vpce-0e52251df1a7fb16b']  # Replace with your endpoint IDs

# Delete the specified VPC endpoints
response = ec2.delete_vpc_endpoints(VpcEndpointIds=endpoint_ids_to_delete)

# Check if there are any failures during deletion
if 'Unsuccessful' in response:
    for failure in response['Unsuccessful']:
        error_message = failure.get('Error', {}).get('Message', 'Unknown error')
        print(f"Failed to delete endpoint {failure.get('VpcEndpointId', 'Unknown ID')}: {error_message}")
else:
    print("All specified endpoints have been deleted.")

