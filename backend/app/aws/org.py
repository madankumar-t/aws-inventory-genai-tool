import boto3
def list_accounts():
 #o=boto3.client('organizations');p=o.get_paginator('list_accounts');return [a['Id'] for pg in p.paginate() for a in pg['Accounts'] if a['Status']=='ACTIVE']
 return ["964201074108"] 