from scapy.all import *

# Create an ICMP packet
packet = IP(dst="www.google.com") / ICMP()

# Send the packet and receive a response
response = sr1(packet, timeout=2, verbose=False)

# Check if a response was received
if response:
    print(f"Received response from {response.src}")
else:
    print("No response received")