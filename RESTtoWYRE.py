import urllib2, base64
import ssl
import pprint
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

username = 'radek01'
password = 'radek01!'
url = 'https://135.248.215.135:3001/users/4606c4f8-29b9-44c3-b578-dc511c571a3c/roster'
request = urllib2.Request(url)

# You need the replace to handle encodestring adding a trailing newline 
# (https://docs.python.org/2/library/base64.html#base64.encodestring)
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   
result = urllib2.urlopen(request, context=ctx)
response = result.readline()
json_s = json.loads(response)

pprint.pprint(json_s)


