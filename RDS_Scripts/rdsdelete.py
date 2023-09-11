import boto3

# Initialize the Boto3 RDS client
rds = boto3.client('rds')

# Specify the DB instance identifier of the RDS instance to delete
db_instance_identifier = 'your-db-instance-identifier'

# Delete the RDS instance
response = rds.delete_db_instance(
    DBInstanceIdentifier=db_instance_identifier,
    SkipFinalSnapshot=True  # Set to True if you don't want a final DB snapshot
)

# Wait for the deletion to complete (optional but recommended)
waiter = rds.get_waiter('db_instance_deleted')
waiter.wait(DBInstanceIdentifier=db_instance_identifier)

# Print a success message
print(f"RDS instance '{db_instance_identifier}' has been deleted.")
