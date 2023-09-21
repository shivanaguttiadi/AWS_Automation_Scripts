import boto3
from tabulate import tabulate

# Initialize the AWS Cost Explorer client
ce = boto3.client('ce', region_name='us-east-1')  # Replace with your desired region

# Define the time period for cost estimation (last month)
start_date = '2023-08-01'
end_date = '2023-08-31'

# Specify the granularity and metrics for the estimation
granularity = 'DAILY'
metrics = ['UsageQuantity']

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

# Create a dictionary to store data by service and region
usage_data = {}

# Populate the dictionary with usage data
for result in results:
    for group in result['Groups']:
        service = group['Keys'][0]
        region = group['Keys'][1]
        usage_quantity = group['Metrics']['UsageQuantity']['Amount']

        if service not in usage_data:
            usage_data[service] = {}

        usage_data[service][region] = usage_quantity

# Create a list of dictionaries to store high usage data
high_usage_list = []

# Filter services with high usage
threshold = 100000  # You can adjust this threshold as needed
for service, regions in usage_data.items():
    for region, usage_quantity in regions.items():
        if float(usage_quantity) > threshold:
            high_usage_list.append([service, region, usage_quantity])

# Define table headers
headers = ["Service", "Region", "Usage Quantity"]

# Print the table in tabular format
if high_usage_list:
    print(tabulate(high_usage_list, headers, tablefmt="grid"))
else:
    print("No services with high usage found.")
