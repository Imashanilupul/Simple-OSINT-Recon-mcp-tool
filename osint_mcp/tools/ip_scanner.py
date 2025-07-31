import socket



def scan_ip_ports(ip_address: str, start_port: int = 1, end_port: int = 1024) -> str:
    """
    Scan the given IP address for open ports in a user-defined range.
    Returns a string with open ports or a message if none are found.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((ip_address, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except:
            pass

    if open_ports:
        return "Open ports:\n" + "\n".join([f"Port {p} is open" for p in open_ports])
    else:
        return "No open ports found."

