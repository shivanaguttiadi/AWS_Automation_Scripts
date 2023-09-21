import boto3
import pandas as pd
from tabulate import tabulate

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')

# Specify the granularity and metrics for the estimation
granularity = 'DAILY'
metrics = ['BlendedCost']

# Get the current date
end_date = pd.Timestamp.now(tz='UTC')

# Calculate the start date as 3 months ago from the end date
start_date = end_date - pd.DateOffset(months=3) + pd.DateOffset(days=1)

# Create a list to store the data for each month
monthly_data = []

# Loop through the last 3 months
for i in range(3):
    # Calculate the end of the current month
    current_month_end = start_date + pd.DateOffset(months=1) - pd.DateOffset(days=1)

    # Get the cost and usage data for the current month
    response = ce.get_cost_and_usage(
        TimePeriod={'Start': start_date.strftime('%Y-%m-%d'), 'End': current_month_end.strftime('%Y-%m-%d')},
        Granularity=granularity,
        Metrics=metrics,
        GroupBy=[
            {'Type': 'DIMENSION', 'Key': 'SERVICE'},
            {'Type': 'DIMENSION', 'Key': 'REGION'},
        ]
    )

    # Extract the results for the current month
    results = response['ResultsByTime']
    
    if results:
        last_month_costs = results[-1]['Groups']
        monthly_data.append({'Month': start_date.strftime('%B %Y'), 'Data': last_month_costs})
    
    # Move to the next month
    start_date = current_month_end + pd.DateOffset(days=1)

# Create a dictionary to store costs by month
costs_by_month = {}

# Extract costs by month from the data
for month_data in monthly_data:
    month = month_data['Month']
    costs = {}
    
    for group in month_data['Data']:
        service = group['Keys'][0]
        region = group['Keys'][1]
        cost = group['Metrics']['BlendedCost']['Amount']
        
        if service not in costs:
            costs[service] = {}
        costs[service][region] = cost
    
    costs_by_month[month] = costs

# Create a list of rows for the table
table_data = []

for month, costs in costs_by_month.items():
    row = [month]
    
    for service, regions in costs.items():
        for region, cost in regions.items():
            row.extend([service, region, cost])
    
    table_data.append(row)

# Create a table and print it
headers = ["Month", "Service", "Region", "Cost"]
table = tabulate(table_data, headers, tablefmt="grid", numalign="center")
print("\nAWS Service Costs by Region (Last 3 Months):\n")
print(table)
