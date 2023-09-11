import boto3
import datetime
from tabulate import tabulate

# Initialize the IAM client
iam_client = boto3.client('iam')

# List IAM users
response_users = iam_client.list_users()

# Initialize a list to store user details
user_details = []

# Iterate through IAM users
for user in response_users['Users']:
    user_name = user['UserName']
    groups_response = iam_client.list_groups_for_user(UserName=user_name)
    groups = ', '.join([group['GroupName'] for group in groups_response['Groups']])

    # Get the last accessed timestamp for the user
    user_last_activity = None
    access_keys = iam_client.list_access_keys(UserName=user_name)['AccessKeyMetadata']
    for key in access_keys:
        key_last_used = iam_client.get_access_key_last_used(AccessKeyId=key['AccessKeyId'])
        if key_last_used.get('LastUsedDate'):
            last_used_date = key_last_used['LastUsedDate']
            if user_last_activity is None or last_used_date > user_last_activity:
                user_last_activity = last_used_date

    if user_last_activity:
        last_activity_days = (datetime.datetime.now(datetime.timezone.utc) - user_last_activity).days
    else:
        last_activity_days = "No activity recorded"

    has_mfa = 'Yes' if user.get('PasswordLastUsed') else 'No'

    password_last_changed = user.get('PasswordLastUsed')
    if password_last_changed:
        password_age = (datetime.datetime.now(password_last_changed.tzinfo) - password_last_changed).days
    else:
        password_age = None

    user_details.append([user_name, groups, has_mfa, password_age, last_activity_days])

# Define the table headers
headers = ["User Name", "Groups", "MFA Enabled", "Password Age (days)", "Last Activety"]

# Print the table
print(tabulate(user_details, headers, tablefmt="pretty"))
