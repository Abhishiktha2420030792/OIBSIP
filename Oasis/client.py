# client.py
import socket
import threading
import sys

HOST = "127.0.0.1"
PORT = 5000

def receive(sock):
    try:
        while True:
            data = sock.recv(4096)
            if not data:
                print("\n[Disconnected from server]")
                break
            print(data.decode("utf-8"), end="")
    except Exception as e:
        print(f"\n[Receive error] {e}")
    finally:
        try:
            sock.close()
        except:
            pass
        # end the process when receiver loop ends
        try:
            sys.exit(0)
        except SystemExit:
            pass

def main():
    print(f"Connecting to {HOST}:{PORT} ...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        threading.Thread(target=receive, args=(s,), daemon=True).start()

        # first prompt is username; then messages
        for line in sys.stdin:
            msg = line.rstrip("\n")
            s.sendall((msg + "\n").encode("utf-8"))
            if msg == "/quit":
                break

if __name__ == "__main__":
    main()
