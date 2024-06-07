import pika

def enviar_mensaje(mensaje):
    credentials = pika.PlainCredentials('jeff', 'jeff')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
    channel = connection.channel()
    
    channel.queue_declare(queue='cola')

    channel.basic_publish(exchange='', routing_key='cola', body=mensaje)
    print("Mensaje enviado a la cola: %r" % mensaje)
    
    connection.close()

# Ejemplo de uso
enviar_mensaje("Hola desde el productor!")
