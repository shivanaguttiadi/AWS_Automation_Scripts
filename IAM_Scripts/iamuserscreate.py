import boto3
from tabulate import tabulate

# Initialize IAM client
iam_client = boto3.client('iam')

# List of IAM users to create with associated tags
users_with_tags = [
    {
        'UserName': 'TestUser1',
        'Tags': [
            {'Key': 'Environment', 'Value': 'Production'},
            {'Key': 'Department', 'Value': 'Engineering'},
        ],
    },
    {
        'UserName': 'TestUser2',
        'Tags': [
            {'Key': 'Environment', 'Value': 'Development'},
            {'Key': 'Department', 'Value': 'Marketing'},
        ],
    },
    {
        'UserName': 'TestUser3',
        'Tags': [
            {'Key': 'Environment', 'Value': 'Production'},
            {'Key': 'Department', 'Value': 'Finance'},
        ],
    },
]

# Create IAM users with tags and count the total
total_created_users = 0

# Initialize a list to store user details
user_details = []

# Create IAM users with tags
for user_info in users_with_tags:
    user_name = user_info['UserName']
    tags = user_info['Tags']

    try:
        # Create IAM user
        iam_client.create_user(UserName=user_name)

        # Add tags to the IAM user
        if tags:
            for tag in tags:
                iam_client.tag_user(
                    UserName=user_name,
                    Tags=[{'Key': tag['Key'], 'Value': tag['Value']}]
                )

        total_created_users += 1
        user_details.append([user_name, tags])
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"IAM user '{user_name}' already exists.")
    except Exception as e:
        print(f"An error occurred while creating IAM user '{user_name}': {str(e)}")

# Define the table headers
headers = ["User Name", "Tags"]

# Print the table with proper spacing
table = tabulate(user_details, headers, tablefmt="grid")

# Print the table with the total number of created users
print(table)
print(f"Total created users: {total_created_users}")
