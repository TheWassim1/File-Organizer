import socket

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECTmsg = "disconnect"

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    # Convert length to string, encode it, and pad to HEADER
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))  # pad with spaces
    client.send(send_length)  # send the length first
    client.send(message)      # then send the actual message
msg=str(input("Give the message you want to send! \n"))
send(msg)
send()

