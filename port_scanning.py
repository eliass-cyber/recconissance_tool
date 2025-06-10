import socket
import time
import sys
from concurrent.futures import ThreadPoolExecutor

open_ports = []

def load_ports(ports):
    with open('nmap-top-ports.txt','r') as f:
        for line in f:
            p = int(line.strip())
            ports.append(p)
        return ports

def port_scan(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"[+] port {port} is open")
            open_ports.append(port)
    except KeyboardInterrupt:
        print("\n Exiting Program !!!!")
        sys.exit()
    except:
        return False

def run_scanner(ports, thread_count = 100):
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        for port in ports:
            executor.submit(port_scan, port)

def main():
    start = time.time()
    domain = input('Input host: ')
    global target_ip
    target_ip = socket.gethostbyname(domain)
    ports = []
    load_ports(ports)
    print('Starting scan on host:', target_ip)
    run_scanner(ports)
    end = time.time()
    print(f'time taken {end - start:.2f} seconds')
    print(f"Open ports found: {sorted(open_ports)}")

if __name__ == "__main__":
    main()
