import os
import shutil
source = "C:\\Users\\miche\\Downloads"
destination = "C:\\Users\\miche\\Downloads\\C102_assets-main"
fileList = os.listdir(source)
#print (fileList)
for fileName in fileList:
    name, extension = os.path.splitext(fileName)
    if extension=="":
        continue
    if extension in [".png",".jpg",".jpeg",".gif",".jfif"]:
        path1 =source + "/"+ fileName
        path2 = destination + "/"+ "image_files"
        path3 = destination + "/"+ "image_files"+ "/"+ fileName

        if os.path.exists(path2):
            print("moving" + fileName)
            shutil.move(path1, path3)
        else:
            os.makedirs(path2)
            print("moving" + fileName)
            shutil.move(path1, path3)