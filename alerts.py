import smtplib
from email.mime.text import MIMEText
from tracker import data

def send_email_alert(crypto, price):
    sender = '************@gmail.com'
    recievers = ['****@gmail.com']
    subject = f'{crypto} price alert'
    body = f'the price of {crypto} has reached ${price}'

    msg = MIMEText(body)
    msg['subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recievers)

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender, 'yourpassword')
        server.sendmail(sender, recievers, msg.as_string())

#example:
if data['bitcoin']['usd'] > 50000:
    send_email_alert('Bitcoin', data['bitcoin']['usd'])

