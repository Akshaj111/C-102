import os
import shutil
source = "C:\Users\akshajaryash\Downloads"
destination = "C:\Users\akshajaryash\Downloads\Images2"
list_of_files = os.listdir(source)
for file_name in list_of_files:
    name,extension = os.path.splitext(file_name)
    
    if extension == "":
        continue
    if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
        path1 = source + '/' + file_name
        path2 = destination + '/' + "image_folder"
        path3 = destination + '/' + "image_folder" + '/' + file_name
        if os.path.exists(path2):
            shutil.move(path1, path3)
        else:
            os.mkdir(path2) 
            shutil.move(path1, path3)