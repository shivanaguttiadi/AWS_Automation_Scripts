import boto3
import csv
from tabulate import tabulate

# Initialize the EC2 client
ec2 = boto3.client('ec2')

# Replace 'your-volume-id' with the actual EBS volume ID
volume_id = 'vol-0249447083d3e1605'

# Record the volume's information before deletion
with open('deleted_volumes.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Get information about the volume (size and type)
    try:
        describe_response = ec2.describe_volumes(VolumeIds=[volume_id])
        volume_info = describe_response['Volumes'][0]
        size = volume_info['Size']
        volume_type = volume_info['VolumeType']
        
        # Write the information to the CSV file
        writer.writerow([volume_id, size, volume_type])
    except ec2.exceptions.ClientError as e:
        print(f"Error: {e}")

# Delete the EBS volume
try:
    ec2.delete_volume(VolumeId=volume_id)
    print(f"EBS volume {volume_id} deletion requested.")
except ec2.exceptions.ClientError as e:
    print(f"Error: {e}")

# Optionally, you can list all previously deleted volumes from the CSV file
with open('deleted_volumes.csv', mode='r') as file:
    reader = csv.reader(file)
    deleted_volume_info = list(reader)

if deleted_volume_info:
    # Create a table and print it
    table_headers = ["Volume ID", "Size (GiB)", "Volume Type"]
    print("List of Deleted EBS Volumes:")
    table = tabulate(deleted_volume_info, headers=table_headers, tablefmt="grid")
    print(table)
else:
    print("No deleted EBS volumes found in the record.")
