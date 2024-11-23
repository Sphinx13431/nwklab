import socket
def decompression(codeValue,myDict):
    result=""
    for i in codeValue:
          result+=myDict.get(int(i))
    return result

def compression(text,length,start,myDict):
        tempDict=dict()
        subStr=""
        i=0
        ls=[]
        while(i<length):
            subStr+=text[i]
            if(subStr in tempDict):
                i+=1
                continue
            else:
                myDict[start]=subStr
                tempDict[subStr]=start
                ls.append(start)
                start=start+1
                subStr=""
            i+=1
        if(subStr!=""):
            ls.append(tempDict.get(subStr))
        
        return ls

def main():
    myDict=dict()
    start=256
    for i in range(start):
        myDict[i]=chr(i)


    serverSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverSocket.bind(('127.0.0.1',12345))
    serverSocket.listen()
    print("server is listening .....")

    while True:
        clientSocket,clientAddress=serverSocket.accept()
        msg=clientSocket.recv(1024).decode().split('.')
        if(msg[1]=='compression'):
            text=msg[0]
            length=len(text)
            result=compression(text,length,start,myDict)
        elif(msg[1]=='decompression'):
            codeValue=msg[1].split(',')
            result=decompression(codeValue,myDict)
        print(result)
main()