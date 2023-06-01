import json
import boto3
def lambda_handler(event, context):
    string = "whatever"
    file_name = "hello.txt"
    encoded_string = string.encode("utf-8")
    bucket_name = "s3bucket"
    file_name = "hello.txt"
    s3_path = "100001/20180223/" + file_name
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_string)
    