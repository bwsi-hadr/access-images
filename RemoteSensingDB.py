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
        #print(client.list_database_names())

    #inserts data into the database from the json file
    def insertData(self, js):
        self.db["raw_images"].insert_many(js)

    #finds the object from a given id
    def findByID(self, i):
        o = self.db["raw_images"].find_one({"_id": ObjectId(i)})
        #print(o)

    #finds the object from a given name
    def findByName(self, n):
        j = self.db["raw_images"].find_one({"name": n})
        print(j)

    #find the object from a given date
    def findByDate(self, d):
        b = self.db["raw_images"].find_one({"date": d})
        #print(b)

    # store the data in the database. Returns the id of the file in gridFS
    def uploadphoto(self, b, name):
        #storing data
        self.fs = gridfs.GridFS(self.db)
        #print(name)
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

    #-------------------METHODS------------------------#

    dbMan.insertData(file)
    dbMan.queryDB(query)
    dbMan.findByName(na)
    dbMan.findByDate(da)
    dbMan.findByID(id)
    dbMan.uploadphoto(filename)
    dbMan.downloadphoto(dbMan.uploadphoto(filename))
