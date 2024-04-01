Project Title
Overview

This project aims to automate the configuration of web servers and a load balancer to distribute traffic evenly across multiple servers. Additionally, it involves automating the setup of a custom HTTP response header using both Bash scripts and Puppet.
Requirements

    Ubuntu 16.04 LTS
    Nginx web server
    HAProxy load balancer
    Puppet
    Shellcheck 0.3.7 for linting Bash scripts
    Curl for testing

Tasks
Task 0: Double the Number of Webservers

Objective: Configure web-02 to be identical to web-01 and add a custom Nginx response header to identify which web server is responding.
Implementation Details

    Bash script to automate Nginx installation and configuration.
    Custom HTTP header named X-Served-By with the server's hostname as its value.

Task 1: Install Your Load Balancer

Objective: Install and configure HAProxy on lb-01 to distribute traffic to web-01 and web-02 using a round-robin algorithm.
Implementation Details

    Bash script for HAProxy installation and setup.
    Configuration to ensure traffic distribution is managed via a round-robin algorithm.

Task 2: Add a Custom HTTP Header with Puppet

Objective: Automate the task of creating a custom HTTP header response with Puppet.
Implementation Details

    Puppet manifest to ensure Nginx is installed and running.
    Nginx configuration to include a custom HTTP header X-Served-By with the server's hostname.

Getting Started

To get a local copy up and running follow these simple steps.
Prerequisites

    Ensure you have Ubuntu 16.04 LTS running.
    Install curl, nginx, haproxy, and puppet on your machine.

Installation

    Clone the repository to your local machine.
    Make the Bash scripts executable:

    sh

chmod +x *.sh

Run the Bash scripts to configure the web servers and the load balancer:

sh

./0-custom_http_response_header.sh
./1-install_load_balancer.sh

Apply the Puppet manifest to configure the custom HTTP header:

sh

    sudo puppet apply 2-puppet_custom_http_response_header.pp

Usage

    Use curl to verify the custom HTTP header:

    sh

curl -sI http://<your-web-server-ip> | grep X-Served-By

Access the HAProxy stats page to monitor traffic distribution (if configured):

sh

    http://<your-load-balancer-ip>/haproxy?stats

Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
