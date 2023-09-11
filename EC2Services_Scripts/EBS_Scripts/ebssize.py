import boto3

ec2 = boto3.client('ec2')

# Replace 'your-volume-id' with the actual EBS volume ID
volume_id = 'vol-0f736572cba8be1d6'

# Modify the EBS volume type and size
response = ec2.modify_volume(
    VolumeId=volume_id,
    VolumeType='gp3',  # Change to the desired volume type
    Size=8          # Change to the desired size in GiB (as an integer)
)

# Wait for the modification to complete (optional but recommended)
ec2.get_waiter('volume_modification').wait(
    VolumeIds=[volume_id],
    Filters=[
        {
            'Name': 'modification-state',
            'Values': ['completed'],
        },
    ],
)
