import os, shutil, time, fnmatch
path = "/home/Thanawat/Dokumente/Workspace/python/sdir/"
moveto = "/home/Thanawat/Dokumente/Workspace/python/ddir/"
#moveto2 = "/users/steven/Documents/repos/diashow-txl/images"
count = 0
clear = lambda: os.system('clear')
#pattern muss vom GUI übergeben werden 
pattern = "*.JPG"
#move_or_copy muss vom GUI übergeben werden / 0 == move, 1 == copy
move_or_copy = 1
#costom_time muss vom GUI übergeben werden / 1 == 1 min
costom_min = 1
copied_Files=[]

def exceMove():
    global count
    print(path)
    
    subset_of_im = set(copied_Files)
    files = os.listdir(path)
    files.sort()
    im = fnmatch.filter(os.listdir(path), pattern)
    img = [x for x in im if x not in subset_of_im]
#Anzahl der verschobenen Dateien
    print("moved: "+ str(count) + " files")
    for f in img:
        if move_or_copy == 0:
            shutil.move(path+f,moveto+f)
            count +=1
            print(f)
            time.sleep(0.5)
        else:
            shutil.copy(path+f,moveto+f)
            count +=1
            print(f)
            time.sleep(0.5)
    for c in im:
        if copied_Files.__contains__(c):
            continue
        else:
            copied_Files.append(c)
    print(copied_Files)
while True:
    clear()
    exceMove()
#Zeitintervalle time.sleep(seconds)
#   time.sleep(60*costom_time)    
    time.sleep(2)
    