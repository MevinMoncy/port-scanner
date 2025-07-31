import socket
import time  # to measure execution time

def scan_ports(host, start_port, end_port):
    print(f"Scanning {host} from port {start_port} to {end_port}...")
    start_time = time.time()  # record start time
    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  # quick timeout for responsiveness

        result = sock.connect_ex((host, port))
        if result == 0:
            print(f"[+] Port {port} is open")
            open_ports.append(port)

        sock.close()

    end_time = time.time()  # record end time
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")
    
    print(f"Scanning done for {host}.")
    print(f"Time taken: {total_seconds:.2f} seconds")
    print(f"Time taken: {minutes} minutes and {seconds:.2f} seconds")

# Example usage
if __name__ == "__main__":
    target_host = input("Enter target IP or hostname: ")
    scan_ports(target_host, 1, 1024)
# This script scans a range of ports on a specified host and reports which ports are open.
# It also measures the time taken for the scan and prints it in both seconds and minutes.
