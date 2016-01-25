import commands
import sys
import copy

Server_Controller = ['openstack-ceilometer-alarm-evaluator.service','openstack-ceilometer-alarm-notifier.service','openstack-ceilometer-api.service','openstack-ceilometer-central.service','openstack-ceilometer-collector.service','openstack-ceilometer-notification.service']

Server_Compute= ['openstack-ceilometer-compute.service']

Server_command = sys.argv[1]
Server_Server = sys.argv[2]

def server_service(Server=None):
    if Server_command == 'status':
        for i in Server:
            Status=commands.getoutput("systemctl -a|grep %s" % i )
	    print Status
    elif Server_command == 'start':
	for i in Server:
	    commands.getoutput("systemctl start %s" % i)
    elif Server_command == 'stop':
	for i in Server:
	    commands.getoutput("systemctl stop %s" % i)
    elif Server_command == 'restart':
	for i in Server:
            commands.getoutput("systemctl restart %s" % i) 
    elif Server_command == 'detail':
	for i in Server:
            detail = commands.getoutput("systemctl status %s" % i)
	    print detail 

def server_controller():
    Server = copy.copy(Server_Controller) 
    server_service(Server)

def server_compute():
    Server = copy.copy(Server_Compute) 
    server_service(Server)


def main():
    if Server_Server == 'controller':
        server_controller()
    elif Server_Server == 'compute':
        server_compute()

main()
