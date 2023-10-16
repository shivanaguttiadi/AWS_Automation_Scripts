import boto3
from datetime import datetime as dt, timedelta
from tabulate import tabulate

# Initialize Boto3 clients for CloudWatch and CloudWatch Logs
logs_client = boto3.client('logs')
cloudwatch_client = boto3.client('cloudwatch')

# Calculate start and end dates for the 7-day window
end_date = dt.today().isoformat(timespec='seconds')
start_date = (dt.today() - timedelta(days=7)).isoformat(timespec='seconds')

print("Looking from %s to %s" % (start_date, end_date))

# Create a paginator to list all log groups
paginator = logs_client.get_paginator('describe_log_groups')
pages = paginator.paginate()

data = []

for page in pages:
    for json_data in page['logGroups']:
        log_group_name = json_data.get("logGroupName")

        # Query CloudWatch Metrics for IncomingBytes in the past 7 days
        cw_response = cloudwatch_client.get_metric_statistics(
            Namespace='AWS/Logs',
            MetricName='IncomingBytes',
            Dimensions=[
                {
                    'Name': 'LogGroupName',
                    'Value': log_group_name
                },
            ],
            StartTime=start_date,
            EndTime=end_date,
            Period=3600 * 24 * 7,  # 7 days in seconds
            Statistics=['Sum'],
            Unit='Bytes'
        )

        if len(cw_response.get("Datapoints")):
            stats_data = cw_response.get("Datapoints")[0]
            stats_sum = stats_data.get("Sum")
            sum_GB = stats_sum / (1000 * 1000 * 1000)  # Convert to GB

            if sum_GB > 1.0:
                data.append([log_group_name, "%.2f GB" % sum_GB])

# Print the table
headers = ["Log Group Name", "IncomingBytes"]
print(tabulate(data, headers, tablefmt="grid"))
