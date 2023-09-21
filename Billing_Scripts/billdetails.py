import boto3
import pandas as pd
from tabulate import tabulate
from datetime import datetime

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

# Create a dictionary to store data by service and region
cost_data = {}

# Populate the dictionary with cost data
for result in results:
    for group in result['Groups']:
        service = group['Keys'][0]
        region = group['Keys'][1]
        cost = group['Metrics']['BlendedCost']['Amount']

        if service not in cost_data:
            cost_data[service] = {}

        # Convert the timestamp to a month name
        timestamp = result['TimePeriod']['Start']
        month_name = datetime.strptime(timestamp, '%Y-%m-%d').strftime('%B')

        cost_data[service][month_name] = cost

# Create a pandas DataFrame from the cost data
df = pd.DataFrame(cost_data).T.fillna('N/A')

# Print the table
print("Cost Estimation by Service and Region (Last 6 Months):\n")
print(tabulate(df, headers='keys', tablefmt='pretty'))
