import sys
import subprocess

#Implement pip as a subprocess to upgrade pip and then install virtualenv
if sys.argv[1] == "virtualenv":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'virtualenv'])
    print("Successfully installed Virtual Environment")
# implement pip as a subprocess to install Scapy
if sys.argv[1] == "scapy":
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--pre', 'scapy[basic]'])
    print("Successfully upgraded pip and installed scapy")

