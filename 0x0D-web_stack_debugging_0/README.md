# Webstack Debugging with Docker and Apache

This project focuses on debugging a webstack running Apache within a Docker container. The goal is to ensure that Apache serves a page containing "Hello Holberton" when querying the root of the container.

## Description

Webstack debugging involves identifying and fixing issues in the components of a webstack, which typically includes web servers, databases, and other services. In this project, we're specifically tackling issues related to Apache web server running in a Docker container.

## Getting Started

To debug the Apache server running in a Docker container and ensure it serves the desired page, follow these steps:

1. Pull the Docker image:
   ```bash
   docker pull holbertonschool/265-0

Run the Docker container, mapping port 8080 on the host to port 80 in the container:

bash

docker run -p 8080:80 -d -it holbertonschool/265-0

Verify that the container is running:

bash

docker ps

Access the container and debug Apache to ensure it serves the "Hello Holberton" page:

bash

# Connect to the container
docker exec -it CONTAINER_ID /bin/bash

# Debug Apache and configure it to serve the desired page

Test the configuration by querying the server's root using curl:

bash

curl 0:8080

If everything is configured correctly, you should receive a response containing "Hello Holberton".

Technologies Used

    Docker: Containerization platform used to run the Apache server.
    Apache HTTP Server: Web server software responsible for serving web pages.
    Shell scripting: Used for debugging and configuring the Apache server.
