"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2
from securityGroups import create_security_group


config = pulumi.Config()

bucket_name = config.require("s3-bucket")
# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket(bucket_name)

sg = create_security_group('my-sg')

ec2_instance = ec2.Instance("demo-instance",
                            ami='ami-0287a05f0ef0e9d9a',
                            instance_type='t2.micro',
                            vpc_security_group_ids=[sg.id],
                            key_name='test_key',
                            tags={
                                'Name': 'server1'
                            }
                            )


# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)
pulumi.export('instance_ip', ec2_instance.public_ip)
