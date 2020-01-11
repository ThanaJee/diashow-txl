import os, shutil, time, fnmatch
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
moveto2 = "/users/steven/Documents/repos/diashow-txl/images"
count = 0
clear = lambda: os.system('clear')
pattern = "*.JPG"
def exceMove():
    global count
    print(path)
    files = os.listdir(path)
    files.sort()
    im = fnmatch.filter(os.listdir(path), pattern)           
#Anzahl der verschobenen Dateien
    print("moved: "+ str(count) + " files")
    for f in im:
        shutil.move(path+f,moveto+f)
        count +=1
        print(f)
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)


