# import smtplib
# from email import encoders
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email.mime.multipart import MIMEMultipart


# server=smtplib.SMTP("smtp.gmail.com",465) 


# server.ehlo()

# server.login("yashmalviya506@gmail.com","yash#999")

# msg=MIMEMultipart()
# msg["From"]="Yash"
# msg["To"]="malviyayash634@gmail.com"
# msg["Subject"]="Just a test"

# with open("backup.txt") as f:
#     message=f.read()
    

# msg.attach(MIMEText(message,"plain"))

# fileName="christopher-robin-ebbinghaus-pgSkeh0yl8o-unsplash.jpg"
# attacment=open(fileName,"rb")


# p=MIMEBase("application","octet-stream")
# p.set_payload(attacment.read())

# encoders.encode_base64(p)

# p.add_header("Content-Disposition",f"attacment; filename={fileName}")
# msg.attach(p)
# text=msg.as_string()
# server.sendmail("yashmalviya506@gmail.com","malviyayash634@gmail.com",text)


# # name=",".join(map(str,cont.keys())).split(",")
#  cont=load_contacts()
#     # json_to_txt(cont)
#     dic={ 
#         "sahil": {
#         "address": "ahemdabad",
#         "email": "",
#         "phone": [
#             "8956905634"
#         ]
#     },
#           "gautam": {
#         "address": "ahemdabad",
#         "email": "",
#         "phone": [
#             "8956675634"
#         ]
#     },}
    
    
#     # data_dic=dic.values()
#     data=list(cont.values())
#     name=",".join(map(str,cont.keys())).split(",")
    
   
#     # delete_contact(cont)
#     # deleted_data(name,data)
    
    
    
   
 
# #   

import smtplib
global server
# Email details
smtp_server = "smtp.gmail.com"
port = 465  # For TLS
sender_email = "malviyasyash634@gmail.com"
password = "yash#999"
receiver_email = "yashmalviya506@example.com"
message = """\
Subject: Test Email from Python

This is a test email sent using smtplib in Python."""

try:
    
    # Connect to the server and start TLS
    server = smtplib.SMTP(smtp_server, port)
    server.starttls()  # Secure the connection
    server.login(sender_email, password)  # Login to the email account
    
    # Send the email
    server.sendmail(sender_email, receiver_email, message)
    server.noop()
    print("Email sent successfully!")
    server.quit()  # Close the connection

except Exception as e:
    print(f"Error: {e}")

