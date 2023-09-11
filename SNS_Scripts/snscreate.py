import boto3

# Initialize the Boto3 SNS client
sns = boto3.client('sns')

# Replace 'your-topic-name' with the desired topic name
topic_name = 'Shiavnaguttitest'

# Create the SNS topic
response = sns.create_topic(Name=topic_name)

# Extract the ARN of the created topic
topic_arn = response['TopicArn']

# Print the ARN of the created topic
print(f"Created SNS topic with ARN: {topic_arn}")
