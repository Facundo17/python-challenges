from pathlib import Path # crear los folders
import glob # recuperar los files
import shutil # para mover files

fileTypes = {"txt" : "Text files","csv" : "Csv files","jpg" : "Images"}

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