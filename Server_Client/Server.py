import socket
import threading

HEADER = 64
PORT =5050
FORMAT ="utf-8"
#get the server ipv4 address automatically
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER,PORT)
DISCONNECTmsg ="disconnect"
#Create a TCP IPv4 socket so it can send and recieve data over a network
server =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#attaching the socket to that IP and port
server.bind(ADDR)

def handle_client(conn , addr) :
    print(f"[NEW CONNECTION] {addr} connected.")
    connected =True
    while connected :
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg =conn.recv(msg_length).decode(FORMAT)      
            if msg ==DISCONNECTmsg:
                connected=False
            print(f"{addr} {msg}")
    conn.close()
def start():
    #start listening for incoming connections
    server.listen()
    print(f"Server is listening on {SERVER}")
    while True :
        #Creates a new socket (conn) for that client and gets the client address (addr)
        conn , addr =server.accept()
        thread =threading.Thread(target=handle_client , args=(conn ,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS]{threading.active_count()-1}")

print("Server is starting...")
start()
