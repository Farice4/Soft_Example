from openstack import profile
from openstack import connection
from openstack import exceptions

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

def delete_server(conn):
    print "Delete server:"
    try:
        res = conn.compute.delete_server("cf1cc2ef-632a-48c2-a7a9-fe81cdf5ed16", force=True)
    except exceptions.NotFoundException:
        res = True

    print res

#delete_server(conn)



def delete_server_metadata(conn):
    print "Delete server metadata:"
    keys = ['cluster_node_id']
    res = conn.compute.delete_server_metadata("d91a8522-dcf4-48fc-b239-e3f79578ccc1", keys)

    print res

#delete_server_metadata(conn)

def reset_server_state(conn):
    print "Reset server state:"
    res = conn.compute.reset_server_state("769bf949-989a-4dae-b291-5feb706fbfaf", "active")
    print res

#reset_server_state(conn)


def server_get(conn):
    print "Server get:"
    res = conn.compute.get_server("1c61e875-bf36-4339-a002-562288ecf4f0")
    print res
    print "----------------------------------"
    print res.image_id
    print "volume id is: %s" % res.attached_volumes
    for i in res.attached_volumes:
        print i['id']
    print "server uuid is:%s" % res.id

#server_get(conn)

def profile_get(conn):
    print "Profile get:"
    res = conn.cluster.get_profile("f0a57317-3b13-49ab-9a3e-14e39464335f")
    print res.spec['properties']['block_device_mapping_v2']
    print len(res.spec['properties']['block_device_mapping_v2'])
    

#profile_get(conn)

def cluster_delete(conn):
    print "Cluster delete:"
    cid = "6de95aaf-acc6-4970-b154-023fa35d0a03"
    ignore_missing = True
    force_delete = True
    res = conn.cluster.delete_cluster(cid, ignore_missing)
    print res

cluster_delete(conn)

