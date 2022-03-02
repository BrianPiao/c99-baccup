import os
import shutil

s = input("enter Source Folder : ")
d = input("enter Destination Folder : ")

s = s + '/'
d = d + '/'

filelist = os.listdir(s)
for i in filelist: 
    shutil.copy( (s+i) , d )