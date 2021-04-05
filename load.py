import json
import boto3
s3_client = boto3.client('s3')

def lambda_handler(event, context):
       
       print('starting the lambda_handler')
       
       print('Getting bucket name')
       bucket=event['Records'][0]['s3']['bucket']['name']
       print(bucket)
       print('Getting file name')
       file_name=event['Records'][0]['s3']['object']['key']
       print(file_name)
       json_object=s3_client.get_object(Bucket=bucket,Key=file_name)
       jsonFileReader=json_object['Body'].read()
       json_File=json.loads(jsonFileReader)
       
       print('jsonFileReader'+str(jsonFileReader))
       
       print('json_File'+str(json_File))
       s3_client.put_object(Bucket='outputsource',Key=file_name,Body=str(json.dumps(json_File)))
       #s3_client.put_object(Bucket='outputsource',Key=file_name,Body=(bytes(json.dumps(json_File).encode('UTF-8'))
