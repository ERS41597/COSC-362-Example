
# Python Script that retreives user login information from the "Last" command. This includes the username, login time, and the IP adress. It then generates a document of the retreived information.
# Author: Eric Sensebaugh


import subprocess
import re
from collections import defaultdict

# Run the "last" command and capture its output
output = subprocess.check_output(['last']).decode('utf-8')

# Define a regular expression pattern to extract login information
pattern = re.compile(r'(\S+)\s+(\S+)\s+(\S+)\s+(\S+)\s+([(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})\w]*)')

# Create a dictionary to store login information by user
login_info = defaultdict(list)

# Process the login data
for line in output.splitlines():
    match = pattern.match(line)
    if match:
	# Extract the user info, terminal, IP address, and the login data. 
        user, terminal, ip, login_time, _ = match.groups()
	# Storing the login information by the user
        login_info[user].append((login_time, ip))

# Create a document with user login information
document = "User Login Information\n\n"
for user, logins in login_info.items():
    document += f"User: {user}\n"
    for login_time, ip in logins:
        document += f"  - Login Time: {login_time}\n"
        document += f"  - IP Address: {ip}\n"
    document += "\n"

# Write the document to a file
with open("login_info.txt", "w") as file:
    file.write(document)

# Notifying the User that the script ran successfully
print("User login information saved to login_info")
