## Deploying an AWS Lambda Function with S3 Trigger Using Terraform

1. Cue:
   - Performs daily checks, downloading the current day’s file to process the information.
2. Craving:
   - Struggles to sort and locate the latest files efficiently.
3. Response:
   - To address the craving, response is to developed a lambda function that sorts files in a specific path into folders structured by dates(yy/mm/dd)
4. Reward:
   - is increased efficiency in locating and downloading the latest file, parallely reducing frustration.


### Python Module used
1. Boto3
2. OS

- **Boto3(python module)** is an official **AWS SDK**. Used to create, configure, and manage AWS services
- Botocore is basic of aws-cli written in python
- boto3 is written on top of botocore, having lots of objects and methods to work with aws services.

