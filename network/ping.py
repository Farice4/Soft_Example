import commands
ip = '10.10.10.'
server = []

for i in range(90,120):
    ips = ip + str(i)
    s = commands.getoutput('ping %s -c 3' % ips)
    if 'error' in s:
        print '%s network error' % ips
    else:
        print '%s network good' % ips
