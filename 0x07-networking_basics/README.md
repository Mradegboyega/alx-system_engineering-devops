# Networking Bash Scripts

This project contains Bash scripts related to networking concepts, including the OSI model, network types, MAC and IP addresses, TCP and UDP, and more.

## Table of Contents

1. [OSI model](#osi-model)
2. [Types of Network](#types-of-network)
3. [MAC and IP Address](#mac-and-ip-address)
4. [TCP and UDP Ports](#tcp-and-udp-ports)
5. [Is the Host on the Network](#is-the-host-on-the-network)

## OSI Model

The OSI (Open Systems Interconnection) model is an abstract model that describes layered communication and computer network design. This project focuses on the Transport layer (TCP/UDP) and the Network layer (IP and ICMP).

## Types of Network

This section covers Local Area Networks (LANs), Wide Area Networks (WANs), and Internet connections.

## MAC and IP Address

Learn about MAC addresses and IP addresses, essential components of network communication.

## TCP and UDP Ports

Understand the concept of TCP and UDP ports and their significance in networking.

### Usage

Run the script `4-TCP_and_UDP_ports` to display listening ports along with PID and program names.

```bash
sudo ./4-TCP_and_UDP_ports

Is the Host on the Network

Use the Bash script 5-is_the_host_on_the_network to ping an IP address and check if a host is available on the network.

./5-is_the_host_on_the_network {IP_ADDRESS}
