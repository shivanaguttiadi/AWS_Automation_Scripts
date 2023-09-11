import boto3

# Initialize the EKS client
eks = boto3.client('eks')

# List the EKS clusters
response = eks.list_clusters()

# Extract and print the cluster names
clusters = response.get('clusters', [])
for cluster in clusters:
    print("EKS Cluster:", cluster)
