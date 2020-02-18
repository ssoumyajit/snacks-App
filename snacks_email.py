import smtplib, ssl

smtp_server = "smtp.gmail.com"
port = 465 

#create a secure SSL context
context = ssl.create_default_context()
sender_email = "inmygroovelifestyle@gmail.com"
receiver_email = "inmygroovelifestyle@gmail.com"
message = """\
        This is a test message from python by River."""
password = input("Type your password and press enter: ")

try:
    server = smtplib.SMTP(smtp_server, port)
    print(server)
    server.starttls(context = context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
except Exception as e:
    print(e)
finally:
    server.quit()

    
    
    
