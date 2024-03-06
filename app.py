from re import DEBUG
from flask import Flask

app = Flask(__name__)

import boto3

client = boto3.client('s3', region_name='us-west-2')

# Create a reusable Paginator
paginator = client.get_paginator('list_objects_v2')

# Create a PageIterator from the Paginator
page_iterator = paginator.paginate(Bucket='i-optics-data01')

c = 0
for page in page_iterator:
  for content in page['Contents']:
    if '.txt' not in content['Key']:
      print(c, content['Key'])
      c += 1
print(c)


@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
