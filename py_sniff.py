from scapy.all import sniff, Ether, IP, TCP, UDP, ICMP
import csv
import datetime

# Deliverable 2: Setup the CSV File and Headers
# Run before the sniffer starts to create the file and the top row
csv_filename = "pysniff_capture.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Source MAC", "Dest MAC", "Source IP", "Dest IP", "Protocol", "Summary"])

def parse_packet(packet):
    # Deliverable 1: Advanced Protocol Filtering
    # Check for Ether and IP layers first to avoid errors
    if packet.haslayer(Ether) and packet.haslayer(IP):
        src_mac = packet[Ether].src
        dst_mac = packet[Ether].dst
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        
        # Grab a timestamp for the CSV
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        protocol = None
        summary = ""

        # Instead of just mapping the number, we actively filter for specific layers
        if packet.haslayer(TCP):
            protocol = "TCP"
            summary = f"Port {packet[TCP].sport} -> {packet[TCP].dport}"
        elif packet.haslayer(UDP):
            protocol = "UDP"
            summary = f"Port {packet[UDP].sport} -> {packet[UDP].dport}"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
            summary = f"Type: {packet[ICMP].type}"
        
        # If the packet matched one of our three target protocols, process it
        if protocol:
            final_output = f"MAC: {src_mac:<17} -> {dst_mac:<17} | IP: {src_ip:<15} -> {dst_ip:<15} | Proto: {protocol:<4} | {summary}"
            
            # Print to console
            print(final_output)
            
            # Deliverable 2: CSV Export
            # try/except for permission errors
            try:
                with open(csv_filename, mode='a', newline='') as csv_file:
                    writer = csv.writer(csv_file)
                    # Writes the extracted data into neat columns
                    writer.writerow([timestamp, src_mac, dst_mac, src_ip, dst_ip, protocol, summary])
            except PermissionError:
                # This prevents a crash if you have the CSV open in Excel while the script is running
                print(f"[!] Error: Could not write to {csv_filename}. Is the file open in another program?")

def main():
    print("Starting Py-Sniff Capture Engine (Phase 3)...")
    print(f"Filtering for TCP, UDP, and ICMP. Writing data to {csv_filename}")
    print("Press Ctrl+C to stop the capture.")
    
    # store=False makes sure we don't run out of memory during long captures.
    sniff(prn=parse_packet, store=False)

if __name__ == "__main__":
    main()
