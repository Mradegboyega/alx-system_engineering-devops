SSH Configuration Tasks

This repository contains scripts and configuration files related to SSH (Secure Shell) configuration tasks. These tasks aim to automate various aspects of SSH configuration for connecting to servers securely.
Task 0: Use a Private Key
Objective:

Write a Bash script that uses SSH to connect to a server using the private key ~/.ssh/school with the user ubuntu.
Instructions:

    Use only SSH single-character flags.
    Do not use -l.
    Do not handle the case of a private key protected by a passphrase.

Task 1: Create an SSH Key Pair
Objective:

Write a Bash script that creates an RSA key pair.
Requirements:

    The name of the created private key must be school.
    The number of bits in the created key must be 4096.
    The created key must be protected by the passphrase betty.

Task 2: Client Configuration File
Objective:

Configure the local SSH client using a configuration file.
Requirements:

    Configure the SSH client to use the private key ~/.ssh/school.
    Configure the SSH client to refuse authentication using a password.

Task 4: Client Configuration File (w/ Puppet)
Objective:

Use Puppet to make changes to the SSH client configuration file.
Requirements:

    Configure the SSH client to use the private key ~/.ssh/school.
    Configure the SSH client to refuse authentication using a password.

Usage

    Each task has its own script or configuration file.
    Execute the scripts directly or apply the configuration files as instructed in the task descriptions.
    Ensure that the SSH keys are generated and stored securely.
    Test the SSH configurations to verify that they work as expected.

Author

This repository was created by [Adegboyega Ademola].

Feel free to contribute to this repository by submitting pull requests or reporting any issues encountered. Thank you!
