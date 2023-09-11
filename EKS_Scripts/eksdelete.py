import boto3

# Initialize the Boto3 EKS client (region will be determined by your AWS CLI/SDK config)
eks = boto3.client('eks')

# Specify the name of the EKS cluster to delete
cluster_name = 'my-eks-cluster'  # Replace with your EKS cluster name

# Delete the EKS node group (if applicable)
nodegroup_name = 'my-nodegroup'  # Replace with your node group name (if you have one)

try:
    eks.delete_nodegroup(
        clusterName=cluster_name,
        nodegroupName=nodegroup_name,
    )

    # Wait for the node group to be deleted (this may take a few minutes)
    waiter = eks.get_waiter('nodegroup_deleted')
    waiter.wait(clusterName=cluster_name, nodegroupName=nodegroup_name)
    print(f"Node group '{nodegroup_name}' deleted successfully.")
except eks.exceptions.ResourceNotFoundException:
    print(f"Node group '{nodegroup_name}' not found.")

# Delete the EKS cluster
eks.delete_cluster(name=cluster_name)

# Wait for the cluster to be deleted (this may take a few minutes)
waiter = eks.get_waiter('cluster_deleted')
waiter.wait(name=cluster_name)

print(f"Amazon EKS cluster '{cluster_name}' deleted successfully.")
