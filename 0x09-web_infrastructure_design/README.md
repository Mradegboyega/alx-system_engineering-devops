# Web Infrastructure Design

This repository documents the design of a web infrastructure for hosting the website www.foobar.com. The design evolves through multiple tasks, incorporating various components and addressing specific requirements.

## Task 0: Simple Web Stack

### Overview
The infrastructure consists of a single server with a LAMP stack, hosting www.foobar.com.

### Components
- **Server:** Represents the hosting machine.
- **Web Server (Nginx):** Handles incoming HTTP requests.
- **Application Server:** Executes the website's code base.
- **Application Files:** The actual code base of the website.
- **Database (MySQL):** Stores and manages data.
- **Domain Configuration:** www.foobar.com configured to the server's IP.

### Specifics
- **Server Role:** Provides resources and services to user computers.
- **Domain Name Role:** Human-readable label mapping to the server's IP.
- **DNS Record Role:** Associates www subdomain with the main domain.
- **Web Server Role:** Handles HTTP requests and serves static content.
- **Application Server Role:** Executes dynamic content code.
- **Database Role:** Stores and manages data.
- **Communication Protocol:** Uses HTTP to communicate with user computers.

### Issues
- **Single Point of Failure (SPOF):** Vulnerable to failures in any component.
- **Downtime during Maintenance:** Web server restarts cause downtime.
- **Limited Scalability:** Difficult to handle high traffic.

---

## Task 1: Distributed Web Infrastructure

### Overview
The infrastructure expands to a distributed model with three servers, a load balancer, and a primary-replica database cluster.

### Additional Elements
- **Web Servers (1 and 2):** Increase availability and provide redundancy.
- **Load Balancer (HAproxy):** Distributes incoming traffic for load balancing.
- **Database (Primary-Replica Cluster):** Enhances fault tolerance and data redundancy.

### Distribution Algorithm
- **Load Balancer:** Configured with Round Robin for even request distribution.

### Active-Active Setup
- **Load Balancer:** Active-Active setup for increased performance and availability.

### Specifics
- **Database Primary-Replica Cluster:** Primary handles writes, replicas handle reads.
- **Difference (Primary vs. Replica):** Primary is authoritative for data; replicas handle reads.

### Issues
- **SPOF:** Load Balancer can be a single point of failure.
- **Security Issues:** Lack of firewall and HTTPS pose risks.
- **No Monitoring:** Monitoring is essential for issue identification.

---

## Task 2: Secured and Monitored Web Infrastructure

### Overview
Enhances the infrastructure with security measures, HTTPS, and monitoring components.

### Additional Elements
- **Firewalls (3):** Added for security.
- **SSL Certificate:** Enables serving encrypted traffic over HTTPS.
- **Monitoring Clients (3):** Data collectors for monitoring services.

### Why Added?
- **Firewalls:** Enhance security by controlling incoming and outgoing traffic.
- **HTTPS:** Secures data transmission between users and the website.
- **Monitoring Clients:** Collect data for analyzing system performance.

### Specifics
- **SSL Termination at Load Balancer:** Potential security issue.
- **Single MySQL Server for Writes:** Single point of failure.
- **Uniform Servers Components:** Potential problem for scalability and diversity.

### Issues
- **SSL Termination:** Load Balancer termination is a security risk.
- **Single MySQL Server:** A single point of failure.
- **Uniform Server Components:** Limited diversity and scalability.

---

## Task 3: Scale Up

### Overview
Scales up the infrastructure with an additional server, load balancer cluster, and separate components.

### Additional Elements
- **Additional Server:** Added for increased capacity.
- **Load Balancer Cluster:** Enhances load balancing and availability.

### Why Added?
- **Additional Server:** Scales capacity to handle more traffic.
- **Load Balancer Cluster:** Improves load balancing and redundancy.

---

