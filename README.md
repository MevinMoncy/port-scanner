# Port Scanner

A simple Python-based **TCP port scanner** that checks for open ports on a specified IP address or hostname.  
This tool is built using only Python’s built-in libraries, making it lightweight and easy to understand for anyone learning network programming or ethical hacking.

---

## 🎯 Why I Built This Project

I built this project as a hands-on way to:
- Learn how **network sockets** work in Python
- Understand the fundamentals of **TCP communication**
- Explore how port scanning tools like Nmap operate under the hood
- Practice building a real-world tool using **basic programming constructs**

---

## 💡 What I Learned

- How to use Python’s `socket` module to create TCP connections
- How to implement **port scanning** logic
- How to calculate and display **execution time**
- Why scanning responsibly and legally is critical in cybersecurity

---

## 🚀 Features

- Scans a specified range of **TCP ports**
- Detects and prints all **open ports**
- Displays **total time taken** in seconds and in minutes + seconds
- Uses a **simple and readable structure** with no external dependencies

---

## 📌 Why This Project Is Useful

- Helps new developers understand how **networks and ports** work
- Serves as a lightweight alternative to more complex tools like Nmap

---

## 🧰 Requirements

- Python 3.x
- No third-party libraries required

---

## 📦 How to Use

1. **Clone this repository**:

    ```bash
    git clone https://github.com/yourusername/port-scanner.git
    cd port-scanner
    ```

2. **Run the script**:

    ```bash
    python main.py
    ```

3. **Input the target IP or hostname when prompted**:

    ```text
    Enter target IP or hostname: 192.168.1.254
    ```

---

## 🖼️ Example Output

This example shows the output when scanning `127.0.0.1`, which is the loopback IP address for the local machine (also known as *localhost*). This means the port scan was run on the same computer where the script was executed.

<p align="center">
  <img src="images/screenshot.png" alt="Port Scanner Output" width="700">
</p>

### 🔍 Interpreting the Output

The scan revealed that the following ports were open:

- **Port 135**  
  This port is commonly used by Microsoft RPC (Remote Procedure Call) services. It is critical for DCOM (Distributed Component Object Model) communication and is often open by default on Windows systems to support internal processes.

- **Port 445**  
  This port is used for Microsoft SMB (Server Message Block) protocol. It supports file sharing, printer sharing, and various remote Windows operations. An open port 445 indicates that SMB services are available on the scanned machine.

These results confirm that the port scanner can successfully identify open TCP ports and detect common services running on the local host.


---

## ⚠️ Legal and Ethical Warning

> This tool is meant for **educational purposes** and **authorized testing only**.  
> Scanning networks or devices **without permission** is **illegal and unethical**.  
> Always obtain **explicit authorization** before running port scans on systems you do not own.

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---

## 📬 Contributions

Pull requests and suggestions are welcome.  
