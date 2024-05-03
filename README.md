This Python script, ipscanner.py, allows you to scan a range of IP addresses to check if they are online or not. It utilizes the ping command available in most Unix-based systems to send ICMP echo requests and waits for a response to determine the online status of each IP.

How to Use:

Clone the Repository: Clone the repository containing the script using the following command:

bash

$ git clone https://github.com/nabilmursi/ip-address-scanner.git

Navigate to the Directory: Change your current directory to the cloned repository:

bash

$ cd ip-address-scanner

Run the Script: Execute the Python script with the appropriate arguments:


python3 ipscanner.py <start_ip> <end_ip>

Replace <start_ip> and <end_ip> with the starting and ending IP addresses of the range you want to scan, respectively. For example:

$ python3 ipscanner.py 192.168.1.1 192.168.1.10

View Results: The script will print out the IP addresses that are online within the specified range.

Requirements:

Python 3.x
Unix-based operating system (Linux, macOS)

Notes:

Ensure that you have appropriate permissions to execute the ping command.
The script uses ICMP echo requests, so it may not work in environments where ICMP packets are blocked.
The timeout for each ping request is set to 1 second (-W 1), which can be adjusted based on your network conditions.

Feel free to contribute to the repository or report any issues you encounter. Happy scanning! 🚀
