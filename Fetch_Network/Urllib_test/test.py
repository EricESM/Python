import urllib2
import urllib

request = urllib2.Request("http://www.unr.edu")
response = urllib2.urlopen(request)
print response.read()