import boto3

# Initialize the Boto3 RDS client
rds = boto3.client('rds')

# Describe all RDS instances
response = rds.describe_db_instances()

# Extract and print the list of RDS instance names and statuses
rds_instances = response.get('DBInstances', [])

if not rds_instances:
    print("No RDS databases in AWS")
else:
    for instance in rds_instances:
        instance_name = instance['DBInstanceIdentifier']
        instance_status = instance['DBInstanceStatus']
        print(f"RDS Instance Name: {instance_name}, Status: {instance_status}")
