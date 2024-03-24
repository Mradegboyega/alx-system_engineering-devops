# Configuration Management Tasks

This repository contains Puppet manifests for completing various configuration management tasks.

## Tasks

### Task 0: Create a File

**Description:** Using Puppet, create a file in `/tmp`.

- **File Path:** `/tmp/school`
- **File Permission:** `0744`
- **File Owner:** `www-data`
- **File Group:** `www-data`
- **File Content:** `I love Puppet`

### Task 1: Install a Package

**Description:** Using Puppet, install Flask from pip3.

- **Version:** 2.1.0

### Task 2: Execute a Command

**Description:** Using Puppet, create a manifest that kills a process named `killmenow`.

- **Command Used:** `pkill killmenow`

## Usage

To apply any of the tasks, navigate to the directory containing the corresponding Puppet manifest file and run:


Ensure that you have Puppet installed and properly configured on your system before running the commands.


