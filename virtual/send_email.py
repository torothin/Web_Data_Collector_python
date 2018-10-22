from email.mime.text import MIMEText
import smtplib

def send_email(email,height,average_height,count):
    from_email="bradford.duvall@gmail.com"
    from_password="tax4Baby"
    to_email="bradford.duvall@gmail.com"

    subject="Height Data"
    message="{}, Your height was <strong>{}</strong>, avg {} of {} people.".format(email, height, average_height,count)

    msg=MIMEText(message, 'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, from_password)
    gmail.send_message(msg)
