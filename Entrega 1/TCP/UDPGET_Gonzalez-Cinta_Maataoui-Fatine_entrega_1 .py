#GET: llegint del disc i mostrant per pantalla en el Servidor i emmagatzemant en el Client.

# TCP server program that upper cases text sent from the client
from socket import *
import os.path
import random

# Default port number server will listen on
serverPort = 12000

BUFFER_SIZE = 1024

print('IP Server : ', os.system("hostname -I"))


print ('El Servidor esta listo para recibir...')
print ('Servers hostname: ', gethostbyname(gethostname()))

#Abrimos nuevo Socket y establcemos un nuevo puerto aleatorio (RCF 1350)
serverPort = random.randrange(49152, 65535)

# Request IPv4 and TCP communication
serverSocket = socket(AF_INET, SOCK_DGRAM)

# The welcoming port that clients first use to connect
serverSocket.bind((gethostbyname(gethostname()), serverPort))
print("El Servidor conectado al puerto", serverPort, "\n")

print('[*] Conexión establecida')

#------------------------------------------------------------
while True:

	print('Waiting for the option chosen by the Client  ...')
	opcio, clientAddress = serverSocket.recvfrom(1024)
	opcio = opcio.decode()
	print (opcio)
	print(' *** Received successfully *** ')

	if opcio == "PUT" or opcio == "put":
		
		
		txt, clientAddress = serverSocket.recvfrom(1024)
		print(' *** Received successfully *** ')
		
		with open(txt, 'r') as f:
		    contenido = f.read()
		
		directory, clientAddress = serverSocket.recvfrom(1024)
		print(' *** Received successfully *** ')
		
		name, clientAddress = serverSocket.recvfrom(1024)
		print(' *** Received successfully *** ')
		    
		completeName = os.path.join(directory.decode(), name.decode())
		print('Directori on es vol guardar : ',completeName)
		
		file1 = open(completeName, "wb")
		file1.write(contenido)
		file1.close()
		
		print(contenido.decode('utf-8'))
		#connectionSocket.send(capitalizedSentence.encode())
		
	elif opcio == "GET" or opcio == "get":
		print('Receiving file from Client ...')
		arxiu, clientAddress = serverSocket.recvfrom(1024)
		print(' *** Received successfully *** ')
		
		print('El arxiu es leido per el servidor... \n')
		
		with open(arxiu.decode(), 'rb') as f:
			contenido = f.read()
		print('Enviando el archivo al cliente... \n')	
		serverSocket.sendto(contenido, clientAddress)
		
		
	#cerrar
	#connectionSocket.close()

		
