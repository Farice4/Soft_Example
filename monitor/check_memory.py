#!/usr/bin/env Python
from collections import OrderedDict

def meminfo():
    ''' Return the information in /proc/meminfo
    as a dictionary '''
    limit = 55
    meminfo=OrderedDict()

    with open('/proc/meminfo') as f:
        for line in f:
            meminfo[line.split(':')[0]] = line.split(':')[1].strip()

    Total = int((meminfo['MemTotal']).strip('kB')) / 1024.0
    UseMemory = Total - (int((meminfo['MemFree']).strip('kB'))) / 1024.0 -(int((meminfo['Buffers']).strip('kB')))/1024.0 -(int((meminfo['Cached']).strip('kB'))) /1024.0
    print ('UseMemory is : %d' % UseMemory)
    print ('Total is : %d ') % Total
    avg = UseMemory / Total * 100
    if  avg > limit:
        print "Walling, %d %% " % avg
    else:
        print "The system is good: %d %%" % avg
     
    return meminfo

if __name__=='__main__':
    #print(meminfo())
    meminfo()
    
