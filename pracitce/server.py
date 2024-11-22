import socket

serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

serverSocket.bind(("127.0.0.1",12345))

serverSocket.listen()

print("Server is listening.....")

while True:
	clientSocket,clientAddress=serverSocket.accept()
	print("Message from client:",clientSocket.recv(1024).decode())
	msg=input("Enter the message back to client:")
	clientSocket.send(msg.encode())
	clientSocket.close()

serverSocket.close()

