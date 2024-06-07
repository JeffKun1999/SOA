import smtplib
from email.mime.text import MIMEText

def enviar_correo(mensaje):
    sender_email = "je1400r@gmail.com"
    app_password = "enhf stah udrj zslq"  # Utiliza la contraseña de aplicación generada

    receiver_email = "dimehof339@jadsys.com"

    message = MIMEText(mensaje)
    message['Subject'] = 'Mensaje de la cola'
    message['From'] = sender_email
    message['To'] = receiver_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()

# Ejemplo de uso (llamar a esta función cuando se reciba un mensaje)
mensaje_recibido = "Este es un mensaje recibido desde la cola."
enviar_correo(mensaje_recibido)
