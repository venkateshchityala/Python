import subprocess

data = subprocess.check_output(['netsh','wlan','show','profile']).decode('utf-8',errors="backslashreplace").split("\n")
profiles = [i.split(":")[1][1:-1]for i in data if "All User Profile" in i]
for i in profiles:
	try:
		results = subprocess.check_output(['netsh','wlan','show','profile',i,'key=clear']).decode('utf-8',errors="backslashreplace").split("\n")
		results = [b.split(":")[1][1:-1]for b in results if "Key Content" in b]
		try:
			print("{:<30}| {:<}".format(i,results[0]))
		except IndexError:
			print("{:<30}| {:<}".format(i,""))
	except subprocess.CalledProcessError:
		print("{:<30}| {:<}".format(i,"Encoding Error"))
input("")