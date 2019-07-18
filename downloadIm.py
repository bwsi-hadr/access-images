import RemoteSensingDB as dmain
from PIL import Image
import glob
import os
import pathlib

pathname = input("Enter the path to the directory: ")

path = pathlib.Path(pathname)
file_list = [x for x in path.iterdir() if (x.suffix.lower() == '.jpg')]
#print(file_list)
image_list=[]
for filename in file_list:
    im=Image.open(filename)
    image_list.append({"name": filename.stem, "object": im})

#print(image_list)
print("Files are Successfully uploaded to Database.")
