import socket

def main():
    
    while True:
        clientSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        clientSocket.connect(('127.0.0.1',12345))
        msg=""
        choice=int(input("Enter choice-1:Compression, 2:Decompression ->"))
        if(choice==1):
            print("Compression\n")
            text=input("Enter the text to be compressed:")
            msg+=text+"."+"compression"
        elif(choice==2):
            print("\nDecompression")
            code=input("Enter the compressed code:")
            msg+=code+"."+"decompression"
        else:
            print("Invalid choice")
            continue
        clientSocket.send(msg.encode())
        clientSocket.close()

main()