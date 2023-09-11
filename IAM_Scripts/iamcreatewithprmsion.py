import boto3
import json
from tabulate import tabulate

# Initialize IAM client
iam_client = boto3.client('iam')

# List of IAM users to create with associated policies
users_with_permissions = [
    {
        'UserName': 'User1',
        'Permissions': [
            {
                'PolicyName': 'User1ReadOnly',
                'PolicyDocument': {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:Get*",
                                "s3:List*"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
        ]
    },
    {
        'UserName': 'User2',
        'Permissions': [
            {
                'PolicyName': 'User2EC2FullAccess',
                'PolicyDocument': {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": "ec2:*",
                            "Resource": "*"
                        }
                    ]
                }
            }
        ]
    },
    {
        'UserName': 'User3',
        'Permissions': [
            {
                'PolicyName': 'User3S3ReadWrite',
                'PolicyDocument': {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Effect": "Allow",
                            "Action": [
                                "s3:Get*",
                                "s3:Put*"
                            ],
                            "Resource": "*"
                        }
                    ]
                }
            }
        ]
    },
]

# Initialize a list to store user details
user_details = []

# Create IAM users with permissions and get creation time
for user_info in users_with_permissions:
    user_name = user_info['UserName']
    permissions = user_info['Permissions']

    try:
        # Create IAM user
        iam_client.create_user(UserName=user_name)

        # Attach policies to the IAM user
        if permissions:
            for permission in permissions:
                policy_name = permission['PolicyName']
                policy_document = permission['PolicyDocument']
                
                # Create the policy
                iam_client.create_policy(
                    PolicyName=policy_name,
                    PolicyDocument=json.dumps(policy_document)  # JSON-encode the policy document
                )
                
                # Attach the policy to the user
                iam_client.attach_user_policy(
                    UserName=user_name,
                    PolicyArn=f"arn:aws:iam::YOUR_ACCOUNT_ID:policy/{policy_name}"  # Replace YOUR_ACCOUNT_ID
                )

        # Get user creation time
        user_response = iam_client.get_user(UserName=user_name)
        created_time = user_response['User']['CreateDate'].strftime('%Y-%m-%d %H:%M:%S')

        user_details.append([user_name, permissions, created_time])
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"IAM user '{user_name}' already exists.")
    except Exception as e:
        print(f"An error occurred while creating IAM user '{user_name}': {str(e)}")

# Define the table headers
headers = ["User Name", "Permissions", "Created Time"]

# Print the table with proper spacing
table = tabulate(user_details, headers, tablefmt="grid")

# Print the table
print(table)
