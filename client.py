import socket
import threading

def handle_receive(client):
    print("CLIENT : ")
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg:
                print("Server disconnected.")
                break
            print(f"\rSERVER: {msg}\nCLIENT: ", end="")
        except:
            print("Connection closed.")
            break
    client.close()

def handle_send(client):
    while True:
        msg = input("")
        if msg.lower() == "exit":
            client.close()
            break
        client.send(msg.encode())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8000))

# start 2 threads
recv_thread = threading.Thread(target=handle_receive, args=(client,))
send_thread = threading.Thread(target=handle_send, args=(client,))
recv_thread.start()
send_thread.start()
