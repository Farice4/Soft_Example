from openstack import profile
from openstack import connection

auth_url='http://10.10.10.114:5000/v3'
region='RegionOne'
project_name='admin'
user_domain_name='Default'
project_domain_name='Default'
username='admin'
password='123'

def create_connection():
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    conn = connection.Connection(profile=prof, auth_url=auth_url, project_name=project_name, username=username, password=password, user_domain_name=user_domain_name, project_domain_name=project_domain_name)
    return conn

conn = create_connection()

def list_policy_types(conn):
    print "List Policy Types:"
    for pt in conn.cluster.policy_types():
        print pt.to_dict()
#list_policy_types(conn)

def list_networks(conn):
    print "List networks:"
    for pt in conn.network.networks():
        print pt.to_dict() 
#list_networks(conn)

def list_pools(conn):
    print "List pools: "
    for pt in conn.network.pools():
        print pt.to_dict()
list_pools(conn)
