# AWS Daily Email Notifier

This is a serverless project using AWS Lambda, Amazon SES, and EventBridge Scheduler to send automated daily email reminders.

## Features
- Sends daily email notifications using AWS services
- No server management required (fully serverless)
- Written in Python and deployable via AWS Lambda Console
- Free-tier friendly

## Technologies
- AWS Lambda
- Amazon Simple Email Service (SES)
- Amazon EventBridge Scheduler (CloudWatch Events)
- IAM Roles & Permissions

## How It Works
1. A Lambda function sends an email using the AWS SES service.
2. EventBridge Scheduler triggers the function every day.
3. The function uses Python's `boto3` library to call SES and send an email.

## File Structure
├── lambda_function.py # Main Lambda function
├── README.md # This file

## Setup Notes
- Both the sender and recipient emails must be verified in SES sandbox mode
- Ensure your Lambda function has SES permissions via IAM role
- You can test the function manually or wait for the scheduled trigger

## Author
Briana Endanawas
