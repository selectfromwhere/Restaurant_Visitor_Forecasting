import os
import zipfile

os.chdir("Data/zip/")
files = os.listdir()

for file in files:
    with zipfile.ZipFile(file,'r') as inputFile:
        inputFile.extractall()
