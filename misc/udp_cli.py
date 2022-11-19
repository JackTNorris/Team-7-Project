import socket


def read_socket(UDPClientSocket):
	bufferSize = 1024
	print("before cli recv")
	msgFromServer = UDPClientSocket.recvfrom(bufferSize)
	print("after cli recv")
	msg = msgFromServer[0]
	return msg

	
def run_cli():
	msgFromClient       = "Hello UDP Server"
	bytesToSend         = str.encode(msgFromClient)
	serverAddressPort   = ("127.0.0.1", 7500)


	# Create a UDP socket at client side
	UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

	# Send to server using created UDP socket
	UDPClientSocket.sendto(bytesToSend, serverAddressPort)
	return UDPClientSocket