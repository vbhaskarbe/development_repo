import logging
import boto3
from botocore.exceptions import ClientError
from botocore.exceptions import NoCredentialsError
import os
##
## Author : Bhaskar Varadaraju
## A Python program to List buckets in S3 
##
## ******  IMPORTANT ******
##  PLEASE SET AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY in env before executing.
##

# Retrieve the list of existing buckets
s3 = boto3.client('s3',
    region_name='ap-south-1',
)
response = s3.list_buckets()

# Output the bucket names in S3
print('INFO: Existing buckets in S3:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


