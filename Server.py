import socket 
import sys

if __name__ == "__main__":
   
    for k in sys.argv:
    
        port = sys.argv[1]  #used system args since hard coding port numbers is not efficient
        port = int(port)
    
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname) #this grabs the ip address of the current machine
    print("Host: ",ip)
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:                     #added exception handling in case of improper ip && port inputs
        server.bind((ip,port)) #binds the ip address and the port so that it can listen to incoming requests
    except Exception as e:
         print("Please Check The IP Address or the port")
        
    server.listen(3) #server will have a max queue of 3
    client, addr = server.accept()
    def upper():
        string = client.recv(1024).decode("utf-8")
        zsh = string.upper()
        client.send(bytes(zsh,"utf=8"))
    while True:
        message = client.recv(1023).decode("utf-8")
        message_length = int(message[-1])
        if message[0] =="s":
            client_conn = "200 OK: READY"
            client.send(bytes(client_conn,"utf-8"))
            string = client.recv(1024).decode("utf-8")
            if len(string) == message_length:
                zsh = string.upper()
                client.send(bytes(zsh,"utf=8"))
            else:
                print("Given string does not match the parameter")
        else:
            print("Command unknown: Try again")
    client.close()


       