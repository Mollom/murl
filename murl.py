import oauth2 as oauth
import httplib2, urllib
from optparse import OptionParser

class MyClient(oauth.Client):
	def __init__ (self, consumer):
		oauth.Client.__init__(self, consumer)

	def request(self, uri, method="GET", body='', headers=None, redirections=httplib2.DEFAULT_MAX_REDIRECTS, connection_type=None):
		if not isinstance(headers, dict):
			headers = {}

		# set the content type (text/plain for GET, )
		if (method == "POST"):
			DEFAULT_POST_CONTENT_TYPE = 'application/x-www-form-urlencoded'
		elif (method == "GET"):
			DEFAULT_POST_CONTENT_TYPE = 'text/plain'

		headers['Content-Type'] = headers.get('Content-Type', DEFAULT_POST_CONTENT_TYPE)

		is_form_encoded = headers.get('Content-Type') == 'application/x-www-form-urlencoded'

		if is_form_encoded and body:
			parameters = parse_qs(body)
		else:
			parameters = None

		req = oauth.Request.from_consumer_and_token(self.consumer, 
		token=self.token, http_method=method, http_url=uri, 
		parameters=parameters, body=body, is_form_encoded=is_form_encoded)

		req.sign_request(self.method, self.consumer, self.token)

		schema, rest = urllib.splittype(uri)
		if rest.startswith('//'):
			hierpart = '//'
		else:
			hierpart = ''
		host, rest = urllib.splithost(rest)

		realm = schema + ':' + hierpart + host

		headers.update(req.to_header(realm=realm))

		return httplib2.Http.request(self, uri, method=method, body=body, headers=headers, redirections=redirections, connection_type=connection_type)

def __call__ (consumer_key, consumer_secret, hostname, request_url, body='', http_action='GET'):
	consumer = oauth.Consumer(consumer_key, consumer_secret)
	client = MyClient(consumer)

	response, content = client.request(hostname + request_url, http_action, body=body, headers={'Content-Type' : 'text/plain'})
	return content

if __name__ == "__main__":
	usage = "usage: %prog [options] endpoint data"
	parser = OptionParser(usage)
	parser.add_option("-k", "--consumer_key",
		            action="store", dest="consumer_key",
		            help="Consumer key for two legged OAuth")
	parser.add_option("-s", "--consumer_secret",
		            action="store", dest="consumer_secret",
		            help="Consumer secret for two legged OAuth")

	parser.add_option("-H", "--hostname",
		            action="store", dest="hostname", default="http://xmlrpc2.mollom.com",
		            help="Hostname")

	parser.add_option("-p", "--post",
		            action="store_true", dest="post", default=False,
		            help="POST instead of GET")

	(options, args) = parser.parse_args()
	if len(args) > 2:
	    parser.error("incorrect number of arguments")

	body = ''
	if (len(args) == 2):
		body = args[1]

	request_url = args[0]
	if options.post:
		print __call__(options.consumer_key, options.consumer_secret, options.hostname, request_url, body, 'POST')
	else:
		print __call__(options.consumer_key, options.consumer_secret, options.hostname, request_url, body, 'GET')

