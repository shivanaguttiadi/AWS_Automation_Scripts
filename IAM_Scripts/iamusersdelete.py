import boto3
from tabulate import tabulate

# Initialize IAM client
iam_client = boto3.client('iam')

# List of IAM user names to delete (replace with your user names)
user_names_to_delete = ['TestUser1', 'TestUser2', 'TestUser3']

# Initialize a list to store deleted user details
deleted_user_details = []

# Delete IAM users and count the total
total_deleted_users = 0

# Delete IAM users
for user_name in user_names_to_delete:
    try:
        # Remove user from groups (if applicable)
        response_groups = iam_client.list_groups_for_user(UserName=user_name)
        for group in response_groups['Groups']:
            group_name = group['GroupName']
            iam_client.remove_user_from_group(GroupName=group_name, UserName=user_name)

        # Delete access keys (if any)
        response_access_keys = iam_client.list_access_keys(UserName=user_name)
        for access_key in response_access_keys['AccessKeyMetadata']:
            access_key_id = access_key['AccessKeyId']
            iam_client.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)

        # Delete IAM user
        iam_client.delete_user(UserName=user_name)

        total_deleted_users += 1
        deleted_user_details.append([user_name])
    except iam_client.exceptions.NoSuchEntityException:
        print(f"IAM user '{user_name}' not found.")
    except Exception as e:
        print(f"An error occurred while deleting IAM user '{user_name}': {str(e)}")

# Define the table headers
headers = ["Deleted User Name"]

# Print the table with proper spacing
table = tabulate(deleted_user_details, headers, tablefmt="grid")

# Print the table with the total number of deleted users
print(table)
print(f"Total deleted users: {total_deleted_users}")
