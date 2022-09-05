import  boto3
client = boto3.client('s3')
response = client.list_buckets()
for name in response[input("Enter the bucket name:")]:

 if name:
      print("True, bucket name is already existed.")
else:
      print("False, given the wrong bucket name it's showing not existed.")

print(['Buckets'])


 