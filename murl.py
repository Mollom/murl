import oauth2 as oauth
from optparse import OptionParser

usage = "usage: %prog [options] endpoint"
parser = OptionParser(usage)
parser.add_option("-k", "--consumer_key",
                    action="store", dest="consumer_key",
                    help="Consumer key for two legged OAuth")
parser.add_option("-s", "--consumer_secret",
                    action="store", dest="consumer_secret",
                    help="Consumer secret for two legged OAuth")

parser.add_option("-H", "--hostname",
                    action="store", dest="hostname", default="http://rest.mollom.com",
                    help="Hostname")

parser.add_option("-p", "--post",
                    action="store_true", dest="post", default=False,
                    help="POST instead of GET")

(options, args) = parser.parse_args()
if len(args) != 1:
    parser.error("incorrect number of arguments")

request_url = args[0]

consumer = oauth.Consumer(options.consumer_key, options.consumer_secret)
client = oauth.Client(consumer)

if options.post:
    resp, content = client.request(options.hostname + request_url, "POST")
else:
    resp, content = client.request(options.hostname + request_url)

print content

