import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch client
cloudwatch_client = session.client('cloudwatch')

# List all CloudWatch dashboards
dashboards = cloudwatch_client.list_dashboards()

# Create a list to store dashboard information
dashboard_info = []

for dashboard in dashboards['DashboardEntries']:
    dashboard_name = dashboard['DashboardName']

    # Get dashboard details
    try:
        dashboard_details = cloudwatch_client.get_dashboard(DashboardName=dashboard_name)
        sharing_status = dashboard_details.get('DashboardArn', '').split(":")[-2]
        favorite_status = dashboard_details.get('IsFavorite', False)
        last_update_utc = dashboard_details.get('LastModified', 'N/A')

        dashboard_info.append([dashboard_name, sharing_status, favorite_status, last_update_utc])
    except Exception as e:
        print(f"Error retrieving details for dashboard {dashboard_name}: {str(e)}")

# Define table headers
headers = ["Name", "Sharing", "Favorite", "Last Update (UTC)"]

# Print the table of dashboards
print("\nList of CloudWatch Dashboards:")
print(tabulate(dashboard_info, headers, tablefmt="grid"))
