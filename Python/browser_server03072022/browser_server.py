import socket
import multiprocessing


class StaticWebServer(object):
    def __init__(self, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        self.server.bind(('', port))
        self.server.listen(128)

    def start(self):
        while True:
            client, ip_port = self.server.accept()
            print(f'Client address info:{ip_port[0]}:{ip_port[1]}')
            p = multiprocessing.Process(target=self.task, args=(client,))
            p.start()
        server.close()

    def task(self, client):
        request_data = client.recv(1024).decode('utf-8')
        if len(request_data) == 0:
            client.close()
        else:
            request_path = request_data.split(' ')[1]
            print(f'Request path: {request_path}')
            if request_path == '/':
                request_path = '/index.html'

            try:
                with open('static' + request_path, 'rb') as file:
                    file_content = file.read()
            except Exception as e:
                response_line = 'HTTP/1.1 404 NOT FOUND\r\n'
                response_head = 'Server: PSWS1.1\r\n'
                with open('static/error.html', 'rb') as f:
                    error_data = f.read()
                response_data = (response_line + response_head + '\r\n').encode('utf-8') + error_data
                client.send(response_data)
            else:
                response_line = 'HTTP/1.1 200 OK\r\n'
                response_head = 'Server: PSWS1.1\r\n'
                response_data = (response_line + response_head + '\r\n').encode('utf-8') + file_content
                client.send(response_data)
            finally:
                client.close()


if __name__ == '__main__':
    StaticWebServer(80).start()
