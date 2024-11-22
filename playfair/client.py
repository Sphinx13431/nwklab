import socket

clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

clientSocket.connect(('127.0.0.1',12345))

text=input("Enter the text:")
key=input("Enter the key:")
choice=(input("Enter the choice: Encrypt, Decrypt: "))

message=text+" "+key+" "+choice
clientSocket.send(message.encode())

result=clientSocket.recv(1024).decode()

print(f"The result after {choice}ion is:",result)

clientSocket.close()
