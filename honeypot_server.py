import socket
from datetime import datetime

# Step 1: Create a socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Step 2: Bind to all interfaces on port 2222 (SSH honeypot)
server_socket.bind(('0.0.0.0', 2222))
server_socket.listen(5)

print("🚨 Honeypot SSH Server is running on port 2222...")

while True:
    client_socket, addr = server_socket.accept()
    ip = addr[0]
    print(f"[{datetime.now()}] Connection from {ip}")

    # Step 3: Fake login interaction
    client_socket.send(b"Username: ")
    username = client_socket.recv(1024).strip().decode()

    client_socket.send(b"Password: ")
    password = client_socket.recv(1024).strip().decode()

    # Step 4: Log to file
    with open("../logs/attack_logs.txt", "a") as log:
        log.write(f"{datetime.now()} - IP: {ip} - Username: {username} - Password: {password}\n")

    print(f"❌ Intrusion attempt from {ip} with username '{username}' and password '{password}'")

    client_socket.close()
