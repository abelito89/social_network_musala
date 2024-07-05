from email.message import EmailMessage
import smtplib
from dotenv import load_dotenv
import os
import ssl

load_dotenv()

def send_email(to_email, subject, body):
    """
    Send a confirmation email to the newly created user.

    Parameters:
    - `to_email`: The email address of the recipient.
    - `subject`: The subject of the email.
    - `body`: The body content of the email.
    """
    # Configurar el mensaje de correo
    msg = EmailMessage()
    msg['From'] = EMAIL_FROM
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.set_content(body)
    # Establecer conexión con el servidor SMTP y enviar correo
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT, context=context) as server:
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.sendmail(EMAIL_FROM, to_email, msg.as_string())

# Configuración del servidor de correo electrónico
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_USER = os.getenv('EMAIL_USER')  # el que recibe el correo
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_FROM = os.getenv('EMAIL_FROM')  # desde donde se envía el correo
context = ssl.create_default_context()