import socket
import sys
from sqlite3 import connect


if __name__ == "__main__":
    
    for k in sys.argv: 
        port = sys.argv[1]
        port = int(port)
           #used system args since hard coding port numbers is not efficient
        # string = sys.argv[1]     #sys args saves the input as a variable. so, used type casting. 
        # port = 1238
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname) #this grabs the ip address of the current machine

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((ip,port))
    message = input("Enter first message ")
    message_length = int(message[-1])
    # try: #added exception handling in case of improper ip && port inputs
    #     server.connect((ip,port))
    # except Exception as e: print("Please check the IP Address or the port")
    while message != "t 0" :
        server.send(bytes(message,"utf-8"))
        
        client_conn = server.recv(1024).decode("utf-8")
        print(client_conn)
        string = input("Enter the string ")
        if len(string) == message_length: 
            server.send(bytes(string,"utf-8"))
            zsh = server.recv(1024).decode("utf-8")
            print(zsh)
        elif len(string) != message_length and string == "t 0":
            print("Given string does not match the parameter and or the connection has closed")
            server.close()
    server.close()     



    