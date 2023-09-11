import boto3

# Create a Boto3 client for the Elastic Load Balancing service without specifying credentials or region
elbv2 = boto3.client('elbv2')

# Define the load balancer name
load_balancer_name = 'MyLoadBalancer'

# Define the security group IDs for the load balancer
security_group_ids = ['sg-0123456789abcdef0', 'sg-abcdef01234567890']

# Define the subnet IDs where the load balancer will be deployed
subnet_ids = ['subnet-0123456789abcdef0', 'subnet-abcdef01234567890']

# Define the listener configuration for the load balancer
listeners = [
    {
        'Protocol': 'HTTP',
        'Port': 80,
        'DefaultActions': [
            {
                'Type': 'fixed-response',
                'FixedResponseConfig': {
                    'ContentType': 'text/plain',
                    'StatusCode': '200',
                    'ContentType': 'text/plain',
                    'ContentDescription': 'Hello from the load balancer!'
                }
            }
        ]
    }
]

# Create the load balancer
response = elbv2.create_load_balancer(
    Name=load_balancer_name,
    Subnets=subnet_ids,
    SecurityGroups=security_group_ids,
    Scheme='internet-facing',  # Replace with 'internal' for an internal load balancer
    LoadBalancerAttributes=[
        {
            'Key': 'idle_timeout.timeout_seconds',
            'Value': '60'  # Idle timeout in seconds
        }
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyLoadBalancer'
        }
    ],
    IpAddressType='ipv4',
    Scheme='internet-facing',
    LoadBalancerName=load_balancer_name,
    Listeners=listeners
)

# Retrieve the DNS name of the load balancer
dns_name = response['LoadBalancers'][0]['DNSName']

print(f'Load Balancer created with DNS name: {dns_name}')
