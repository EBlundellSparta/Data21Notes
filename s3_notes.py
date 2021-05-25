import boto3
from pprint import pprint
import json
import pandas as pd
import io

s3_client = boto3.client('s3')
bucket_list = s3_client.list_buckets()

## This prints the list of buckets!!
# for index, bucket in enumerate(bucket_list['Buckets'], start=1):
#     print(f"{index}:", bucket['Name'])


bucket_name = 'data-eng-resources'
## This would just look at everything in the data-eng-resources bucket
# bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name)

# This would only look in the big-data/pig-demo prefix of the bucket
bucket_contents = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='python/')

## This prints the name of each document within the bucket
# for name in bucket_contents['Contents']:
#     print(name['Key'])

## Second method to print the name of each document
# s3_resource = boto3.resource('s3')
# bucket = s3_resource.Bucket(bucket_name)
# contents = bucket.objects.all()

# for object in contents:
#     print(object.key)

## Reading from a csv file
# s3_object = s3_client.get_object(
#     Bucket=bucket_name,
#     Key='python/fish-market.csv'
# )

# contents = s3_object['Body']
# df = pd.read_csv(contents)
# print(df)

with open("ed-dict.json") as jsonfile:
    my_dict = json.load(jsonfile)

## Method 1 for uploading json file onto the s3 bucket
# s3_client.upload_file(
#     Filename="ed-dict.json",
#     Bucket="data-eng-resources",
#     Key="Data21/eblundell.json"
# )

## Method 2 for uploading/putting the json file onto the bucket
# s3_client.put_object(
#     Body=json.dumps(my_dict),
#     Bucket="data-eng-resources",
#     Key="Data21/Put/eblundell.json"
# )

# Using Pandas this creates a dataframe and the string buffer is used as a temporary hold
df = pd.DataFrame([[1, 2, 3, 4], [5, 6, 7, 8]])
str_buffer = io.StringIO()
df.to_csv(str_buffer)

## This puts the dataframe onto the bucket
# s3_client.put_object(
#     Body=str_buffer.getvalue(),
#     Bucket="data-eng-resources",
#     Key="Data21/CSV/eblundell.csv"
# )


## This is another method you could do instead to put the dataframe onto the bucket
# s3_resource = boto3.resource('s3')
# s3_resource.Object("data-eng-resources","Data21/CSV/eblundell.csv").put(Body=str_buffer.getvalue())