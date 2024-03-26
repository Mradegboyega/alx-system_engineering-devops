# Project Name: Configuring a Web Server

This project involves setting up and configuring a web server using various tools and scripts. The primary objectives include file transfer, web server installation, domain setup, redirection, and using Puppet for automation.

## Task Summaries

### 0. Transfer a File to Your Server

- **Objective**: Write a Bash script that transfers a file from a client to a server.
- **Requirements**:
  - Script accepts four parameters: path to the file, server IP, username, and path to SSH private key.
  - Must display usage information if incorrect number of arguments are provided.
  - Utilizes `scp` for file transfer to the user's home directory, with strict host key checking disabled.

### 1. Install Nginx Web Server

- **Objective**: Install Nginx and configure it to serve a custom HTML page.
- **Requirements**:
  - Install Nginx on Ubuntu server.
  - Nginx listens on port 80 and returns a "Hello World!" page on the root URL.
  - Script must not use `systemctl` for restarting Nginx.

### 2. Setup a Domain Name

- **Objective**: Register a `.tech` domain and configure DNS to point to your server.
- **Requirements**:
  - Obtain a free `.tech` domain.
  - Configure DNS A record to point the domain to your server's IP.
  - Verification of domain setup is required.

### 3. Redirection

- **Objective**: Configure Nginx to redirect a specific path to another URL.
- **Requirements**:
  - Implement a 301 "Moved Permanently" redirection.
  - The redirection script should be part of the server's configuration.

### 5. Install Nginx Web Server (w/ Puppet)

- **Advanced Task**
- **Objective**: Use Puppet to install and configure Nginx, including setting up a 301 redirect.
- **Requirements**:
  - Nginx listens on port 80.
  - Root URL serves a "Hello World!" page.
  - `/redirect_me` path redirects to a specified URL with a 301 status code.

## Technologies Used

- Bash scripting
- `scp` for secure file transfer
- Nginx as a web server
- DNS configuration for domain setup
- Puppet for automation and configuration management

## Setup and Configuration

Please refer to each task's specific instructions for setup and configuration details. Ensure all scripts are executable and test configurations on an Ubuntu 16.04 LTS environment.

## Contributing

Feel free to fork this project and submit pull requests for improvements or additional features. For major changes, please open an issue first to discuss what you would like to change.

