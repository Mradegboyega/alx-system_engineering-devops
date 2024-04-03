# Project Title: Nginx Configuration Scripts

## Description

This project comprises Bash scripts designed to automate the installation and configuration of Nginx on Ubuntu 20.04 LTS servers. It ensures that Nginx is installed, running, and set up to listen on port 80 across the server's active IPv4 addresses.

## Getting Started

### Dependencies

- Ubuntu 20.04 LTS
- Internet access for package downloads
- Root or sudo privileges for package installation and system service modification

### Installing

1. **Prepare Your Environment**: Verify you're on Ubuntu 20.04 LTS with root or sudo access.
2. **Clone the Repository** (if applicable): Clone this repository to your machine or directly download the script files.

   ```bash
   git clone [repository-url]
   cd [repository-name]

Make Scripts Executable: Change the scripts' permissions to make them executable.

bash

    chmod +x 0-nginx_likes_port_80 1-debugging_made_short

Executing Program

    Running the Installation Script: To set up and start Nginx so it listens on port 80, execute the main script.

    bash

./0-nginx_likes_port_80

Quick Setup: For a condensed setup version (assuming dependencies are met), run the shorter script.

bash

    ./1-debugging_made_short

Help

If issues arise, ensure all dependencies are correctly installed and that there is internet connectivity. For more detailed help, open an issue in the repository with a comprehensive description of the problem.
