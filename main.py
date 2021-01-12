import email_stuff
import parsing_stuff
import time
import requests
from bs4 import BeautifulSoup

min_size = 40
max_price = 700

recipient = ['dojrana@gmail.com', 'mr.dobrevski@gmail.com']
subject = 'Blip Blop! I have found new apartments per your criteria!'


while True:

    ### Load seen links
    with open('seen_links.txt', 'r') as f:
        seen_links = f.readlines()

    ### Remove new-line characters
    seen_links=[x.strip() for x in seen_links]

    new_apps = 0
    body_string = ''
    with open('seen_links.txt', 'a') as f:
        aps = parsing_stuff.check_new_ads(45, 700)
        for ap in aps:
            link = ap[-1]
            if link not in seen_links:
                new_apps += 1
                ap_string = ' '.join(ap)
                body_string = body_string+ap_string+'\n'
                f.write(link+'\n')
            # print(ap)

    body_base = 'Your humble software servant has found '+str(new_apps)+' new offers within the criteria' \
                  ' SIZE > '+str(min_size)+'m2, price < '+str(max_price)+'e:\n\n'

    body_string = body_base + body_string
    content = [body_string]
    # print(body_string)

    if new_apps > 0:
        email_stuff.send_email(recipient, subject, content)
        print('An email was sent with new offers!')
    else:
        print('No new offers were found. Total offers checked ', len(aps))

    time.sleep(300)
