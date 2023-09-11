import boto3

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Define a list of route table IDs that you want to delete
route_table_ids_to_delete = ['rtb-0675fba41539e6ea9']  # Replace with your route table IDs

# Loop through the list of route table IDs and delete each route table
for route_table_id in route_table_ids_to_delete:
    try:
        ec2.delete_route_table(RouteTableId=route_table_id)
        print(f'Deleted route table {route_table_id}')
    except Exception as e:
        print(f'Failed to delete route table {route_table_id}: {str(e)}')

# Print a confirmation message when all route tables have been deleted
print('All specified route tables have been deleted.')
