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
    def uploadphoto(self, b):
        #storing data
        self.fs = gridfs.GridFS(self.db)

        with open(b, 'rb') as b:
            store = self.fs.put(b)

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
    #-------------------TESTING VERIABLES ----------------------------------------
    json = [
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image1.jpg", "date": "946688580"},
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image2.jpg", "date": "946692180"},
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image3.jpg", "date": "946796400"},
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image4.jpg", "date": "949482000"},
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image5.jpg", "date": "949564800"},
    {"name": "C:/Users/Gabi/Documents/2019-07-12/image6.jpg", "date": "954820800"}
    ]
    query = "Image1.jpg"
    na = 'C:/Users/Gabi/Documents/2019-07-12/Image4.jpg'
    da = '954820800'
    id = '5d28d5aa6c5112c81e28a653'

    #info for uploadphoto()
    filename = "image1.jpg"

    dbMan = RemSensDB()

    #----------METHODS------------------------

    #dbMan.insertData(json)
    #dbMan.queryDB(query)
    #dbMan.findByName(na)
    #dbMan.findByDate(da)
    #dbMan.findByID(id)
    dbMan.uploadphoto(filename)
    #dbMan.downloadphoto(dbMan.uploadphoto(filename))
