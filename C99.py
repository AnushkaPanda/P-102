import os
import shutil
source = input('Enter source folder ')
destination = input('Enter destination folder ')
source = source + '/'
destination = destination + '/'
fileList = os.listdir(source)
for i in fileList:
    shutil.move((source + i),destination) # move to cut, copy to copy
    print("file moved")

