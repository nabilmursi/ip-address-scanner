How to Use This Script

Save the script to a file named ipscanner.py.
Run the script by providing the start and end IP addresses in the command line like this:

python3 ipscanner.py 192.168.1.1 192.168.1.255

The script will print only the IPs that are online.

Notes
The script performs a quick ping check and suppresses all output except for the online notification.
Ensure your system allows ICMP requests through the firewall, as some systems might block ICMP/ping requests, which could lead to false negatives (i.e., the script might report that an IP is offline when it's actually online but blocking ping requests).
