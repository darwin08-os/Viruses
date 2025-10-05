import socket
import argparse


# create argument parser object
parser = argparse.ArgumentParser(description="this is client program to connect to the server")
parser.add_argument("-i","--ip",required=True,help="this takes ip address")
parser.add_argument("-p","--port",required=True,type=int,help="this is port number")

args = parser.parse_args()


host = args.ip
port = args.port


invalids = ["python","python "]

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((host,port))
connection = server.recv(1024).decode()
print(connection)
try:
    while True:
        try:
            command = input("")
            if command in invalids:
                print("invalid command")
                continue
            if command.lower() == "exit":
                server.sendall("exit".encode())
                break
            if len(command)>0:
                server.sendall(command.encode())
                size = int(server.recv(2048).decode())        
                if size < 10:
                    output = server.recv(10).decode()
                else:
                    output = ""
                    iterations = size//10
                    for i in range(0,iterations):
                        output += server.recv(10).decode()
                    if size%10 != 0:
                        output += server.recv(10).decode()
                print(output,end="")
        except KeyboardInterrupt as k:
            print(k)
            continue
except:
    server.sendall("exit".encode())
    server.close()
