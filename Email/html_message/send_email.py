def send_email(user, pwd, recipient, subject):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText
    from email.MIMEImage import MIMEImage

    FROM=user
    TO = recipient
    gmail_user = user
    gmail_pwd = pwd

    msgRoot = MIMEMultipart('related')
    msgRoot['Subject'] = subject
    msgRoot['From'] = user
    msgRoot['To'] = recipient

    msgAlternative = MIMEMultipart('alternative')
    msgRoot.attach(msgAlternative)
    fp = open('test.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', '<image1>')
    msgRoot.attach(msgImage)
    fb = open('test.html','rb')
    msgText = MIMEText(fb.read(),'html')
    fb.close()
    msgAlternative.attach(msgText)
    
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    #print server
    server.login(gmail_user, gmail_pwd)
    #print server
    server.sendmail(FROM, TO, msgRoot.as_string())
    server.close()
    print 'successfully sent the mail'
    
user_email=                      #your_email
user_password=                   #your email's password
to_email=                        #receipt's email
subject=                         #email's subject

send_email(user_email,user_password,to_email,subject)
