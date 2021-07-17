#!/usr/bin/env bash
# This is the script to execute Black-Box
if [[ $1 == '-help' ]]; then
    cat ../docs/help-documentation.txt
    exit 0
elif [[ $1 == '-prInstall' ]]; then
    echo 'Running installer...'
    sleep 3
    ./moduleinstaller.sh
    exit 1
elif ! [[ $# < 1 && -x "$(command -v python3)" ]];
then    
    echo 'Error:
This program runs on Python, but it looks like Python is not installed.
To install Python, check out https://installpython3.com/' >&2
    exit 2
else
    echo 'Looks like you have Python 3. You are good to go!
Launching Black-Box...'
    sleep 3
    python3 main.py
fi