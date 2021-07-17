#!/usr/bin/env bash
# This is the script to install pip and the modules required for the app

read -p 'Would you like to install the necessary external modules and installer for the application? ' ANSWER

case "$ANSWER" in
    YES | yes | Yes | Y | y)
        python3 -m ensurepip --upgrade

        pip3 install virtualenv

        virtualenv venv

        source venv/bin/activate

        pip3 install -r requirements.txt
        ;;
    NO | no | No | N | n)
        echo 'If you wish to manually install the necessary modules and the "pip" installer, use these commands:
python3 -m ensurepip --upgrade

pip3 install virtualenv

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt'
        ;;
    *)
        echo 'Please enter y/yes or n/no'
        ;;
esac