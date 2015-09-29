#!/usr/bin/env python
import sys,os,subprocess,commands
#Display Network card message

def Display():
    #This is display NetWork info
    info = commands.getoutput("ip a")
    print info

#start Init Network
def Init():
    #disable NetworkManager service
    os.system('chkconfig NetworkManager off')
    #stop NetworkManager service
    os.system('service NetworkManager stop')
    #enable network service
    os.system('chkconfig network on')
    return os.system('service NetworkManager status')

#use file write start write network file
def Config(nic,mac,ip,netmask,gateway,dns):
    global name
    global FileDir
    global File
    name = "ifcfg-" + nic
    FileDir = "/etc/sysconfig/network-scripts"
    File = FileDir + "/" + name
    #print File
    if name in os.listdir("%s" % (FileDir)):
        os.rename("%s" % (File),"%s.%s" % (File,'bak'))
        with open(File,'a') as f:
            f.write("%s=%s\n" % ('TYPE','Ethernet'))
            f.write("%s=%s\n" % ('BOOTPROTO','static'))
            f.write("%s=%s\n" % ('DEVICE',nic))
            f.write("%s=%s\n" % ('ONBOOT','yes'))
            f.write("%s=%s\n" % ('HWADDR',mac))
            f.write("%s=%s\n" % ('IPADDR',ip))
            f.write("%s=%s\n" % ('NETMASK',netmask))
            f.write("%s=%s\n" % ('GATEWAY',gateway))
            f.write("%s=%s\n" % ('DNS1',dns))

#display network configure message    
def Netinfo():
    f = open('%s' % File)
    for line in f.readlines():
        print line

#Last Use Restart Network
def Done():
    print "Restart Network"
    os.system('service network restart')
    print "The Network configure Finsh"
    return os.system('service network status')
#    sys.exit()
#use While start all configure
while True:
    print '''Thie is configure network info message
            1) Display Network Name
            2) Start Init Network
            3) Start Configure Network
            4) Display Network Configure
            5) Restart Network 
            6) Exit
            '''
    Select = raw_input("Plese Select:")
    if Select == '1':
        Display()
        continue
    elif Select == '2':
        Init()
        continue
    elif Select == '3':

	#config message
	NIC = raw_input("Please input your Network Name (example eth0): ")
	#MAC = os.popen("ip a | grep ether|awk '{ print $2}'").readlines()
	MAC = commands.getoutput("ip link show " +NIC+ "| grep ether|awk '{ print $2}'")
	print MAC
	IP = raw_input("Please input your IP address(example: 172.16.1.10): ")
	NETMASK = raw_input("Please input your Netmask(example: 255.255.255.0): ")
	GATEWAY = raw_input("Please input your Gateway(example: 172.16.1.1): ")
	DNS = raw_input("Plese input your DNS(example: 8.8.8.8): ")
        Config(NIC,MAC,IP,NETMASK,GATEWAY,DNS)
        continue
    elif Select == '4':
        Netinfo()
        continue
    elif Select == '5':
        Done()
        continue
    elif Select == '6':
        break
    elif len(Select) == 0:
	continue
    else:
	print "You Select Error,You Will exit"
	break
