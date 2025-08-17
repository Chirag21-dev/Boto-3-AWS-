import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

# Create a VPC
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.wait_until_available()
print(f'Created VPC: {vpc.id}')
