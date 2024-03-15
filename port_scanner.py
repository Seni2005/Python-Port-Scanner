import socket   #Import Python's socket library for network communication

#Function to scan ports on a given host
def scan_ports(target_host, start_port, end_port):
    print(f"\nScanning {target_host} from port {start_port} to {end_port}...\n")

    #Loop through each port in the given range
    for port in range(start_port, end_port + 1):
        #Create a new TCP socket for each port attempt
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  #Set a timeout (in seconds) for connection attempts

        try:
            # Try to connect to the target host on the current port
            s.connect((target_host, port))
            print(f"[+] Port {port} is OPEN")  #If connection succeeds, port is open
            s.close()  #Close the socket after use
        except:
            #If connection fails or times out, do nothing (port is closed/filtered)
            pass

#Entry point of the program
if __name__ == "__main__":
    #Get user input for target host and port range
    host = input("Enter target host (IP or domain): ")
    start = int(input("Enter start port: "))
    end = int(input("Enter end port: "))

    #Call the port scanning function
    scan_ports(host, start, end)
