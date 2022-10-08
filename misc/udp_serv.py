import socket

 

localIP     = "127.0.0.1"
localPort   = 7500
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

 

# Create a datagram socket

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

 

# Bind to address and ip

s.bind((localIP, localPort))

print("UDP server up and listening")

 

# Listen for incoming datagrams

while(True):

    bytesAddressPair = s.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client:{}".format(message)
    clientIP  = "Client IP Address:{}".format(address)
    
    #print(clientMsg)
    #print(clientIP)
    print(message)

   

    # Sending a reply to client

    s.sendto(bytesToSend, address)