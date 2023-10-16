import boto3
from tabulate import tabulate

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')  # Replace with your desired region

# Define the time period for cost estimation (last month)
start_date = '2023-08-01'
end_date = '2023-08-31'

# Specify the granularity and metrics for the estimation
granularity = 'DAILY'
metrics = ['BlendedCost']  # Change to 'UnblendedCost' if needed

# Additional settings for grouping by service and region
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

# Create a list of dictionaries to store high cost data
high_cost_list = []

# Filter services with high costs
threshold = 10.0  # Lower threshold for testing
for result in results:
    for group in result['Groups']:
        service = group['Keys'][0]
        region = group['Keys'][1]
        cost = float(group['Metrics']['BlendedCost']['Amount'])

        if cost > threshold:
            high_cost_list.append([service, region, cost])

# Define table headers
headers = ["Service", "Region", "Blended Cost"]

# Print the table in tabular format
if high_cost_list:
    print(tabulate(high_cost_list, headers, tablefmt="grid"))
else:
    print("No services with high costs found.")
