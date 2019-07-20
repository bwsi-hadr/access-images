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
        self.db = client["database"]

        #storing data
        self.fs = gridfs.GridFS(self.db)
        #print(client.list_database_names())

    #inserts data into the database from the json file
    def insertData(self, js):
        self.db["raw_images"].insert_many(js)

    #finds the object from a given id
    def findByID(self, i):
        #o = self.db["raw_images"].find_one({"_id": ObjectId(i)})
        #print(o)
        o = False
        try:
            ObjectId(i)
        except Exception as e:
            raise AssertionError("Invalid ID")
        for grid_out in self.fs.find({"_id": ObjectId(i)}):
            o = grid_out.read()

        #print("id+++++ ", o)
        return o


    #finds the object from a given name
    def findByName(self, n):
        #j = self.db["raw_images"].find_one({"name": n})
        #print(j)
        data=False
        for grid_out in self.fs.find({"filename": n}):
            data = grid_out.read()

        return data


    #find the object from a given date
    def findByDate(self, d):
        #b = self.db["raw_images"].find_one({"date": d})
        #print(b)
        pass

    # store the data in the database. Returns the id of the file in gridFS
    def uploadphoto(self, b, name):
        #print(name)
        store = False
        with open(b, 'rb') as b:
            store = self.fs.put(b, filename = name)
        #print("store:   ", store)
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
