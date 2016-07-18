def http_pack(type,data):
	type = type
	header = '''HTTP/1.0 200 OK\r\n
				Date: Mon, 31 Dec 2016 04:25:57 GMT\r\n
				Server: Apache/2.5(Unix)\r\n
				Content-type: text/html\r\n
				Connection: keep-alive\r\n
				\r\n
				cmd = '''
	response = header +data
	return response

def http_parse(raw_request):
	data = raw_request.split('\r\n\r\n')
	return data[1]
