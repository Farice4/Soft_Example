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
#list_pools(conn)

def list_server(conn):
    print "List server: "
    s1 = conn.compute.get_server('a8a7de59-a119-4b9b-abdb-143b18ea34fe')
    #s2 = conn.compute.get_server('ec4763c2-f62a-481e-92f7-78774cdd8cd6')
    #print s
    server1 = s1.to_dict()
    #server2 = s2.to_dict()
    print server1
    print '------------'
    #print server2
    print server1['image']
    #print server['image']
    #print server['attached_volumes']
    #print server['flavor']['id']
    #print s.attached_volumes['id']
    #print s.image

#list_server(conn)

def find_server(conn):
    print "find server:"
    res = conn.compute.get_server('51748b73-760e-43f6-ae5c-62398f22c7af')
    print res
    print res.id
    print res.image

#find_server(conn)

def create_server_image(conn):
    print "Create server image:"
    res = conn.compute.create_server_image("36a14b7d-475a-43c9-8074-c1de29b3bbdf","fabian_test_image1")
    return res
#csi = create_server_image(conn)
#print csi

def rebuild_server(conn):
    print "Rebuild server image:"
    attrs = {"image": "b7b29c68-45ef-412f-ae27-33adc9e0237d"}
    image = "b7b29c68-45ef-412f-ae27-33adc9e0237d"
    server = "2b4886cb-1ef9-4ef8-8478-f75f8760b5ce"
    name = 'test'
    admin_password = ""
    res = conn.compute.rebuild_server(server, name, admin_password, **attrs)
    print res

rebuild_server(conn)

