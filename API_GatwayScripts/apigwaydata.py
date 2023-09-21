import boto3
import prettytable as pt

# Initialize the Boto3 API Gateway client
api_gateway_client = boto3.client('apigateway')

# Initialize the Boto3 Lambda client
lambda_client = boto3.client('lambda')

# List API Gateway resources
response = api_gateway_client.get_rest_apis()

# Create a table to display the API Gateway details
table = pt.PrettyTable()
table.field_names = ["API Name", "API ID", "Stage Name", "Memory Size (MB)"]

# Iterate through the API Gateway resources
for api in response['items']:
    api_id = api['id']
    api_name = api['name']
    
    # Get the stages for the API
    stages = api_gateway_client.get_stages(restApiId=api_id)
    
    for stage in stages['item']:
        stage_name = stage['stageName']
        memory_size = 'N/A'
        
        # Get the associated Lambda function for the stage
        if 'deploymentId' in stage:
            deployment_id = stage['deploymentId']
            stage_variables = stage.get('variables', {})
            lambda_function_name = stage_variables.get('lambdaAlias')  # Assuming you have a variable named lambdaAlias
            
            if lambda_function_name:
                try:
                    # Get the Lambda function configuration
                    lambda_response = lambda_client.get_function_configuration(FunctionName=lambda_function_name)
                    memory_size = lambda_response['MemorySize']
                except Exception as e:
                    print(f"Error fetching Lambda function configuration for {lambda_function_name}: {str(e)}")
        
        table.add_row([api_name, api_id, stage_name, memory_size])

# Print the table
print(table)
