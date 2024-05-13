import boto3
import os



if __name__ == '__main__':
    client = boto3.client('route53', 
        aws_access_key_id=os.environ["KEY"], 
        aws_secret_access_key=os.environ["SECRET"], 
        region_name='us-east-1')


    response = client.create_hosted_zone(
        Name='oggilliam.net',
        CallerReference='string'
    )
