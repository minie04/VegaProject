import orjson
import logging
import sys
from flask import Flask, render_template, request
app = Flask (__name__)

def getDevice (model):
    with open("device.json") as json :
        data = orjson.loads(json.read())
    query = model.upper()
    returnValue = data[query]
    return returnValue


@app.route('/')
def main ():
    return render_template("index.html")


@app.route('/download', methods =  ['POST', 'GET'])
def device ():
    if request.method == "POST":
        try:
            form = request.form
            model = form.get("model")
            json = getDevice(model)
            print (json[0])
            return render_template ("download.html",
                name = json[0]["name"], model = model, image = '',
                binx = json[0]["binx"], pdl = json[0]["pdl"], update = json[0]["update"],
                binxversion = json[0]["versions"][0], pdlversion = json[0]["versions"][1], zipversion = json[0]["versions"][2]
            )
        except (IndexError, KeyError):
            return render_template("deviceNotFound.html")
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)