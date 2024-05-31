import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # For UDP

client_ip = "127.0.0.1"

while True:
    modifiedMessage, serverAddress = client_socket.recvform(2048) #receive the modified message from the server
    print('Modified message: ', modifiedMessage.decode()) #print thw modified message
    client_socket.close() #close the socket

    