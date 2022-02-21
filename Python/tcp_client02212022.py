"""
    TCP Client
"""
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(('192.168.2.23', 6666))

while True:
    send_data = input('You:')
    if send_data != 'quit':
        send_data = send_data.encode('utf-8')
        client_socket.send(send_data)
    else:
        print('You have been disconnected from the server!')
        break

    recv_data = client_socket.recv(1024)
    if len(recv_data) != 0:
        recv_data = recv_data.decode('utf-8')
        print(f'Server: {recv_data}')
    else:
        print('You have been disconnected from the server!')
        break

client_socket.close()
