import boto3

# Initialize the Boto3 RDS client
rds = boto3.client('rds')

# Define the DB subnet group name and description
subnet_group_name = 'my-db-subnet-group'
subnet_group_description = 'My DB Subnet Group Description'

# Replace 'subnet-1', 'subnet-2', etc., with your actual subnet IDs
subnet_ids = ['subnet-087c072ab687dba30', 'subnet-06be9ea5583277dc9']

# Create the DB subnet group
response = rds.create_db_subnet_group(
    DBSubnetGroupName=subnet_group_name,
    DBSubnetGroupDescription=subnet_group_description,
    SubnetIds=subnet_ids
)

# Define RDS instance details
db_instance_identifier = 'my-rds-instance'
db_instance_class = 'db.t2.micro'
engine = 'postgres'
master_username = 'dbadmin'
master_password = 'Aadigs@123'
allocated_storage = 20  # in GB
db_name = 'mydatabase'

# Define security group IDs (modify as needed)
security_group_ids = ['sg-0123456789abcdef0']

# Create the RDS instance with the new DB subnet group
response = rds.create_db_instance(
    DBInstanceIdentifier=db_instance_identifier,
    AllocatedStorage=allocated_storage,
    DBInstanceClass=db_instance_class,
    Engine=engine,
    MasterUsername=master_username,
    MasterUserPassword=master_password,
    DBName=db_name,
    VpcSecurityGroupIds=security_group_ids,
    DBSubnetGroupName=subnet_group_name  # Use the newly created DB subnet group
)

# Wait for the RDS instance to be available (optional but recommended)
waiter = rds.get_waiter('db_instance_available')
waiter.wait(DBInstanceIdentifier=db_instance_identifier)

# Print the RDS instance details
print(f"RDS instance '{db_instance_identifier}' created successfully.")
