from email.message import EmailMessage

import ssl
import smtplib

email_sender = 'zaynkoshyari1234@gmail.com'
email_password = 'mmylaazjjqdbfuzj'

email_receiver = 'naticik237@iunicus.com'

subject = "Dont forget to subscribe"
body = """
When you watch a video, please hit subscribe
"""

em= EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)



# create a context
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.google.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())


   