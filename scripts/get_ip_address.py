import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print(f'IP Address: {ip}')
