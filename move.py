import os, shutil, time, fnmatch
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
#moveto2 = "/users/steven/Documents/repos/diashow-txl/images"
count = 0
clear = lambda: os.system('clear')
pattern = "*.JPG"
#move_or_copy muss im GUI übergeben werden / 0 == move, 1 == copy
move_or_copy = 1
copied_Files=[]

def exceMove():
    global count
    print(path)
    print(copied_Files)
    files = os.listdir(path)
    files.sort()
    im = fnmatch.filter(os.listdir(path), pattern)
    print(im)
#Anzahl der verschobenen Dateien
    print("moved: "+ str(count) + " files")
    for f in im:
        if move_or_copy == 0:
            shutil.move(path+f,moveto+f)
            count +=1
            print(f)
            #time.sleep(0.5)
        else:
            shutil.copy(path+f,moveto+f)
            count +=1
            print(f)
            #time.sleep(0.5)
    copied_Files.append(im)
    #print(copied_Files)
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)    
    time.sleep(2)



