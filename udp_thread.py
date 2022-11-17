import threading
from misc.udp_cli import read_socket

def fetch_traffic(q):
    #while True:
    #we want this infinite (while program is running)
    # Fetch the string
    msg = read_socket()

    # Decode the string
    #d_msg = msg.decode('utf-8')
    
    # If last item added is equivalent to current item, don't add to queue
    # Add string to Queue
    print(msg.decode())
    #q.put(d_msg)
        


def create_thread(q):
    # creating thread
    t1 = threading.Thread(target=fetch_traffic, args=(q,))
    #starts the thread
    t1.start()
    #waits until thread has finished execution
    #t1.join()