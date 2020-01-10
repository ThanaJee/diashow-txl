import os, shutil,time
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
count = 0
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
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)
