import eventlet
from eventlet.green import urllib2

urls = ["http://www.baidu.com",
        "http://www.sina.com",
        "http://www.youdao.com"]

def fetch(url):
    return urllib2.urlopen(url).read()

pool = eventlet.GreenPool()
for body in pool.imap(fetch, urls):
    print ("got body", len(body))
