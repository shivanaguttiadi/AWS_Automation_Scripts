import boto3

# Initialize the Boto3 SNS client
sns = boto3.client('sns')

# Replace 'your-topic-arn' with the ARN of the topic you want to delete
topic_arn = 'arn:aws:sns:us-east-1:973620134507:Shiavnaguttitest'

# Delete the SNS topic
sns.delete_topic(TopicArn=topic_arn)

# Print a message to confirm the deletion
print(f"Deleted SNS topic with ARN: {topic_arn}")
