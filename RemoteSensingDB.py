#Gabi Tessier, 7/19/2019
#This creates a database with MongoDB with PyMongo
import pymongo
from bson.objectid import ObjectId
import gridfs
from bson import objectid



#uploadphoto , downloadphoto
class RemSensDB():
    db = None
    fs = None

    #creats the database
    def DataBaseInitialize(self):
        client = pymongo.MongoClient()
        #Creating a client
        self.db = client["database"]

        #storing data
        self.fs = gridfs.GridFS(self.db)

    #inserts data into the database from the json file
    #THIS IS NOT USED TO INSERT PHOTO'S - ONLY DATA****
    def insertData(self, js):
        self.db["raw_images"].insert_many(js)

    #finds the object from a given id (i)
    def findByID(self, i):
        data = False
        try:
            ObjectId(i)
        except Exception as e:
            raise AssertionError("Invalid ID")
        for grid_out in self.fs.find({"_id": ObjectId(i)}):
            data = grid_out.read()

        return data


    #finds the object from a given name (n)
    def findByName(self, n):
        for grid_out in self.fs.find({"filename": n}):
            data = grid_out.read()

        return data

    # store the data in the database. Returns the id of the file in gridFS
    def uploadphoto(self, b, name):
        with open(b, 'rb') as b:
            store = self.fs.put(b, filename = name)
        return store

# create an output file and store the image in the output file
    def downloadphoto(self, a):
        #retrieving data and returning .jpg in bytes
        outputdata = self.fs.get(a).read()
        return outputdata

    def __init__(self):
        self.DataBaseInitialize()
        #self.insertData()

if __name__ == "__main__":
    dbMan = RemSensDB()

    #---------------TEST VARIABLES--------------------#
    na = "image1"
    id = "5d31ceeff814e0b3a9fe59de"
    n = "image1"
    filename = "images/"

    #-------------------METHODS------------------------#

    #++++++++++++DO NOT USE++++++++++++++++#
    #dbMan.insertData(file)
    #dbMan.queryDB(query)
    #dbMan.findByDate(da)

    #+++++++++++USE++++++++++++++++++++++++#
    dbMan.findByName(na)
    dbMan.findByID(id)
    #dbMan.uploadphoto(filename,n)
    #dbMan.downloadphoto(dbMan.uploadphoto(filename))
