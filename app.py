import orjson
import logging
import sys
from flask import Flask, render_template, request
app = Flask (__name__)

def getDevice (model):
    with open("device.json") as json :
        data = orjson.loads(json)
    returnValue = data[model.upper]
    return returnValue


@app.route('/')
def main () :
    return render_template("index.html")

@app.route('/download', methods = ['POST', 'GET'])
def device () :
    if request.method == "POST":
        try:
            try:
                form = request.form
                model = form.get("model")
                json = getDevice(model)
                sys.stdout.flush(model)
            except (IndexError, KeyError):
                return "."
        except Exception as e:
            error = "{}".format(e)
            return error
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)