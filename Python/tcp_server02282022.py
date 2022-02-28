"""
TCP Server
"""
import socket
import threading


def client_task(client_socket, ip_port):
    print(f'The client,{ip_port},has successfully established a connection with the server!')
    while True:
        recv_data = client_socket.recv(1024).decode('utf-8')
        if len(recv_data) != 0:
            print(f'Message from the client {ip_port}: {recv_data}')
        else:
            print(f'The client {ip_port} is offline!')
            break
        send_data = input('Server：').encode('utf-8')
        client_socket.send(send_data)


if __name__ == '__main__':
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    server_socket.bind(('', 6666))
    server_socket.listen(128)
    while True:
        client_socket, ip_port = server_socket.accept()
        t_client = threading.Thread(target=client_task, args=(client_socket, ip_port))
        t_client.daemon = True
        t_client.start()

