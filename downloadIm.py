#Gabi Tessier, 7/19/2019
#this program asks usr for directory path and will insert image and name into database
import RemoteSensingDB as dmain
from PIL import Image
import glob
import os
import pathlib


pathname = input("Enter the path to the directory (ex format: images/): ")

#Setting up path and list for uploading data
path = pathlib.Path(pathname)
file_list = [x for x in path.iterdir() if (x.suffix.lower() == '.jpg')]

#quiry filename and make sure doesnt exist befor inserting
for filename in file_list:
    dmain.RemSensDB().uploadphoto(filename, filename.stem)

print("Files are Successfully uploaded to Database.")
