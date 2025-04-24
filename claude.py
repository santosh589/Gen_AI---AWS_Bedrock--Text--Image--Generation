import boto3
import json

prompt_data="""
Write series of events that took transformation changes of India since 1000 years from now...
"""

bedrock=boto3.client(service_name="bedrock-runtime")

payload={
    "prompt":prompt_data,
    "maxTokens":1024,
    "temperature":0.5,
    "topP":0.8
}
body = json.dumps(payload)
model_id = "ai21.j2-mid-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept="application/json",
    contentType="application/json",
)

response_body = json.loads(response.get("body").read())
response_text = response_body.get("completions")[0].get("data").get("text")
print(response_text)