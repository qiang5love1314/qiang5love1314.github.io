import requests
from bs4 import BeautifulSoup
import time

google_scholar = "https://scholar.google.com/citations?user=2fHc1o4AAAAJ&hl=zh-CN"

previous_citations = 620

def send_notification(new_citations):
    import smtplib
    from email.mime.text import MIMEText

    sender_email = 'abc2611617@gmail.com'
    sender_password = 'fymzdbzzehsietsz'
    recipient_email = 'abc2611617@qq.com'

    subject = 'You have new citations'
    message = f'Your citations have be updated by: {new_citations}'

    msg = MIMEText(message)
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)    #mail.bjtu.edu.cn  465
        server.ehlo()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        print('message have been sent')
    except Exception as e:
        print('error')

import chardet
while True:
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
        response = requests.get(google_scholar, headers=headers)
        encoding = chardet.detect(response.content)['encoding']
        response.encoding = encoding
        soup = BeautifulSoup(response.text, 'html.parser')

        indexes = soup.find_all("td", "gsc_rsb_std")
        h_index = indexes[2].string
        i10_index = indexes[4].string
        citations = indexes[0].string
        print(citations)
        citations = int(citations.replace(',', ''))

        if citations != previous_citations:
            print(f'citations have been changes: {previous_citations} -> {citations}')
            send_notification(citations)
            previous_citations  = citations

        time.sleep(3600*24) # 3600*24
    except Exception as e:
        print('错误')
