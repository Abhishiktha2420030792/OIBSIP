# server.py
import socket
import threading
import datetime

HOST = "127.0.0.1"   # localhost
PORT = 5000          # change if busy

clients = {}  # conn -> username

def timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S")

def broadcast(msg, exclude=None):
    remove = []
    for conn in list(clients.keys()):
        if conn is exclude:
            continue
        try:
            conn.sendall(msg.encode("utf-8"))
        except Exception:
            remove.append(conn)
    for conn in remove:
        username = clients.pop(conn, "Unknown")
        try:
            conn.close()
        except:
            pass
        print(f"[{timestamp()}] Disconnected: {username}")

def handle_client(conn, addr):
    try:
        conn.sendall("Enter a username: ".encode("utf-8"))
        username = conn.recv(1024).decode("utf-8").strip()
        if not username:
            username = f"user_{addr[1]}"
        clients[conn] = username

        join_msg = f"[{timestamp()}] {username} joined the chat.\n"
        print(join_msg.strip())
        broadcast(join_msg, exclude=None)
        conn.sendall("Type /quit to exit.\n".encode("utf-8"))

        while True:
            data = conn.recv(4096)
            if not data:
                break
            text = data.decode("utf-8").rstrip("\n")
            if text == "/quit":
                break
            out = f"[{timestamp()}] {username}: {text}\n"
            print(out.strip())
            broadcast(out, exclude=None)
    except ConnectionResetError:
        pass
    finally:
        username = clients.pop(conn, "Unknown")
        leave_msg = f"[{timestamp()}] {username} left the chat.\n"
        print(leave_msg.strip())
        broadcast(leave_msg, exclude=None)
        try:
            conn.close()
        except:
            pass

def main():
    print(f"Starting server on {HOST}:{PORT} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print("Server ready. Waiting for clients...")
        while True:
            conn, addr = s.accept()
            threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
