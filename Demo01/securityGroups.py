from pulumi_aws import ec2


# Create EC2 security group
def create_security_group(security_group_name):
    sg = ec2.SecurityGroup(security_group_name,description='security group for my-vm')

    allow_ssh = ec2.SecurityGroupRule('AllowSSH',
                                    type= 'ingress',
                                    from_port=22,
                                    to_port=22,
                                    protocol='tcp',
                                    cidr_blocks=['0.0.0.0/0'],
                                    security_group_id= sg.id)
    return sg