import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1',12345))

plainText=input("Enter the plain text:")
choice=input("Enter the choice 1:encrypt, 2:decrypt-")

msg=plainText+"."+choice

clientSocket.send(msg.encode())

result=clientSocket.recv(1024).decode()

print(f"The result after {choice}ion is:",result)

clientSocket.close()
