import boto3

# Get the service resource
for x in range(1, 30, 1):
  try:
    sqs = boto3.resource('sqs', endpoint_url='http://localstack:4576', region_name='us-west-2')
    queue = sqs.create_queue(QueueName='test13', Attributes={'DelaySeconds': '5'})
    break
  except e:
    raise e
