from botocore.config import Config
from app.config import AWS_TIMEOUTS

def collect(session):
    cfg = Config(**AWS_TIMEOUTS)
    c = session.client("ec2", config=cfg)

    return {
        "instances": [
            i for r in c.describe_instances()["Reservations"]
            for i in r["Instances"]
        ],
        "security_groups": c.describe_security_groups()["SecurityGroups"]
    }