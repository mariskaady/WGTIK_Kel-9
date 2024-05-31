from socket import * # Mengimport library socket
import threading # Mengimport library threading bisa menangani 2 proses

def threading_socket(connectionSocket):
    """Membuat thread baru untuk setiap koneksi"""
    try:
        message = connectionSocket.recv(1024).decode() # Menerima data dari client
        status = "HTTP/1.1 200 OK\n" # Status OK untuk response 
        header = "Content-Type: text/html\r\n\r\n" # Membuat header untuk response
        message = message_request(message) # Memproses request dari client
        response = status+header+message # Membuat response
        connectionSocket.send(response.encode()) # Mengirim response ke client
    except IOError:
        connectionSocket.send("Server is Down".encode()) # Menghandle ketika file tidak ditemukan 

def message_request(request):
    """Memproses request dari client"""
    header = request.split("\r\n\r\n")[0] # Mengambil header dari request 
    path = header.split()[1] # Mengambil path dari header

    ## Membuat response berdasarkan path atau query ##
    if path == "/" or path == "/index.html":
        file = open("./index.html", "r") # Membuka file index.html jika pathnya sesuai
        message = file.read()
    elif path == "/about.html":
        file = open("./about.html", "r")
        message = file.read()
    else:
        file = open("./404.html", "r")
        message = file.read()
    file.close()

    return message

"""Membuat server socket"""
serverPort = 8016 # Port yang digunakan
serverAddr = "localhost" # Server Lokal Host
serverSocket = socket(AF_INET, SOCK_STREAM) # Membuat Socket TCP
serverSocket.bind((serverAddr, serverPort)) # Menghubungkan Socket dengan Port
serverSocket.listen(1) # Server dapat menerima koneksi dari client

print('Ready to serve ...')

while True:
    connectionSocket, addr = serverSocket.accept() # Menerima koneksi dari client
    threading.Thread(target=threading_socket, args=(connectionSocket,)).start() # Membuatthread baru untuk setiap koneksi

serverSocket.close() # Menutup server socket    