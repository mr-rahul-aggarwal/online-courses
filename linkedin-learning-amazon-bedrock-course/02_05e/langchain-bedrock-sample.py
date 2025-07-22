#Imports
import boto3
from langchain.llms.bedrock import Bedrock
import json
import os

with open('config.json', 'r') as aws_creds:
    data = aws_creds.read()
creds = json.loads(data)

 # Set environment variables for AWS credentials
os.environ['AWS_ACCESS_KEY_ID'] = creds['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY'] = creds['AWS_SECRET_ACCESS_KEY']
os.environ['AWS_DEFAULT_REGION'] = creds['AWS_DEFAULT_REGION']


boto3_client = boto3.client('bedrock-runtime')

#setting model inference parameters
inference_modifier = {
  "temperature" : 0.5,
  "top_p" : 1,
  "max_tokens_to_sample" : 1000
}

#Create the llm
llm = Bedrock(
  model_id="anthropic.claude-instant-v1",
  client = boto3_client,
  model_kwargs= inference_modifier
)

#Generate the response
response = llm.invoke ("""
  Human: Write an email from Mark, Hiring Manager,
  welcoming a new employee "John Doe" to the company on his first day.
                       
  Answer:""")


#Display the result
print (response)
