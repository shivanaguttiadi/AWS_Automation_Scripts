import boto3

# Initialize a Boto3 session
session = boto3.Session()

# Create a CloudWatch Logs client
logs_client = session.client('logs')

# Specify the list of log group names to delete
log_group_names_to_delete = [
    '/aws/apigateway/welcome',
    '/aws/codebuild/Build-Angular',
    '/aws/codebuild/Test-Angular',
    '/aws/codebuild/afe',
    '/aws/codebuild/angular-app',
    '/aws/codebuild/demo',
    '/aws/codebuild/demo-cloudfront',
    '/aws/codebuild/test',
    '/aws/codebuild/test5',
    '/aws/codebuild/testone',
    '/aws/eks/Vinod-DevOps-Test-2-EKS_DEMO/cluster',
    '/aws/lambda/Autoturnoff-TestLambdaFunction-jhsmb3DhTDZt',
    '/aws/lambda/DefineAuthChallengeFunction',
    '/aws/lambda/Ec2Autoturnoff-TestLambdaFunction-fnUvc94DygKN',
    '/aws/lambda/PRE_signup',
    '/aws/lambda/Pre_sign_up',
    '/aws/lambda/Process_purchase',
    '/aws/lambda/Turnoff-TestLambdaFunction-DcrYam67KWmU',
    '/aws/lambda/auth-challenge-poc-AuthFunction-gjDs22i7atR3',
    '/aws/lambda/lambdatest',
    '/aws/lambda/migrationuser',
    '/aws/lambda/newconfigs-CreateConfig-dhPDclGUjRpg',
    '/aws/lambda/recQuery-receipt',
]

# Initialize a count for deleted log groups
deleted_count = 0

# Delete each log group in the list
for log_group_name in log_group_names_to_delete:
    try:
        logs_client.delete_log_group(logGroupName=log_group_name)
        deleted_count += 1
        print(f"Deleted log group: {log_group_name}")
    except logs_client.exceptions.ResourceNotFoundException:
        # Log group not found, continue to the next one
        continue

# Print the count of deleted log groups
print(f"Deleted {deleted_count} log group(s).")
