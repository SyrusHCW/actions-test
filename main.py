import boto3
import os



if __name__ == '__main__':
    '''
    client = boto3.client('route53', 
        aws_access_key_id=os.environ["KEY"], 
        aws_secret_access_key=os.environ["SECRET"], 
        region_name='us-east-1')


    response = client.create_hosted_zone(
        Name='oggilliamtest2.net',
        CallerReference='string2'
    )
    '''
    response = {'Test': 'ABC'}
    #env_file = os.getenv('GITHUB_ENV')
    print(str(response))
    print('1')
    #with open(env_file, "a") as myfile:
    #    myfile.write("MY_VAR1=MY_VALUE1")

