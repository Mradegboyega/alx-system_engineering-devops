# Firewall Configuration and Port Forwarding with UFW

This README outlines the necessary steps to configure the UFW (Uncomplicated Firewall) to manage network traffic on a Linux server, specifically for allowing access to common web ports and forwarding traffic from port 8080 to port 80.

## Overview

This setup includes:
- Installing UFW.
- Basic UFW configuration to allow certain ports.
- Advanced UFW configuration for port forwarding.
- Testing the configuration.

## Prerequisites

- A Linux server (Debian/Ubuntu is assumed for package management).
- Root or sudo access on the server.

## Installation

First, ensure that UFW is installed on your system:

```bash
sudo apt-get update
sudo apt-get install ufw

