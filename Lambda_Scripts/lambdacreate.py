import boto3

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Specify the Lambda function properties
function_name = 'Thismyfirstlambdafunction'
runtime = 'python3.8'
handler = 'lambda_function.handler'  # Replace with your handler

# Specify the tags for the Lambda function (key-value pairs)
tags = {
    'Environment': 'Production',
    'Owner': 'Adi.shiva@zapcg.com'
}

# Create the Lambda function without specifying code
try:
    response = lambda_client.create_function(
        FunctionName=function_name,
        Runtime=runtime,
        Handler=handler,
        Role='your-role-arn',  # Replace with your role ARN
        Tags=tags  # Add the tags to the Lambda function
    )

    print(f"Lambda function '{function_name}' created with tags: {tags}")

except lambda_client.exceptions.ResourceConflictException:
    print(f"Lambda function '{function_name}' already exists.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
