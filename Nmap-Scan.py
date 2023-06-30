import nmap

def scan_ports(target_hosts, target_ports, scan_type):
    # Create a new instance of the PortScanner object
    scanner = nmap.PortScanner()

    # Set the scan type
    scanner.scaninfo = {scan_type: '-T4'}

    # Scan the target hosts for the specified ports
    scan_results = scanner.scan(target_hosts, target_ports)

    # Iterate over the scan results and print open ports
    for host in scan_results['scan']:
        for protocol in scan_results['scan'][host]:
            if protocol == scan_type:
                ports = scan_results['scan'][host][protocol].keys()
                for port in ports:
                    state = scan_results['scan'][host][protocol][port]['state']
                    if state == 'open':
                        print(f"Port {port}/{protocol} is open on {host}")

    # Save the scan results to a file
    filename = 'scan_results.txt'
    with open(filename, 'w') as file:
        file.write(scanner.csv())

    print(f"\nScan results saved to {filename}")

# Rest of the code remains the same...


# Function to prompt for IP addresses, port range, and scan type
def prompt_scan():
    target_hosts = input("Enter the IP addresses to scan (separated by commas): ")
    target_ports = input("Enter the ports to scan (e.g., 1-1000): ")
    scan_type = input("Enter the scan type (tcp or udp): ")

    target_hosts = [host.strip() for host in target_hosts.split(",")]

    scan_ports(target_hosts, target_ports, scan_type)

# Prompt the user for input
prompt_scan()
