import os, shutil,time
path = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
count = 0
clear = lambda: os.system('clear')
def exceMove():
    global count
    files = os.listdir(path)
    files.sort()
#Anzahl der verschobenen Dateien
    print("moved: "+ str(count) + " files")
    for f in files:
        shutil.move(path+f,moveto+f)
	count += 1
        print(f)
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)
