# Network Security Lab

## Overview
This project is part of the SEED Labs and focuses on understanding and implementing various network security concepts using packet sniffing, spoofing, and network diagnostics with Scapy and Wireshark.

Lab completed in 2022 Spring.

## Tasks and Learnings

### 1. Sniffing Packets
- **Objective:** Capture and analyze network packets to understand traffic and protocols.
- **Key Learnings:**
  - **Mechanism:** Using Scapy to sniff packets and apply filters for specific packet types.
  - **Privileges:** Root privileges are required for full access to network interfaces.
- **Execution:**
  - Sniffed ICMP packets and demonstrated the need for root privileges.
  - Captured specific packets like TCP from a particular IP and subnet traffic using filters.

### 2. Spoofing ICMP Packets
- **Objective:** Spoof ICMP echo request packets and observe responses.
- **Key Learnings:**
  - **Mechanism:** Crafting and sending custom ICMP packets with Scapy.
  - **Impact:** Understanding how spoofed packets can affect network communications.
- **Execution:**
  - Sent spoofed ICMP requests and used Wireshark to verify responses.

### 3. TCP Traceroute
- **Objective:** Implement a custom TCP traceroute to diagnose network paths.
- **Key Learnings:**
  - **Mechanism:** Manually sending TCP packets to trace the route to a destination.
  - **Path Discovery:** Identifying the hops packets take to reach the target IP.
- **Execution:**
  - Developed a script to perform TCP traceroute and validated the path using Wireshark.

### 4. Sniffing and Then Spoofing
- **Objective:** Combine sniffing and spoofing to manipulate network traffic.
- **Key Learnings:**
  - **Mechanism:** Sniffing packets and then spoofing responses based on captured data.
  - **Practical Application:** Handling specific scenarios like unreachable IPs and valid addresses.
- **Execution:**
  - Created a program to sniff and spoof packets.
  - Tested with different IPs to demonstrate successful and unsuccessful spoofing attempts.

## Additional Notes
- **Tools Used:** Python, Scapy for packet manipulation, Wireshark for traffic analysis, and Linux commands for script execution.
- **Challenges:** Managing root privileges for certain operations and understanding the limitations of spoofed packets.

## Conclusion
This lab provides hands-on experience with network security techniques, including packet sniffing, spoofing, and network diagnostics. It highlights the importance of understanding network vulnerabilities and implementing proper security measures to mitigate potential attacks.

## Usage
To replicate the tasks:
1. Set up the environment and ensure Scapy and Wireshark are installed.
2. Follow the instructions in each task to perform the activities.
3. Use Wireshark to monitor and verify network traffic for each task.

For detailed instructions, refer to the lab documentation linked [here](https://seedsecuritylabs.org/Labs_20.04/Files/Packet_Sniffing_Spoofing/Packet_Sniffing_Spoofing.pdf).

---

Feel free to clone this repository and explore the provided scripts to gain a deeper understanding of network security concepts and techniques.
