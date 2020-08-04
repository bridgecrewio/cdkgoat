from aws_cdk import core, \
    aws_s3 as s3, \
    aws_ec2 as ec2, \
    aws_kms as kms, \
    aws_rds as rds
from aws_cdk.aws_ec2 import Peer, Port
from aws_cdk.aws_rds import PostgresEngineVersion
from aws_cdk.core import RemovalPolicy


class CdkGoatStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        vpc = ec2.Vpc(self,
                      'vpc1'
                      )

        bucket_name = 'my-cdk-bucket'
        s3.Bucket(self,
                  bucket_name,
                  bucket_name=bucket_name,
                  access_control=s3.BucketAccessControl.PUBLIC_READ_WRITE,
                  removal_policy=RemovalPolicy.DESTROY)

        ec2.Volume(self, 'vol1', availability_zone='us-east-1a', size=core.Size.gibibytes(8))

        sg = ec2.SecurityGroup(self,
                               'sg1',
                               vpc=vpc)
        sg.add_ingress_rule(Peer.any_ipv4(), Port.tcp(22))

        kms.Key(self, 'kms1')

        rds.DatabaseInstance(self,
                             'rds1',
                             engine=rds.DatabaseInstanceEngine.postgres(version=PostgresEngineVersion.VER_12),
                             master_username='root',
                             vpc=vpc,
                             vpc_placement=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC))
