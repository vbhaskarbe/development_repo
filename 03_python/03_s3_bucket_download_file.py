import boto3
import os
##
## Author : Bhaskar Varadaraju
## A Python3 program to Download an existing file from S3
##       
## ******  IMPORTANT ******
##  PLEASE SET AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY in env before executing.
##
""" Input:
export S3_DOWNLOAD_FILENAME='01_shell.zip'
export S3_DOWNLOAD_LOCALNAME='/tmp/01_shell_local.zip'
export S3_BUCKET_NAME='bhasvarajenkins'
"""

def download_from_aws_s3(bucket, remote_file, local_file):
    print("Downloading file : ", remote_file)
    s3_client = boto3.client('s3',
        region_name='ap-south-1',
    )
    s3_client.download_file(bucket, remote_file, local_file)

s3_file_name      = os.environ.get('S3_DOWNLOAD_FILENAME')
s3_local_filepath = os.environ.get('S3_DOWNLOAD_LOCALNAME')
s3_bucket_name    = os.environ.get('S3_BUCKET_NAME')

download_from_aws_s3( s3_bucket_name, s3_file_name, s3_local_filepath)

