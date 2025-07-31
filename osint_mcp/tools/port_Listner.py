import socket

def tcp_port_listener(port: int, host: str = '0.0.0.0', buffer_size: int = 1024) -> str:
    """
    Listens on a TCP port for one incoming connection and returns the received data.

    Parameters:
    - port (int): Port number to listen on.
    - host (str): IP address to bind to (default is '0.0.0.0').
    - buffer_size (int): Max size of the receiving buffer (default is 1024 bytes).

    Returns:
    - str: The data received from the client.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"[+] Listening on {host}:{port}...")
    client_socket, addr = server_socket.accept()
    print(f"[+] Connection from {addr}")

    data_received = b""

    while True:
        data = client_socket.recv(buffer_size)
        if not data:
            break
        data_received += data

    client_socket.close()
    server_socket.close()

    return data_received.decode(errors='ignore')
