import smtplib

port = 25
smtp_server = "127.0.0.1"
sender_email = "sender@domain.htb"  # Enter your address
receiver_email = "receiver@domain.htb"  # Enter receiver address
message = "this is message to john from kyle"

try:
    server = smtplib.SMTP(smtp_server,port)
    server.ehlo() # Can be omitted
    server.starttls(context=context) # Secure the connection
    server.ehlo() # Can be omitted
    server.login(sender_email, password)
    # TODO: Send email here
except Exception as e:
    # Print any error messages to stdout
    print(e)
finally:
    server.quit() 
