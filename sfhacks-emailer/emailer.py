import smtplib, ssl
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

port = 465
name = input("Please enter your full name: ")
password = input("Please enter your password for sfhacksteam@gmail.com: ")
csv_file = input("Please enter the CSV file you'd like to pull from: ")

if ('.csv' not in csv_file):
    csv_file = csv_file + '.csv'

sender_email = "sponsors@sfhacks.io"
receiver_email = "sfhacksteam@gmail.com"
message_body = """
Hello {first_name},

Hope you’re doing well! 

My name is {name}, and I'm part of the partnership team for SF Hacks 2020, the largest student-run collegiate hackathon in San Francisco. Our last hackathon in 2019 was a huge success in terms of quality projects and growth in numbers across the board: we grew from 320 participants in 2018 to 570 participants last year, 20% of whom were female hackers. Last year’s projects ranged from non-browser search engines to apps that could be used to report domestic abuse through a disguised platform.

We'd love to have {company} on the SF Hacks fam! Please let us know if you’d be interested in partnering with SF Hacks 2020 or if you have any questions, and I would be happy to talk more. 

Best regards,
{name}
Partnerships @ SF Hacks 2020
sponsors@sfhacks.io
"""


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("sfhacksteam@gmail.com", password)
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')

        for row in reader:
            company = row[0]
            fullname = row[1]
            email = row[3]
            contact_message_body = message_body.format(name=name, company=company, first_name=fullname.split(" ")[0])

            if (('@' in email) and (fullname != None)):
                print("Emailing: {}: {} at {}".format(company, fullname, email))
                message = MIMEMultipart()
                message['Subject'] = 'SF Hacks 2020 Partnership Opportunity'
                message['From'] = sender_email
                message['To'] = email
                message.attach(MIMEText(contact_message_body, 'plain'))

                server.sendmail(sender_email, 
                        email, 
                        message.as_string())

