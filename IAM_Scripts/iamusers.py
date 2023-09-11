import boto3
from tabulate import tabulate

# Initialize the IAM client
iam_client = boto3.client('iam')

# List all IAM users
response = iam_client.list_users()

# Initialize a list to store the table data
user_data = []

for user in response['Users']:
    user_name = user['UserName']
    created_date = user['CreateDate'].strftime('%Y-%m-%d %H:%M:%S')
    user_data.append([user_name, created_date])

# Calculate the total number of IAM users
total_users = len(user_data)

# Define the table headers
headers = ["User Name", "Created Date"]

# Print the table
print(tabulate(user_data, headers, tablefmt="pretty"))
print(f"Total IAM users: {total_users}")
