#GET: llegint del disc i mostrant per pantalla en el Servidor i emmagatzemant en el Client.

# TCP server program that upper cases text sent from the client
from socket import *
import os.path
import sys
import random


#Default values
host = 'localhost' # Esta función nos da el nombre de la máquina
port = 12000

#####################################


#Print IP
print('IP Server : ')
os.system("hostname -I")

#####################################

#Random port
port = random.randrange(49152, 65535)
#Print Port
print('Port in usage : ', port)

#####################################

#buffer
size = 2048


print ('The Server is ready to recive...')

# Main code
with socket(AF_INET, SOCK_STREAM) as serverSocket:
	serverSocket.bind(('', port)) 
	serverSocket.listen(1) # Waiting for the connection with the client 
	connectionSocket, addr = serverSocket.accept()# Connected with the client
	# Connecting the socket
	with connectionSocket:
		print('\n\n[**********] Successfully connection with the Client [**********]\n\n')

		opcio = connectionSocket.recv(128).decode()

		if opcio == "PUT" or opcio == "put":
			
			print ('Recieving file,s client ')
			txt = connectionSocket.recv(size)
			print (' ------ Recieved successfully ------\n')
			
			print ('Opening file')
			with open(txt, 'r') as f:
			    contenido = f.read()
			print ('------ Opened successfully ------ \n')       
			
			print ('Setting directory,s path ')
			directory = connectionSocket.recv(size).decode()
			
			print ('Setting file,s name ')
			name = connectionSocket.recv(size).decode()
			print ('\n\n')
			    
			completeName = os.path.join(directory, name)
			
			
			file1 = open(completeName, "w")
			file1.write(contenido)
			file1.close()
			
			print('File,s content : ')
			print(contenido)
			print('\nThis file has saved in : ', completeName)
			
			
		elif opcio == "GET":
			print ('Recieving file,s client ')
			txt = connectionSocket.recv(size)
			print (' ------ Recieved successfully ------\n')
			
			print ('Opening file')
			with open(txt, 'r') as f:
				contenido = f.read()
			print ('------ Opened successfully ------ \n')  
				
			connectionSocket.send(contenido.encode())
			
	
	connectionSocket.close()			
