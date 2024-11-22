import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

port=12345
clientSocket.connect(("127.0.0.1",port))
msg=input("Enter the message for client:")

clientSocket.send(msg.encode())
receivedMsg=clientSocket.recv(1024).decode()

print("The received message is:",receivedMsg)

clientSocket.close()

