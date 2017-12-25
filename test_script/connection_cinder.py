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




def get_volume(conn):
    print "get volume"
    res = conn.block_store.get_volume('de3160b4-637f-4f14-98e2-65b83e9327ca')
    print 'volume id is: %s' % res.id
    print 'volume status is: %s' % res.status
    if 'available' == res.status:
        print 'ok'
    print res.is_bootable
    print res.volume_image_metadata
    print "image is is: %s" % res.volume_image_metadata['image_id']

get_volume(conn)


def create_volume(conn):
    print "create volume"
    kwargs = {
        'name': 'fabian1',
        'size': '2',
    }
    res = conn.block_store.create_volume(**kwargs)
    print res
    return res.id

#volume_id = create_volume(conn)

def create_volume_attach(conn):
    print "create volume attach"
    server = '8d34d5fa-5fd6-4724-8d07-e4b530951f21'
    kwargs = {
        'device': '/dev/vdb',
        'serverId': server,
        'volumeId': '28dce804-72fd-48d1-9611-4cbb534b3c18',
    }
    res = conn.compute.create_volume_attachment(server, **kwargs)
    print res

#create_volume_attach(conn)


def delete_volume(conn):
    print 'delete volume'
    volume_id = 'c5f75dbc-65c3-49a2-98fc-ca7d539ebe67'
    ignore_missing=True
    res = conn.block_store.delete_volume(volume_id, ignore_missing=ignore_missing)

#delete_volume(conn)

def delete_volume_detach(conn):
    print 'delete volume detach'
    volume_id = '28dce804-72fd-48d1-9611-4cbb534b3c18'
    server_id = '8d34d5fa-5fd6-4724-8d07-e4b530951f21'
    ignore_missing=True
    res = conn.compute.delete_volume_attachment(volume_id, server_id, ignore_missing=ignore_missing)
    print res

#delete_volume_detach(conn)
