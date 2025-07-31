# Port Scanner Script
# This script scans a range of ports on a specified host and reports which ports are open.
# It also measures and displays the time taken for the scan in both seconds and minutes.
# Author: Mevin Moncy

# ----------------------------- Imports -----------------------------

import socket  # For network communication
import time    # For measuring execution time

# ------------------------ Port Scanning Function ------------------------

def scan_ports(host, start_port, end_port):
    """
    Scans a range of TCP ports on the specified host.
    
    Parameters:
        host (str): The target IP address or hostname
        start_port (int): The starting port number
        end_port (int): The ending port number
    """

    print(f"Scanning {host} from port {start_port} to {end_port}...")
    start_time = time.time()  # Record the start time of the scan
    open_ports = []           # List to store open ports

    # Iterate over the specified port range
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket
        sock.settimeout(0.5)  # Set timeout to avoid hanging on closed ports

        result = sock.connect_ex((host, port))  # Try connecting to the port
        if result == 0:
            print(f"[+] Port {port} is open")
            open_ports.append(port)  # Add to list if the port is open

        sock.close()  # Close the socket

    end_time = time.time()  # Record the end time of the scan

    # Calculate and display duration
    total_seconds = end_time - start_time
    minutes = int(total_seconds // 60)
    seconds = total_seconds % 60

    # Display results
    if not open_ports:
        print("No open ports found.")
    else:
        print(f"Open ports: {open_ports}")
    
    print(f"Scanning done for {host}.")
    print(f"Time taken: {total_seconds:.2f} seconds")
    print(f"Time taken: {minutes} minutes and {seconds:.2f} seconds")

# ------------------------- Script Entry Point -------------------------

if __name__ == "__main__":
    # Prompt the user for a target IP or hostname
    target_host = input("Enter target IP or hostname: ")
    
    # Perform the scan from port 1 to 1024
    scan_ports(target_host, 1, 1024)
# End of script
# ----------------------------- End of main.py -----------------------------    