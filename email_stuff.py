import yagmail

username="mr.dobrevski@gmail.com"
password="xxx"


def send_email(recipient, subject, content):
    with yagmail.SMTP(username, password) as yag:
        yag.send(recipient, subject, content)
