import boto3
from tabulate import tabulate

# Initialize IAM client
iam_client = boto3.client('iam')

# List IAM users
response_users = iam_client.list_users()

# Initialize a list to store user details
user_details = []

# Iterate through IAM users
for user in response_users['Users']:
    user_name = user['UserName']

    # List groups for the user
    groups_response = iam_client.list_groups_for_user(UserName=user_name)
    groups = ', '.join([group['GroupName'] for group in groups_response['Groups']])

    # List attached policies (permissions)
    policies_response = iam_client.list_attached_user_policies(UserName=user_name)
    attached_policies = ', '.join([policy['PolicyName'] for policy in policies_response['AttachedPolicies']])

    # Get user tags
    user_tags_response = iam_client.list_user_tags(UserName=user_name)
    user_tags = ', '.join([f"{tag['Key']}={tag['Value']}" for tag in user_tags_response['Tags']])

    user_details.append([user_name, groups, attached_policies, user_tags])

# Define the table headers
headers = ["User Name", "Groups", "Permissions (Attached Policies)", "Tags"]

# Print the table
print(tabulate(user_details, headers, tablefmt="pretty"))
