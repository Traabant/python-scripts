def send_email(user, pwd, recipient, subject, body):
    # posila mail, neumi diakritiku
    import smtplib

    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    TEXT = body

    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        # print ('successfully sent the mail')
        print('successfully sent the mail')
    except:
        print("failed to send mail")

user = "siba.robot@gmail.com"
password = "lplojiju321"
subject = "Nove udalosti MS"
recipient = [
    "david.siba@gmail.com",
]
body = 'test '
send_email(user, password, recipient, subject, body)
