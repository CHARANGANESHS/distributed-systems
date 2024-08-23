ifconfig en0 | grep 'inet ' | awk '{print $2}' > ip.txt
conda activate
clear
python3 traits.py
python3 server.py
rm ip.txt