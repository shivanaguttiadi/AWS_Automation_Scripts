import boto3
from tabulate import tabulate

# Initialize a Boto3 session
session = boto3.Session()

# Create a Cost Explorer client
ce = session.client('ce')

# Specify the time period for which you want to list alarms
start_date = '2023-09-01'
end_date = '2023-09-15'

# Get the AWS Cost Explorer results for the specified time period
results = ce.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity='DAILY',  # You can adjust the granularity as needed
    Metrics=['UnblendedCost'],  # You can specify the desired metrics
)

# Extract the data from the results
data = results['ResultsByTime'][0]['Groups']

# Prepare data for the table
table_data = []

for item in data:
    keys = item['Keys']
    cost = item['Metrics']['UnblendedCost']['Amount']
    table_data.append([keys[0], keys[1], cost])

# Define table headers
headers = ["Service", "Region", "Cost"]

# Print the table
print(tabulate(table_data, headers, tablefmt="grid"))
