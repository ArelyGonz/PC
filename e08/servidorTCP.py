#!/usr/bin/env python
import argparse
import socket
from cryptography.fernet import Fernet
#Paso de argumentos
description ="""-h -msj "Mensaje a enviar"""
parser = argparse.ArgumentParser (description='Port scanning',
                                epilog=description,
                               formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument ("-msj", metavar='MSJ', dest="msj",
                    help="mensaje a enviar",required=True)
params = parser.parse_args ()
#Generar el objeto para cifrar
clave = Fernet.generate_key ()
cipher_suite = Fernet (clave)
#Almacenamos la clave
file = open ('clave.key', 'wb')
file.write (clave)
file.close ()
                                # se guarda en bytes wb
#Tomar el argumento, convertirlo a bytes
mensaje = params.msj
mensajeBytes = mensaje.encode ()
#Ciframos el mensaje
msj_cifrado = cipher_suite.encrypt (mensajeBytes)
print ("Mensaje enviado:\n",mensaje)
#Preparamos los datos de la conexión
TCP_IP = 'l27.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 2048 #Cantidad de info que se queda en memoria
#Establecemos la conexión
s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
s.connect ( (TCP_IP, TCP_PORT))
s.send (msj_cifrado)
respuesta = s.recv (BUFFER_SIZE).decode ()
s.close ()
print ("Respuesta recibida:", respuesta)
