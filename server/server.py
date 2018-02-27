import socket
import threading
import random, string
import time


class ClientStreamingThread(threading.Thread):

    def __init__(self, client_address, client_socket):
        threading.Thread.__init__(self)
        self.csocket = client_socket
        print("New connection added: ", client_address)

    def run(self):

        print("Connection from : ", client_address)

        # self.csocket.send(bytes("Hi, This is from Server..", 'utf-8'))

        message_to_send = bytes("%06d-%s\n" % (cpu_pause_ms, RANDOM_1_MB[:(message_bytes - 8)]), 'UTF-8')
        # TODO: don't send the exact same string each time (incase Spark caches it)

        last_unix_time = 0
        message_count_this_second = 0

        while True:
            # data = self.csocket.recv(2048)
            # msg = data.decode()
            # if msg == 'bye':
            #     break
            # print("from client", msg)

            unix_time_now = time.time()

            if int(unix_time_now) != last_unix_time:
                last_unix_time = int(unix_time_now)
                message_count_this_second = 0

            if message_count_this_second < message_count_per_second:
                self.csocket.send(message_to_send)
                message_count_this_second = message_count_this_second + 1
            else:
                time.sleep(((last_unix_time + 1) - unix_time_now)/10)

        print("Client at ", client_address, " disconnected...")


ALL_HOSTS = "127.0.0.1"
STREAM_PORT = 9999
CONTROL_PORT = 8889

MAX_MESSAGE_BYTES = 100 * 1000 ^ 2
RANDOM_1_MB = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)
                      for _ in range(MAX_MESSAGE_BYTES))

# Experiment Parameters.
cpu_pause_ms = 20
message_bytes = 200
message_count_per_second = 2

if __name__ == '__main__':
    stream_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    stream_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    stream_server.bind((ALL_HOSTS, STREAM_PORT))

    print("Server started")
    print("Waiting for client request..")

    # Worker thread for this:
    while True:
        stream_server.listen(1)
        client_socket, client_address = stream_server.accept()
        new_thread = ClientStreamingThread(client_address, client_socket)
        new_thread.start()

    # TODO: another thread to listen for connections on the control socket


