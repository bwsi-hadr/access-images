# Import flask and create an app with it
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Response, send_file
app = Flask(__name__)
from pymongo import MongoClient
client = MongoClient()
import time
from random import Random
import cv2
from RemoteSensingDB import RemSensDB


# Set the directory of the app's webpage
@app.route("/")
def basic():
    data = RemSensDB()
    return "<a href='/random'>hi</a>"

@app.route("/image/<string:id_number>", methods=["GET"])
def getImageById(id_number):
    data = RemSensDB()
    file = findByID(id_number)
    filename = 'images/image{}.jpg'.format(id_number)
    return send_file(filename, mimetype = 'image/jpg')

# @app.route("/imagebydate")
# def getTodayImage():

@app.route("/images", methods=["GET"])
def getImageList():
    data = RemSensDB()
    print("Listing\nImages")
    return "Listing\nImages"


@app.route("/date/<int:date>", methods=["GET"])
def getImageByDate(date):
    data = RemSensDB()
    print(date)
    file = data.findByDate(date)
    return send_file(file, mimetype = 'image/jpg')

@app.route("/random", methods=["GET"])
def getRandomImage():
    data = RemSensDB()
    r = Random()
    randNumber = r.randint(1,5)
    return redirect("../image/{}".format(randNumber))

@app.route("/upload", methods=["POST"])
def uploadImage(img):
    data = RemSensDB()
    pass

def runFlask():
    app.run(port=8383)

# run this code if the file is executed (but not imported)
if __name__ == "__main__":
    runFlask()
