import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import getpass

sender_email = input("Direción de envio: ")
password = getpass.getpass()
receiver_email = input("Direccion del destino: ")
integrantes = input ("Ingresa los integrantes del equipo: ")

message = MIMEMultipart("alternative")
message["Subject"] = input("Asunto: ")
message["From"] = sender_email
message["To"] = receiver_email
body = input("Ingresa el texto: ")
filename = input("Ingresa el nombre del archivo: ")  # In same directory as script

# Turn these into plain/html MIMEText objects
part1 = MIMEText(body, "plain")

# Add body to email
message.attach(MIMEText(body, "plain"))

# Open file
with open(filename, "rb") as attachment:
    # Add file as application/octet-stream
    # Email client can usually download this automatically as attachment
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email    
encoders.encode_base64(part)

# Add header as key/value pair to attachment part
part.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)

# Add attachment to message and convert message to string
message.attach(part)
text = message.as_string()

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP("outlook.office365.com", 587) as server:
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, message.as_string()
    )
    print(message.as_string())
