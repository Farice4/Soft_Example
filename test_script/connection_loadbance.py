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


def list_pools(conn):
    print "List pools: "
    for pt in conn.network.pools():
        print pt.to_dict()
#list_pools(conn)

def find_pool(conn):
    print "Find Pools: "
    print conn.network.find_pool('1b614f12-56ae-45e9-84f3-cda906203a0e')

#find_pool(conn)

def delete_pool(conn):
    print "Delete Pools: "
    conn.network.delete_pool('e417cd50-118f-485c-9e38-003a3fb0f751')

#delete_pool(conn)

def create_pool(conn):
    print "Create Pools: "
    conn.network.create_pool({'spec':{"lb_method":"ROUND_ROBIN", "protocol":"HTTP", "subnet_id":"df68f190-8933-4064-98cf-2392cfc9f590"}})
#create_pool(conn)

def get_pool(conn):
    print "Get Pool:"
    pool=conn.network.find_pool('30fe3b2c-5691-4f6e-b43d-f3c859e5585e')
    print '.............'
    print '________pool id___________'
    print pool.id
    print '+++++++++vip id____________'
    print pool.vip_id
    print '________health_monitor______'
    print pool.health_monitors
    print '________pool status_________'
    print pool.status
    print '________subnet id___________'
    print pool.subnet_id
    
get_pool(conn)

def create_lister(conn):
    print "Create Listener:"
    spec = {
        'name':'test_vip',
        'protocol_port':'22',
        'protocol':'tcp',
        'subnet_id':'df68f190-8933-4064-98cf-2392cfc9f590',
        'pool_id':'10c2f2ab-80c7-4beb-a0c3-149a42109d66'
    }
    listener=conn.network.create_listener(spec)

#create_lister(conn)

def add_ass(conn):
    print "add ass:"
    conn.network.create_health_associate('114fe589-62a8-4b25-bac7-c2eeeab5da9e','4f82e4ad-3ee5-4fe2-98af-036e404a27b7')
#add_ass(conn)

def del_ass(conn):
    print "del ass:"
    conn.network.delete_health_associate('5f483fa3-3c3e-4dc3-9ede-e9f4a97729a1','dfee1b29-4c46-405b-8562-8c9956e5fd9d')

#del_ass(conn)
def del_health(conn):
    print "del ass:"
    conn.network.delete_health_monitor('dfee1b29-4c46-405b-8562-8c9956e5fd9d')

del_health(conn)

def get_net(conn):
    print "Get net: "
    subnet_obj=conn.network.get_subnet('df68f190-8933-4064-98cf-2392cfc9f590')
    print subnet_obj
    print "Net ID......"
    net_id = subnet_obj.network_id
    print net_id
    print "Get network......"
    network = conn.network.get_network(net_id)
    print network
    print '..........'
    print network.name
#get_net(conn)

def add_member(conn):
    print "Add loadbance member"
    kwargs = {
            'address': '7.7.7.50',
            'protocol_port': 80,
            'admin_state_up': True,
        }
    #import pdb;pdb.set_trace()
    member = conn.network.create_pool_member('d548b54a-d71f-47a2-972a-94b6046a6f48', **kwargs)
    print member.id 
#add_member(conn)

def del_member(conn):
    print "Del member"
    s = conn.network.delete_pool_member('42826869-0abc-4a6f-90e1-c3c6a328c248')
    print s
#del_member(conn)


def get_listener(conn):
    print "Get listener:"
    listener = conn.network.find_listener('97ada976-6444-42ae-a6c5-b182675e5f4b')
    print listener.status
    print listener.id

#get_listener(conn)

