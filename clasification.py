import boto3
import base64
import json

ENDPOINT = "image-classification-2025-08-20-00-20-41-037"

runtime = boto3.client("sagemaker-runtime")

def lambda_handler(event, context):
    image_data = event["body"]["image_data"]
    image = base64.b64decode(image_data)

    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image
    )

    inferences = response["Body"].read().decode("utf-8")
    event["inferences"] = inferences

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    } 