FROM python:3
ENV AWS_ACCESS_KEY_ID YOUR_ACCESS_KEY
ENV AWS_SECRET_ACCESS_KEY YOUR_SECRET_KEY

WORKDIR /usr/src/app

COPY mock_sqs_setup.py ./

RUN pip install boto3

CMD ["python", "./mock_sqs_setup.py"]
