import boto3
import os


def handler_function():
    s3_client = boto3.client('s3')

    # BUCKET_PATH = "my-bucket-name/folder1/folder2/file.txt"
    bucket_path= os.getenv('BUCKET_PATH')
    #bucket_path= "my-bucket-name/folder1/folder2/file.txt"
    
    print(f'Bucket path: {bucket_path}')
    # ['my-bucket-name', 'folder1', 'folder2', 'file.txt']
   
    bucket_name = bucket_path.split('/')[0]
    # bucket_name = 'my-bucket-name'

    prefix = bucket_path.split(bucket_name + '/')[1]
    # ['my-bucket-name', 'folder1/folder2/file.txt' ]
    
    # will print bucket name and prefix 
    print(f'Bucket name: {bucket_name} and prefix: {prefix}')

    response = s3_client.lis