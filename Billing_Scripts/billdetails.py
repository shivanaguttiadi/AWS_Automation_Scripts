import boto3
from tabulate import tabulate

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')

# Define the time period for cost estimation (last 6 months)
start_date = '2023-03-01'
end_date = '2023-09-01'

# Specify the granularity and metrics for the estimation
granularity = 'MONTHLY'
metrics = ['BlendedCost']

# Additional settings for grouping by services and regions
group_by = [{'Type': 'DIMENSION', 'Key': 'SERVICE'}, {'Type': 'DIMENSION', 'Key': 'REGION'}]

# Get the cost and usage data, including service and region details
response = ce.get_cost_and_usage(
    TimePeriod={'Start': start_date, 'End': end_date},
    Granularity=granularity,
    Metrics=metrics,
    GroupBy=group_by
)

# Extract the results
results = response['ResultsByTime']

# Prepare data for tabular format
table_data = []

# Create a header row with the months
header_row = ["Service", "Region"]
for result in results:
    date = result['TimePeriod']['Start']
    header_row.append(date)
table_data.append(header_row)

# Populate the table with cost data
for result in results:
    for group in result['Groups']:
        service = group['Keys'][0]
        region = group['Keys'][1]
        cost = group['Metrics']['BlendedCost']['Amount']
        row = [service, region]
        row.extend(['N/A'] * (len(header_row) - 2))  # Fill with 'N/A' for other months
        row.append(cost)
        table_data.append(row)

# Create a table and print it
table = tabulate(table_data, tablefmt="grid")
print("Cost Estimation by Service and Region (Last 6 Months):")
print(table)
