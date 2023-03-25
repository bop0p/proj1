import os
import shutil

from_dir = "C:/Users/rick_/Downloads"
to_dir = "C:/Users/rick_/Desktop/Download_Images"
ListOfFiles = os.listdir(from_dir)
#print(ListOfFiles)
for file_name in ListOfFiles:
    name, extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == "":
        continue
    if extension in[".csv"]:
        path1 = from_dir + "/"+file_name
        path2 = to_dir + "/"+"image_files"
        path3 = to_dir + "/"+"image_files"+"/"+file_name
        print(path1)
    #check if the folder path exists before moving ele make a new directory then move
        if os.path.exists(path2):
            print("moving"+file_name+"...")

    #move from path 1 to 3
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving"+file_name+"...")
            shutil.move(path1, path3)