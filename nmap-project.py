import nmap

class NmapScanner:
    def __init__(self, target):
        self.target = target

    def scan_ports(self):
        with nmap.PortScanner() as scanner:
            scanner.scan(self.target, '1-1000')

            for host in scanner.all_hosts():
                print(f"Open ports for {host}:")
                for port in scanner[host].all_tcp():
                    print(f"Host: {host}    Port: {port}")

def main():
    target = input("Enter the target IP address: ")
    scanner = NmapScanner(target)
    scanner.scan_ports()

if __name__ == '__main__':
    main()