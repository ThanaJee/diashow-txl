import os, shutil, time, glob, fnmatch
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
count = 0
clear = lambda: os.system('clear')
pattern = "*.JPG"
def exceMove():
    global count
    files = os.listdir(path)
    files.sort()
    def img(files):
        imgE = ['*.JPG']
        if(files in imgE):
            return True
        else:
            return False
    image = filter(img,files) 

    im = fnmatch.filter(os.listdir(path), pattern)           
#Anzahl der verschobenen Dateien
    print("moved: "+ str(count) + " files")
    for f in im:
        shutil.move(path+f,moveto+f)
	count += 1
        print(f)
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)


