import socket


def read_socket():
	msgFromServer = UDPClientSocket.recvfrom(bufferSize) 
	msg = msgFromServer[0]

	msg = "Message from Server {}".format(msgFromServer[0])
	print(msg)
	
	return msg

	
if __name__ == '__main__':
	msgFromClient       = "Hello UDP Server"
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = ("127.0.0.1", 7500)
	bufferSize          = 1024

	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	# Send to server using created UDP socket
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)