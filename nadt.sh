#!/bin/bash

DIRECTORY="venv/lib/python3.6/site-packages/scapy" #Destination to determine if the Scapy Package is installed or not on the machine's virtual enviroment
MASTERFILE="MASTER.json"
REPEATFILE="REPEAT.json"
virtenv_dir="venv"
curr_dir=$(pwd)
end="/venv"
nadt () {
	if [ -d "$virtenv_dir" ]; then #If the folder venv exists, continue
		echo "$virtenv_dir exists!"
	else #If the folder venv DNE, install the Virtual Enviroment package and setup the venv folder
		echo "$virtenv_dir not found...\nSetting up the python virtual enviroment now!"
		python3 packageInstaller.py virtualenv #Runs a pip install command to install virtualenv which is used to create the Virtual Enviroment
		python3 -m venv $curr_dir$end #Creates the virtual enviroment directory which will handle running python scripts and download packages here 
	fi
	source venv/bin/activate #Turns on Virtual Enviroment (all python package installations and python scripts will be installed/runned here)
	if [ -d "$DIRECTORY" ]; then #Checks to see if Scapy is installed in the directory
		echo "$DIRECTORY exists! Executing Program..."
	else
		echo "$DIRECTORY not found..."
		while true ; do #Handles user input on decision to download Scapy or not
			read -p "Would you like to install Scapy (y/n)? " answer
			if [ $answer == "Y" ] || [ $answer == "y" ]; then
				echo "Installing Scapy, one moment..."
				echo "Going to upgrade pip in the Virtual Environment..."
				python3 packageInstaller.py scapy #Runs a pip install command to install Scapy onto the users Virtual Enviroment
				break
			elif [ $answer == "N" ] || [ $answer == "n" ]; then
				echo -e "Scapy is required to run certain scripts \nEnding Shell Script..."; deactivate; exit 1; #Turns off Virtual Enviroment for Python and ends the Script
			else
				echo "Wrong input... Please try again!"
			fi
		done
	fi
	sudo env "PATH=$PATH" python3 networkScanner.py #Scans the network to find all available devices and then dumps the information into a txt file
	python3 dataConversion.py #Runs the scripts that converts the data in the txt into a JSON File
	if [ -f $MASTERFILE ] && [ -f $REPEATFILE ]; then
		python3 onlineDetection.py #Compares the MASTER JSON and REPEAT JSON to determine whether a computer is online or not
	fi
	deactivate #Turns off Virtual Enviroment for Python
}
nadt
#EOF
