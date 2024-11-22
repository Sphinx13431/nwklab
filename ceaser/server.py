import socket


def encrypt(text):
	result=""
	for i in text:
		if(i in ['x','y','z','X','Y','Z']):
			result=result+chr(ord(i)-23)
		else:
			result+=chr(ord(i)+3)
	return result

def decrypt(text):
	result=""
	for i in text:
		if(i in ['a','b','c','A','B','C']):
			result=result+chr(ord(i)+23)

		else:
			result+=chr(ord(i)-3)
	return result






serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(('127.0.0.1',12345))

serverSocket.listen()

print("Socket is listening...")

while True:
	clientSocket,clientAddress=serverSocket.accept()
	ls=clientSocket.recv(1024).decode().split('.')
	msg=ls[0]
	choice=ls[1]
	if(choice.lower() == 'encrypt'):
		result=encrypt(msg)
	else:
		result=decrypt(msg)
	clientSocket.send(result.encode())
	clientSocket.close()

serverSocket.close()
