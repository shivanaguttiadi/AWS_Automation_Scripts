import boto3
from tabulate import tabulate

# Initialize the IAM client
iam_client = boto3.client('iam')

# List IAM users
response_users = iam_client.list_users()
users_count = len(response_users['Users'])

# List IAM groups
response_groups = iam_client.list_groups()
groups_count = len(response_groups['Groups'])

# List IAM roles
response_roles = iam_client.list_roles()
roles_count = len(response_roles['Roles'])

# List IAM policies
response_policies = iam_client.list_policies()
policies_count = len(response_policies['Policies'])

# Print a summary of IAM details
print("IAM Dashboard Summary:")
print(f"Number of Users: {users_count}")
print(f"Number of Groups: {groups_count}")
print(f"Number of Roles: {roles_count}")
print(f"Number of Policies: {policies_count}")

# Optionally, you can list the details of these IAM entities in a table format.
# Example:
users_data = [[user['UserName'], user['CreateDate']] for user in response_users['Users']]
groups_data = [[group['GroupName'], group['CreateDate']] for group in response_groups['Groups']]
roles_data = [[role['RoleName'], role['CreateDate']] for role in response_roles['Roles']]

print("\nUsers:")
print(tabulate(users_data, headers=["User Name", "Created Date"], tablefmt="pretty"))

print("\nGroups:")
print(tabulate(groups_data, headers=["Group Name", "Created Date"], tablefmt="pretty"))

print("\nRoles:")
print(tabulate(roles_data, headers=["Role Name", "Created Date"], tablefmt="pretty"))
