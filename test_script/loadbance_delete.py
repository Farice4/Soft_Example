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


def find_loadbance(conn):
    print "Find Loadbance:"
    lb=conn.network.find_pool('5f483fa3-3c3e-4dc3-9ede-e9f4a97729a1')
    print "Pool id......"
    print lb.id
    print "members......"
    print lb.members
    print "health monitors......"
    print lb.health_monitors
    print "lb vip......"
    print lb.vip_id
    return lb

#find_loadbance(conn)

def del_members(conn, lb):
    print "delete member from lb pool"
    members = lb.members
    for member in members:
    	conn.network.delete_pool_member(member)
    
#del_members(conn, find_loadbance(conn)) 

def disconn_delete_health(conn, lb, health_id):
    print "disconnect health to pool"
    pool_id = lb.id
    conn.network.delete_health_associate(pool_id, health_id)
    print "delete healthmonitor"
    conn.network.delete_health_monitor(health_id)

#disconn_delete_health(conn, find_loadbance(conn), 'dfee1b29-4c46-405b-8562-8c9956e5fd9d')

def del_vip(conn, lb):
    print "Delete lb vip:"
    vip = lb.vip_id
    conn.network.delete_listener(vip)

#del_vip(conn, find_loadbance(conn))

def del_pool(conn):
    print "Delete lb pool:"
    conn.network.delete_pool('5f483fa3-3c3e-4dc3-9ede-e9f4a97729a1')
#del_pool(conn)

def get_pool(conn):
    print "List pool: "
    pools = conn.network.pools()
    for pool in pools:
        print pool

get_pool(conn)

