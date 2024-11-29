#UDP CLIENT

import socket 

PORT = 8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello from CLIENT"
client_socket.sendto(message.encode(), ('localhost', PORT))
print(f'Message sent to server from client : {message}')

try:
    response, server_addr = client_socket.recvfrom(1024)
    print(f'Response from server to client : {response.decode()}')
except Exception as e:
    print(f'An error occurred : {e}')
    
client_socket.close()


#UDP SERVER

import socket 

PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('localhost', PORT))
print(f'Server listening on port {PORT}')

while True:     # while the connection lasts 
    try:
        data, client_addr = server_socket.recvfrom(1024)
        print(f'Received from {client_addr} : {data.decode()}')
        
        response = "Hello from SERVER"
        server_socket.sendto(response.encode(), client_addr)
        print(f'Response sent from server to client at {client_addr} : {response}')
    except Exception as e:
        print(f'Error occurred : {e}')
    
