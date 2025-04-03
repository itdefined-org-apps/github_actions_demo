#!/bin/bash
set -e  # Exit on error
echo "Installing: ${SOFTWARE_NAME}"
sudo apt update
sudo apt install -y "${SOFTWARE_NAME}"
echo "${SOFTWARE_NAME} installation completed!"