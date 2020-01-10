import os, shutil, time, fnmatch
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/users/steven/Documents/repos/diashow-txl/images"
count = 0
clear = lambda: os.system('clear')
pattern = "*.JPG"
def exceMove(path):
    global count
    print(path)
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
<<<<<<< HEAD
#    print("moved: "+ str(count) + " files")
#    for f in im:
#        shutil.move(path+f,moveto+f)
#	count += 1
#        print(f)
=======
    print("moved: "+ str(count) + " files")
    for f in im:
        shutil.move(path+f,moveto+f)
        count +=1
        print(f)
>>>>>>> b81aabaf40e1ae0870d7e7ed6bf6196016ee4b78
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)


