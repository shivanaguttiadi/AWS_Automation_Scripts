import boto3
from prettytable import PrettyTable
from datetime import datetime

# Create a Boto3 client for the EC2 service without specifying credentials or region
ec2 = boto3.client('ec2')

# Retrieve a list of key pairs
key_pairs = ec2.describe_key_pairs()['KeyPairs']

# Create a table with proper formatting for key pairs
table = PrettyTable()
table.field_names = ["Key Pair Name", "Creation Date"]

# Function to extract creation date if the name follows the expected format
def extract_creation_date(key_pair_name):
    try:
        return datetime.strptime(key_pair_name.split("_")[-1], '%Y-%m-%d_%H-%M-%S').strftime('%Y-%m-%d %H:%M:%S')
    except ValueError:
        return "N/A"

# Populate the table with key pair information
for key_pair in key_pairs:
    key_pair_name = key_pair['KeyName']
    creation_date = extract_creation_date(key_pair_name)

    table.add_row([key_pair_name, creation_date])

# Print the formatted table
print(table)
