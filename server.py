import socket
import threading

def handle_receive(conn):
    print("Server : ")
    while True:
        try:
            msg = conn.recv(1024).decode()
            if not msg:
                print("Client disconnected.")
                break
            print(f"\rCLIENT: {msg}\nSERVER: ", end="")
        except:
            print("Connection closed.")
            break
    conn.close()

def handle_send(conn):
    while True:
        msg = input("")
        if msg.lower() == "exit":
            conn.close()
            break
        conn.send(msg.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8000))
server.listen(1)
print("Server listening...")

conn, addr = server.accept()
print("Connected to", addr)

# start 2 threads
recv_thread = threading.Thread(target=handle_receive, args=(conn,))
send_thread = threading.Thread(target=handle_send, args=(conn,))
recv_thread.start()
send_thread.start()
