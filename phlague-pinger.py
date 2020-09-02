import os

ip_list = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]
for ip in ip_list:
	response = os.popen(f"ping {ip}").read()
	if "Received = 4" in response:
		print(f"Online {ip} Process Successful")
	else:
		print(f"Offline {ip} Process Denied")