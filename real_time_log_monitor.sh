#!/bin/bash

# Script Description
# This script monitors a log file in real-time, filtering lines that contain specific keywords.
# It is useful for live monitoring of important events or error logs on Linux systems.

# Prompt for log file path and keyword
read -p "Enter the path to the log file: " log_file
read -p "Enter the keyword to monitor for (e.g., ERROR, WARNING): " keyword

# Verify log file exists
if [[ ! -f $log_file ]]; then
    echo "Log file does not exist: $log_file"
    exit 1
fi

# Monitor log file in real-time, filtering for the keyword
echo "Monitoring $log_file for occurrences of '$keyword'..."
tail -f "$log_file" | grep --line-buffered "$keyword"
