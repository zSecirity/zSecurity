#!/bin/bash

# Colors for output
GREEN="\e[32m"
RED="\e[31m"
YELLOW="\e[33m"
BLUE="\e[34m"
RESET="\e[0m"

echo -e "${BLUE}Starting installation...${RESET}"
echo -e "${YELLOW}Please wait while we set up everything for you...${RESET}"

# Check if running in Termux or Kali Linux
if [ -d "$HOME/../usr" ]; then
    echo -e "${GREEN}Termux detected...${RESET}"
    echo -e "${YELLOW}Updating and upgrading Termux packages...${RESET}"
    pkg update -y && pkg upgrade -y
    pkg install python -y
    pkg install git -y
    echo -e "${YELLOW}Termux setup complete!${RESET}"
elif [ -f "/etc/debian_version" ]; then
    echo -e "${GREEN}Kali Linux detected...${RESET}"
    echo -e "${YELLOW}Updating and upgrading Kali Linux packages...${RESET}"
    sudo apt update -y && sudo apt upgrade -y
    sudo apt install python3 python3-pip git -y
    echo -e "${YELLOW}Kali Linux setup complete!${RESET}"
else
    echo -e "${RED}Unsupported OS detected! Exiting...${RESET}"
    exit 1
fi

# Give execution permission to zsecurity.py
echo -e "${YELLOW}Granting execution permissions to zsecurity.py...${RESET}"
chmod +x zsecurity.py
echo -e "${YELLOW}Execution permissions granted!${RESET}"

# Final message
echo -e "${GREEN}Installation complete!${RESET}"
echo -e "${BLUE}You can now run the tool by using the command: ${YELLOW}python3 zsecurity.py${RESET}"
echo -e "${GREEN}zSecurity!${RESET}"
