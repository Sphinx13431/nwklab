import socket

def findBogusLetter(myDict,letter):
	for i in range(ord(letter),ord('z')+1,1):
		if(chr(i) in myDict):
			continue
		else:
			return chr(i)



def function(matrix,myDict,key):
	x,y=0,0
	counter=0
	for char in key:
		x=counter//5
		y=counter%5
		matrix[x].append(char)
		myDict[char]=[x,y]
		counter+=1
	bogusLetter=findBogusLetter(myDict,'j')
	for i in range(ord('a'),ord('z')+1,1):
		char=chr(i)
		if(char in myDict or char==bogusLetter):
			continue
		else:
			x=counter//5
			y=counter%5
			matrix[x].append(char)
			myDict[char]=[x,y]
			counter+=1



def main():

	serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

	serverSocket.bind(('127.0.0.1',12345))

	serverSocket.listen()

	print("SOCKET IS LISTENING......")

	while True:
		clientSocket,clientAddress=serverSocket.accept()
		list=clientSocket.recv(1024).decode().split(" ")
		text=list[0]
		key=list[1]
		choice=list[2]
		matrix=[[],[],[],[],[]]
		myDict=dict()
		function(matrix,myDict,key)
		
		print(matrix,"\n",myDict)
		msg="Testing"
		clientSocket.send(msg.encode())
		clientSocket.close()
	serverSocket.close()
main()
