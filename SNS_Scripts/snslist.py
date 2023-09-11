import boto3
from tabulate import tabulate
from datetime import datetime

# Initialize the Boto3 SNS client
sns = boto3.client('sns')

# List all SNS topics
response = sns.list_topics()

# Create a list to store topic details
topic_details = []

# Iterate through the list of topics
for topic in response.get('Topics', []):
    # Get topic ARN
    topic_arn = topic['TopicArn']

    # Get topic name from ARN
    topic_name = topic_arn.split(':')[-1]

    # Get topic attributes
    topic_attributes = sns.get_topic_attributes(TopicArn=topic_arn).get('Attributes', {})

    # Get topic creation date
    creation_date = topic_attributes.get('CreatedTimestamp')
    
    if creation_date:
        creation_date_str = datetime.fromtimestamp(int(creation_date) / 1000).strftime('%Y-%m-%d %H:%M:%S')
    else:
        creation_date_str = 'N/A'

    # Add topic information to the list
    topic_details.append([topic_name, creation_date_str])

# Create a table and print it for topic information
table_headers = ["Topic Name", "Created At"]
table = tabulate(topic_details, headers=table_headers, tablefmt="grid")

# Print the list of SNS topics with details in table format
print("List of SNS Topics with Created Dates:")
print(table)
