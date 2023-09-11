import boto3
from tabulate import tabulate

# Initialize the Boto3 SNS client
sns = boto3.client('sns')

# List all SNS topics
response = sns.list_topics()

# Create a list to store subscription details
subscription_details = []

# Iterate through the list of topics
for topic in response.get('Topics', []):
    # Get topic ARN
    topic_arn = topic['TopicArn']

    # Get topic name from ARN
    topic_name = topic_arn.split(':')[-1]

    # List subscriptions for the topic
    subscriptions = sns.list_subscriptions_by_topic(TopicArn=topic_arn).get('Subscriptions', [])

    # Get subscription details and add them to the list
    for sub in subscriptions:
        protocol = sub['Protocol']
        endpoint = sub['Endpoint']

        # Add topic name, endpoint, and protocol to the list
        subscription_details.append([topic_name, endpoint, protocol])

# Create a table and print it for subscription information
table_headers = ["Topic Name", "Endpoint", "Protocol"]
table = tabulate(subscription_details, headers=table_headers, tablefmt="grid")

# Print the list of SNS topics with their subscription details in table format
print("List of SNS Topics with Subscription Details:")
print(table)
