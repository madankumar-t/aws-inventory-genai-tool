import boto3
from botocore.config import Config
from app.config import ORG_ROLE_NAME, AWS_TIMEOUTS


def assume_role(a, r):
    sts = boto3.client('sts')

    c = sts.assume_role(
        RoleArn=f'arn:aws:iam::{a}:role/{ORG_ROLE_NAME}',
        RoleSessionName='agent'
    )['Credentials']

    cfg = Config(**AWS_TIMEOUTS)

    return boto3.Session(
        aws_access_key_id=c['AccessKeyId'],
        aws_secret_access_key=c['SecretAccessKey'],
        aws_session_token=c['SessionToken'],
        region_name=r,
        #botocore_config=cfg
    )
