import time
import os, shutil
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
def exceMove():
    files = os.listdir(path)
    files.sort()
#Anzahl der verschobenen Dateien
    print(len(os.listdir(moveto)))
    for f in files:
        shutil.move(path+f,moveto+f)
        print(f)
while True:
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)
