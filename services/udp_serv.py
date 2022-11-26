import socket
from threading import Thread


def fetch_traffic(q, sock):
    bufferSize  = 1024
    q = q[0]
    sock = sock[0]

    # Listen for incoming datagrams
    while(True):
        # Receive traffic from socket
        bytesAddressPair = sock.recvfrom(bufferSize)

        # Parse the packet
        bytesToSend = bytesAddressPair[0]
        address = bytesAddressPair[1]

        # Decode the message
        d_msg = bytesToSend.decode()
        
        # Update the queue with the message
        q.put(d_msg)

        # Sending a reply to client
        sock.sendto(bytesToSend, address)


def start_server():
    localIP     = "127.0.0.1"
    localPort   = 7500

    # Create a datagram socket
    sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    # Bind to address and ip
    sock.bind((localIP, localPort))

    return sock


def run_udp_thread(q, sock):
    # Create the thread
    udp_thread = Thread(target=fetch_traffic, args=([q], [sock]))
    
    # Start the thread and set as daemon (kills the thread once main thread ends)
    udp_thread.daemon = True
    udp_thread.start()
