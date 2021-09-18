import logging
import boto3
from botocore.exceptions import ClientError
import os

##
## PLEASE SET AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY in env before executing.
##

# Retrieve the list of existing buckets
s3 = boto3.client('s3',
region_name='ap-south-1',
)
response = s3.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name #.split(os.path.sep)[-1:][0] ##os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
        print(response)
    except ClientError as e:
        logging.error(e)
        return False
    return True


def download_file(file_name, bucket, object_name=None):
    #print("Downloading file : ", filename)
    s3.download_file('BUCKET_NAME', 'OBJECT_NAME', 'FILE_NAME')

print("Uploading file s3_bucket_list.py")
upload_file( './s3_bucket_list.py','bhasvarajenkins')

print("Downloading file s3_bucket_list.py")
download_file('01_shell.zip','bhasvarajenkins')

