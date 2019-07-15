import pymongo
from bson.objectid import ObjectId
import gridfs
from bson import objectid

#uploadphoto , downloadphoto
class RemSensDB():
    db = None

    #creates the database
    def DataBaseInitialize(self):
        client = pymongo.MongoClient()
        self.db = client["database"]
        #print(client.list_database_names())

    #inserts data into the database from the json file
    def insertData(self, js):
        self.db["raw_images"].insert_many(js)
        return 0

    #finds the object from a given id
    def findByID(self, i):
        o = self.db["raw_images"].find_one({"_id": ObjectId(i)})
        return o

    #finds the object from a given name
    def findByName(self, n):
        j = self.db["raw_images"].find_one({"name": n})
        return o

    #find the object from a given date
    def findByDate(self, d):
        b = self.db["raw_images"].find_one({"date": d})
        return b

    def uploadphoto(self, b):

        fs = gridfs.GridFS(self.db)

        with open(b, 'rb') as b:
            store = fs.put(b)

        outputdata = fs.get(store).read()
        #print(outputdata)
        return outputdata


    def downloadphoto(self):
        pass



    def __init__(self):
        self.DataBaseInitialize()
        #self.insertData()

if __name__ == "__main__":
    json = [
    {"name": "images/image1.jpg", "date": "946688580"},
    {"name": "images/image2.jpg", "date": "946692180"},
    {"name": "images/image3.jpg", "date": "946796400"},
    {"name": "images/image4.jpg", "date": "949482000"},
    {"name": "images/image5.jpg", "date": "949564800"},
    {"name": "images/image6.jpg", "date": "954820800"}
    ]
    query = "Image1.jpg"
    na = 'images/image4.jpg'
    da = '954820800'
    id = '5d28d5aa6c5112c81e28a653'

    #info for uploadphoto()
    filename = "images/image1.jpg"

    dbMan = RemSensDB()
    #dbMan.insertData(json)
    #dbMan.queryDB(query)
    #dbMan.findByName(na)
    #dbMan.findByDate(da)
    #dbMan.findByID(id)
    #dbMan.uploadphoto(filename)
    dbMan.downloadphoto(filename)
