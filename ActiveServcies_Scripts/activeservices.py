import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Get a list of all AWS services
all_services = session.get_available_services()

# Filter active services (some services may be disabled)
active_services = []

for service in all_services:
    if service == 'accessanalyzer':
        # Skip 'accessanalyzer' service as it doesn't have a policy
        continue
    
    try:
        # Check if there's a policy associated with the service (IAM)
        iam_client = session.client('iam')
        iam_client.get_policy(PolicyArn=f'arn:aws:iam::aws:policy/{service}')
        
        # Initialize the EC2 client outside the try-except block
        ec2_client = session.client(service, region_name='us-east-1')  # Use a default region for the check
        available_regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
        
        active_services.append((service, available_regions))
    except iam_client.exceptions.NoSuchEntityException:
        pass
    except ec2_client.exceptions.ClientError:
        pass

# Create a table from the active services list
table_data = []
for service, regions in active_services:
    table_data.append([service, ', '.join(regions)])

# Define table headers
headers = ["Active Services", "Available Regions"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))
