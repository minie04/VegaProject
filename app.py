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


@app.route('/download', methods =  ['POST', 'GET' ])
def device ():
    if request.method == "POST":
        try:
            try:
                form = request.form
                model = form.get("model")
                json = getDevice(model)
                print (json, flush=True)
            except (IndexError, KeyError):
                return render_template("deviceNotFound.html")
        except Exception as e:
            print (e, flush=True)
            return "."
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)