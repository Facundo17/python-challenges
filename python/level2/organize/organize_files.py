"""
Create a program that organizes files in a directory into subdirectories based on their file types.

For example, all text files should go into a "Text files" folder, all CSV files into a "Csv files" folder, and so on.

Put all your files in a folder called "files".

The program should create the necessary folders if they do not already exist and move the files into their respective folders.
"""

from pathlib import Path # crear los folders
import glob # recuperar los files
import shutil # para mover files

fileTypes = {"txt" : "Text files","csv" : "Csv files","png" : "Images", "jpg": "Images", "jpeg": "Images", "pdf": "Pdf files"}

filespath = {}

# get files
for x in fileTypes:
    f = glob.glob(f"./files/*.{x}")
    filespath[x] = f

# create folder using pathlib
for i in filespath:
    folder = Path(fileTypes[i])
    folder.mkdir(parents=True, exist_ok=True)
    
    # mover los archivos a la nueva carpeta
    for file in filespath[i]:
        print(file)
        shutil.move(file, folder)