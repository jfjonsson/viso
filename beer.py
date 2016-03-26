# Jón Fresyteinn Jónsson 09-09-2015
import requests as r
import time, datetime, sys
from getpass import getpass
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://myschool.ru.is/myschool/'


print('Please authenticate with RU Myschool username and password.')
print()
while True:
    AUTH = (input('Username: '), getpass('\nPassword: '))
    front_page = r.get(BASE_URL, auth=AUTH)
    if front_page.ok:
        front_page = BS(front_page.text, "html.parser")
        break
    else:
        print('Authentication failed.')

print()

while True:
    try:
        EVENT_URL = input('Enter the event url: ')
        event_page = r.get(EVENT_URL, auth=AUTH)
        event_page = BS(event_page.text, "html.parser")
        POST_URL = event_page.center.form['action']
        print(BASE_URL + POST_URL)
        break;
    except:
        print('Provided url is not valid')

while True:
    leet = datetime.datetime.now().replace(hour=13, minute=36, second=45, microsecond=0)
    if datetime.datetime.now() > leet:
        while True:
            payload = {'payload': 'empty'}
            post_result = r.post(BASE_URL + POST_URL, data=payload, auth=AUTH)
            post_result = BS(post_result.text, "html.parser")
            ruButton = post_result.center.form.find('input', {"name" : "ruButton"})
            if ruButton['value'] == 'Afskrá':
                print('Success!')
                sys.exit()
            else:
                print('...')
    else:
        print('Starting in: ', leet - datetime.datetime.now())

