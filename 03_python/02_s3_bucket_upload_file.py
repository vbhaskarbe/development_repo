##
## Author : Bhaskar Varadaraju
## A Python3 program to Upload a new file to s3 bucket
##
## ******  IMPORTANT : Set below before executing ******
##  export AWS_ACCESS_KEY_ID=<Your_Aws_KeyId>
##  export AWS_SECRET_ACCESS_KEY=<Your_Aws_Secret_Access_Key>
##
import boto3
from botocore.exceptions import NoCredentialsError
import os

""" Input:
export S3_UPLOAD_LOCALFILE='./s3_bucket_upload_file.py'
export S3_UPLOAD_FILENAME='s3_bucket_upload_file.py'
export S3_BUCKET_NAME='<your_s3_bucket_name>'
"""
def upload_to_aws_s3(local_file, bucket, s3_file):
    """Upload a file to an S3 bucket
    :param local_file: File to upload
    :param bucket    : Bucket to upload to
    :param s3_file   : S3 object name or default file_name
    :return: True if file was uploaded, else False
    """
    s3_client = boto3.client('s3',
        region_name='ap-south-1',
    )
    try:
        print("Uploading file: ", local_file)
        response = s3_client.upload_file(local_file, bucket, s3_file, ExtraArgs = {'ACL': 'public-read'})
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

s3_local_upload_file = os.environ.get('S3_UPLOAD_LOCALFILE')
s3_remote_file_name  = os.environ.get('S3_UPLOAD_FILENAME')
s3_bucket_name       = os.environ.get('S3_BUCKET_NAME')

upload_to_aws_s3( s3_local_upload_file, s3_bucket_name, s3_remote_file_name)

