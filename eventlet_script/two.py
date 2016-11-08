import eventlet
from eventlet.green import urllib2

urls = [
    "http://www.baidu.com",
    "http://www.sina.com",
    "http://www.youdao.com",
]

def fetch(url):
    print "Opening", url
    body = urllib2.urlopen(url).read()
    print "done with", url
    return url, body

pool = eventlet.GreenPool(200)
for url, body in pool.imap(fetch, urls):
    print "got body from", url, "of length", len(body)
