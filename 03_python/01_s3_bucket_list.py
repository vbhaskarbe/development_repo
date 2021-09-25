import boto3
##
## Author : Bhaskar Varadaraju
## A Python3 program to List buckets in S3 
##
## ******  IMPORTANT ******
##  Set AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY in env before executing.
##

# Retrieve the list of existing buckets
s3 = boto3.client('s3',
    region_name='ap-south-1',
)
response = s3.list_buckets()

# Output the bucket names in S3
print('INFO: List of buckets in S3:')
for s3bucket in response['Buckets']:
    print(f'  {s3bucket["Name"]}')


