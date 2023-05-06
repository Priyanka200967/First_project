import boto3


ec2 = boto3.client('ec2',
                    'us-east-1',
                    aws_access_key_id= 'AKIA2YFZYNUJXL7ZG34D',
                    aws_secret_access_key= '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')

conn = ec2.run_instances(InstanceType='t2.micro',
                        MaxCount=1,
                        MinCount=1,
                        ImageId='ami-0889a44b331db0194',
                        KeyName='test1')
