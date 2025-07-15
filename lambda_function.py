import boto3
from botocore.exceptions import ClientError

SENDER = "brianaendanawas.aws1@gmail.com"   # Verified SES sender email
RECIPIENT = "brianaendanawas.aws1@gmail.com"  # Receiver email (can be same as sender)
AWS_REGION = "us-east-1"  # SES region
SUBJECT = "Daily Reminder from Your AWS Lambda"
BODY_TEXT = ("Hello!\r\n"
             "This is your daily notification from AWS Lambda.")
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Hello!</h1>
  <p>This is your daily notification from <b>AWS Lambda</b>.</p>
</body>
</html>"""

CHARSET = "UTF-8"

def lambda_handler(event, context):
    client = boto3.client('ses', region_name=AWS_REGION)
    try:
        response = client.send_email(
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Body': {
                    'Html': {'Charset': CHARSET, 'Data': BODY_HTML},
                    'Text': {'Charset': CHARSET, 'Data': BODY_TEXT},
                },
                'Subject': {'Charset': CHARSET, 'Data': SUBJECT},
            },
            Source=SENDER,
        )
        return {
            'statusCode': 200,
            'body': f"Email sent! Message ID: {response['MessageId']}"
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': f"Error sending email: {e.response['Error']['Message']}"
        }
