#Imports
import boto3
import botocore
import json

with open('config.json', 'r') as aws_creds:
    data = aws_creds.read()
creds = json.loads(data)

# Create a client for the Bedrock service using the specified credentials and region
bedrock = boto3.client(service_name='bedrock-runtime',
                        region_name=creds["AWS_DEFAULT_REGION"],
                        aws_access_key_id=creds["AWS_ACCESS_KEY_ID"],
                        aws_secret_access_key=creds["AWS_SECRET_ACCESS_KEY"])

#Setting the prompt
prompt_data = """Command: Write me a blog about coaching employees as a leader.

Blog:
"""

#Model specification
modelId = "amazon.titan-text-lite-v1"
# modelId = "anthropic.claude-instant-v1"
accept = "application/json"
contentType = "application/json"

#Configuring parameters to invoke the model
body = json.dumps({
  "inputText" : prompt_data,
  "textGenerationConfig" : {
    "maxTokenCount" : 1000
  }
})

#Invoke the model
response = bedrock.invoke_model(
  body = body, modelId = modelId, accept = accept, contentType = contentType
)

#Parsing and displaying the output
response_body = json.loads(response.get('body').read())
output = response_body.get('results')[0].get("outputText")
print(output)