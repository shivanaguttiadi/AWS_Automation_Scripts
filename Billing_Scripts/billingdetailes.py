import boto3
import pandas as pd
from tabulate import tabulate
from datetime import datetime

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')

# Define the time period for cost estimation (last 6 months)
end_date = datetime.now()
start_date = end_date - pd.DateOffset(months=6)

# Specify the granularity and metrics for the estimation
granularity = 'MONTHLY'
metrics = ['BlendedCost']

# Additional settings for grouping by services and regions
group_by = [{'Type': 'DIMENSION', 'Key': 'SERVICE'}, {'Type': 'DIMENSION', 'Key': 'REGION'}]

# Get the cost and usage data, including service and region details
response = ce.get_cost_and_usage(
    TimePeriod={'Start': start_date.strftime('%Y-%m-%d'), 'End': end_date.strftime('%Y-%m-%d')},
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
        cost = float(group['Metrics']['BlendedCost']['Amount'])

        if service not in cost_data:
            cost_data[service] = {'Total Cost': 0}

        # Convert the timestamp to a month name
        timestamp = result['TimePeriod']['Start']
        month_name = datetime.strptime(timestamp, '%Y-%m-%d').strftime('%B')

        cost_data[service][month_name] = cost
        cost_data[service]['Total Cost'] += cost

# Create a pandas DataFrame from the cost data
df = pd.DataFrame(cost_data).T.fillna(0)

# Sort the DataFrame by 'Total Cost' in descending order
df = df.sort_values(by='Total Cost', ascending=False)

# Rearrange columns with "Total Cost" as the last column
columns = df.columns.tolist()
columns.remove('Total Cost')
columns.append('Total Cost')
df = df[columns]

# Round all values to two decimal places
df = df.round(2)

# Print the table using tabulate with left-aligned values
table = tabulate(df, headers='keys', tablefmt='pretty', numalign="left", stralign="left")

# Print the table
print("Cost Estimation by Service and Region (Last 6 Months) - Sorted by Total Cost (High to Low):\n")
print(table)
