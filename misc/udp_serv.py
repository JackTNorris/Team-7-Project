import socket
from threading import Thread


def start_server():
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

        bytesToSend = bytesAddressPair[0]
        address = bytesAddressPair[1]
        
        # Sending a reply to client
        s.sendto(bytesToSend, address)


def run_serv_thread():
    # creating thread
    serv_thread = Thread(target=start_server)
    #starts the thread
    serv_thread.daemon = True
    serv_thread.start()
