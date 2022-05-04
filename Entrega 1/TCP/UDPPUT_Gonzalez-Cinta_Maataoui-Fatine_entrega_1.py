# PUT: llegint del disc i mostrant per pantalla en el Client i emmagatzemant en el Servidor.

import sys
import os.path
import random
from socket import *

# Default to running on localhost, port 12000
clientName = gethostbyname(gethostname())
clientPort = random.randrange(49152, 65535)
print('Clients IP: ', clientName, ' with the port ', clientPort, '')

serverName = input('Introduce the IP of the Server :')
serverPort = int(input('Introduce the Port of the Server :'))

# Request IPv4 and UDP communication
clientSocket = socket(AF_INET, SOCK_DGRAM) 
clientSocket.bind((clientName, clientPort))

# Time of waiting answer: 1 second
clientSocket.settimeout(1)

# Read file from the user
funcion = input('Write what function you want to do (GET o PUT): ')
clientSocket.sendto(funcion.encode(),(serverName,serverPort))


print('Contact with the server ', serverName, ' from the port ', serverPort, '')

txt = input('Put which file you want to read : ')

if funcion == "GET" or funcion == "get":
	print('You have chosen the GET function ')

	print('Sending file to Server ...')
	clientSocket.sendto(txt.encode('utf-8'),(serverName,serverPort))
	
	print('Waiting to receive from the Server ...')
	contenido, serverAddress = clientSocket.recvfrom(1024)
	print(' *** Received successfully *** ')
	
	
	print('Saving the file ...')

	save_path = input('Put in which directory you want to save it ----> ')
	if not os.path.exists(save_path):
		print('The directory you chose does not exist. ')
	else:
		file_name = input('What name do you want to put in the new file? : ')
		completeName = os.path.join(save_path, file_name)
		print(completeName)
		file1 = open(completeName, "wb")
		file1.write(contenido)
		file1.close()
		#a = type(contenido)
		#print (a)
		print(contenido)

elif funcion == "PUT" or funcion == "put":
	print('You have chosen the PUT function')
	clientSocket.sendto(txt.encode('utf-8'),(serverName,serverPort))
	with open(txt, 'rb') as f:
		contenido = f.read()
	# Send the file and then wait for a response 
	save_path = input('Put in which directory you want to save it ----> ')

	if not os.path.exists(save_path):
		print('The directory you chose does not exist. ')
	else:

		print('Sending directory to Server ... ')
		clientSocket.sendto(save_path.encode('utf-8'),(serverName,serverPort))
		
		file_name = input('What name do you want to put in the new file? : ')
		print('Sending file name to server ... ')
		clientSocket.sendto(file_name.encode('utf-8'),(serverName,serverPort))

		
else:
	print('You have not chosen any correct options. Please try again ')



# Print the converted text and then close the socket
#print ('From Server:')
clientSocket.close()
