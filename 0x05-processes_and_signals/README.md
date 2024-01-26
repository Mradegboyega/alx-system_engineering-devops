# System Engineering & DevOps - Bash, Processes, and Signals

This repository contains Bash scripts and C programs created as part of the System Engineering & DevOps curriculum. The tasks cover various concepts, including Bash scripting, process management, and signals handling.

## Bash Scripts

### Task 0: What is my PID
- Script: [0-what-is-my-pid.sh](0-what-is-my-pid.sh)
- Description: Displays the PID of the script.

### Task 1: List your processes
- Script: [1-list-your-processes.sh](1-list-your-processes.sh)
- Description: Displays a list of currently running processes.

### Task 2: Show your Bash PID
- Script: [2-show-your-bash-pid.sh](2-show-your-bash-pid.sh)
- Description: Displays lines containing the word 'bash' to get the PID of the Bash process.

### Task 3: Show your Bash PID made easy
- Script: [3-show-your-bash-pid-made-easy.sh](3-show-your-bash-pid-made-easy.sh)
- Description: Displays the PID and process name of processes containing the word 'bash'.

### Task 4: To infinity and beyond
- Script: [4-to-infinity-and-beyond.sh](4-to-infinity-and-beyond.sh)
- Description: Displays "To infinity and beyond" indefinitely with a sleep of 2 seconds.

### Task 5: Don't stop me now!
- Script: [5-dont-stop-me-now.sh](5-dont-stop-me-now.sh)
- Description: Stops the "4-to_infinity_and_beyond" process using `pkill`.

### Task 6: Stop me if you can
- Script: [6-stop-me-if-you-can.sh](6-stop-me-if-you-can.sh)
- Description: Stops the specified process without using `kill` or `killall`.

### Task 7: Highlander
- Script: [7-highlander.sh](7-highlander.sh)
- Description: Displays "To infinity and beyond" with signals handling for SIGTERM.

### Task 67: Stop me if you can
- Script: [67-stop-me-if-you-can.sh](67-stop-me-if-you-can.sh)
- Description: Stops the "7-highlander" process without using `kill` or `killall`.

### Task 8: Beheaded process
- Script: [8-beheaded-process.sh](8-beheaded-process.sh)
- Description: Kills the "7-highlander" process.

### Task 9: Process and PID file
- Script: [9-process-and-pid-file.sh](9-process-and-pid-file.sh)
- Description: Creates a PID file, displays messages, and handles signals.

## C Programs

### Task 102: Zombie
- Program: [102-zombie.c](102-zombie.c)
- Description: Creates 5 zombie processes and handles signals.

## Usage

Make scripts executable before running:

```bash
chmod +x script_name.sh

Run the scripts:

bash

./script_name.sh

For C programs:

bash

gcc program_name.c -o program_name
./program_name
