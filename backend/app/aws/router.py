from app.aws.org import list_accounts
from app.aws.session import assume_role
from app.aws.regions import resolve_regions
from app.collectors import ec2,s3,iam,rds,eks
from app.collectors.vpc import collect_vpc
MAP={'ec2':ec2.collect,'s3':s3.collect,'iam':iam.collect,'rds':rds.collect,'eks':eks.collect,'vpc':collect_vpc}
def route_request(i):
 out={}
 for a in list_accounts():
  out[a]={}
  for r in resolve_regions(i.get('regions')):
   s=assume_role(a,r);out[a][r]={k:MAP[k](s) for k in i['services']}
 return out