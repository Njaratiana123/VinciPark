import smtplib
import ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "rwajar@gmail.com"  # Enter your address
receiver_email = "ryuzakkiiiyo@gmail.com"  # Enter receiver address
password = "ANDRIANAVALONA"
message = "hasina"

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    try:
      server.login(sender_email, password)
    except Exception as e:
        print(" erreur", e)
    server.sendmail(sender_email, receiver_email, message)
