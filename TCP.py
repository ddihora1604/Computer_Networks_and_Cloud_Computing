#TCP CLIENT

import socket 

PORT = 8080

def start_TCP_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client_socket.connect(('localhost', PORT))
    print(f"Connected to server at port : {PORT}")
    
    message = "Hello from Client"
    client_socket.send(message.encode())
    print(f"Message sent from client --> server")
    
    server_response = client_socket.recv(1024)
    print(f'Server response : {server_response.decode()}')
    
    client_socket.close()
    
if __name__ == '__main__':
    start_TCP_client()


#TCP SERVER

import socket 

PORT = 8080
# AF_INET : Ensures that local host is a IPv4 address (indicates that socket will be using IPv4 addrssing)
# SOCK_STREAM : Ensures that data is read and accepted as a continuos stream by the server 

def start_TCP_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    
    server_socket.bind(('localhost', PORT))
    
    server_socket.listen(1)
    print(f'Server listening on port {PORT} for incoming connections')
    
    conn, addr = server_socket.accept()
    print(f'Connection established with {addr}')
    
    received_data = conn.recv(1024)
    print(f'Server received data from client : {received_data.decode()}')
    
    response = "Hello from SERVER"
    conn.send(response.encode())
    print('Response sent from server --> client') 
    
    conn.close()
    server_socket.close() 

if __name__ == '__main__':
    start_TCP_server()