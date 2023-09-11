import boto3

# Initialize the Boto3 EKS client
eks = boto3.client('eks', region_name='us-east-1')  # Replace with your desired region

# Specify the cluster configuration
cluster_name = 'Aadi_Demo'  # Replace with your desired cluster name
role_name = 'eks-cluster-role'  # Replace with your IAM role for EKS cluster
subnets = ['subnet-xxxxxxxxxxxxx', 'subnet-yyyyyyyyyyyyy']  # Replace with your subnet IDs
security_group_ids = ['sg-xxxxxxxxxxxxx']  # Replace with your security group IDs
nodegroup_name = 'my-nodegroup'  # Replace with your desired node group name
node_instance_type = 't2.micro'  # Replace with your desired instance type
node_min_size = 1
node_max_size = 3

# Create the EKS cluster
eks.create_cluster(
    name=cluster_name,
    roleArn=f'arn:aws:iam::xxxxxxxxxxxx:role/{role_name}',
    resourcesVpcConfig={
        'subnetIds': subnets,
        'securityGroupIds': security_group_ids,
    },
    version='1.21',  # Specify the Kubernetes version
)

# Wait for the cluster to be active (this may take a few minutes)
waiter = eks.get_waiter('cluster_active')
waiter.wait(name=cluster_name)

# Create the EKS node group
eks.create_nodegroup(
    clusterName=cluster_name,
    nodegroupName=nodegroup_name,
    scalingConfig={
        'minSize': node_min_size,
        'maxSize': node_max_size,
    },
    instanceTypes=[node_instance_type],
)

# Wait for the node group to be active (this may take a few minutes)
waiter = eks.get_waiter('nodegroup_active')
waiter.wait(clusterName=cluster_name, nodegroupName=nodegroup_name)

print(f"Amazon EKS cluster '{cluster_name}' and node group '{nodegroup_name}' created successfully.")
