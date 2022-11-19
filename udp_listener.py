from threading import Thread
from misc.udp_cli import read_socket

def fetch_traffic(q, UDPClientSocket):
    prev_msg = ''
    while True:
        # Fetch the string
        msg = read_socket(UDPClientSocket[0])

        # Decode the string
        d_msg = msg.decode()
        
        # If last item added is equivalent to current item, don't add to queue
        # Add string to Queue
        
        if d_msg != prev_msg:
            print(d_msg)
            #q.put(d_msg)
            prev_msg = d_msg


def run_listener_thread(q, UDPClientSocket):
    # creating thread
    t1 = Thread(target=fetch_traffic, args=([q], [UDPClientSocket]))
    #starts the thread
    t1.daemon = True
    t1.start()
