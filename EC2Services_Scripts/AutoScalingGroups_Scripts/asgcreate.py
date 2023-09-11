import boto3

# Create a Boto3 client for the Auto Scaling service without specifying credentials or region
autoscaling = boto3.client('autoscaling')

# Define the configuration for the Auto Scaling group
asg_name = 'MyAutoScalingGroup'  # Replace with your desired ASG name
launch_configuration_name = 'MyLaunchConfig'  # Replace with your launch configuration name
min_size = 1
max_size = 3
desired_capacity = 2
subnet_ids = ['subnet-xxxxxxxx', 'subnet-yyyyyyyy']  # Replace with your subnet IDs
security_group_ids = ['sg-xxxxxxxx']  # Replace with your security group IDs

# Create the Auto Scaling group
response = autoscaling.create_auto_scaling_group(
    AutoScalingGroupName=asg_name,
    LaunchConfigurationName=launch_configuration_name,
    MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity,
    VPCZoneIdentifier=','.join(subnet_ids),
    HealthCheckType='EC2',
    HealthCheckGracePeriod=300,  # Replace with your desired health check grace period
    AvailabilityZones=['us-east-1a', 'us-east-1b'],  # Replace with your desired availability zones
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyAutoScalingGroup'
        },
        {
            'Key': 'Environment',
            'Value': 'Production'
        }
    ],
    TerminationPolicies=['Default']
)

print(f'Auto Scaling group {asg_name} created.')
