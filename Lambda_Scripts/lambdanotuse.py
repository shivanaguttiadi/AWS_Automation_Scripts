import boto3

# Initialize the Lambda client
lambda_client = boto3.client('lambda')

# Replace 'your-function-name' with the name of your Lambda function
function_name = 'ListofLambdafunctions'

try:
    # Get the Lambda function by its name
    response = lambda_client.get_function(FunctionName=function_name)

    # Print the entire response for debugging
    print(response)

    # Extract information about the function
    function_details = response['Configuration']

    # Print the function details
    print(f"Function Name: {function_details['FunctionName']}")
    print(f"Function ARN: {function_details['FunctionArn']}")
    print(f"Runtime: {function_details['Runtime']}")
    print(f"Handler: {function_details['Handler']}")
    # Add more attributes as needed

except lambda_client.exceptions.ResourceNotFoundException:
    print(f"Lambda function '{function_name}' not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
