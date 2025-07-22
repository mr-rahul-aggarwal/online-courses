#Imports
import boto3
import json

import os

with open('config.json', 'r') as aws_creds:
    data = aws_creds.read()
creds = json.loads(data)

 # Set environment variables for AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = creds['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = creds['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_DEFAULT_REGION'] = creds['AWS_DEFAULT_REGION']


#Create the client
client = boto3.client(service_name='bedrock-runtime')

prompt_data="""Human: Translate the following text (after "-") into french - Learning about generative ai is fun and exciting with Amazon Bedrock \n
    Assistant: """
#Construct the body
#specify your prompt
body = json.dumps({
    "prompt" : prompt_data,
    "max_tokens_to_sample": 200,
    "temperature": 0.5,
    "top_p": 0.5
})

#Specify model id and content types
# modelId = 'ai21.j2-mid-v1'
modelId = 'anthropic.claude-instant-v1'
accept = 'application/json'
contentType = 'application/json'

#Invoke the model
response = client.invoke_model(
    body=body, 
    modelId=modelId, 
    accept=accept, 
    contentType=contentType
)

#Extract the response
response_body = json.loads(response.get('body').read())


#Display the output
print(response_body['completion'])
# print(response_body.get('completions')[0].get('data').get('text'))