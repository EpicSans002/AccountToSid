import amino
import json
import urllib.request
from flask import Flask, jsonify, request, render_template
import random
import os



client = amino.Client()
def SID(self, email: str, password: str, device: str):
   client=amino.Client(deviceId=device)
   email=email
   password=password
   client.login(email,password)
   SID = client.sid
   return SID

app = Flask(__name__)

@app.route("/")
def home():
  return render_template("my-form.html")

@app.route("/", methods=['POST'])
def home_post():
  email= request.form['email']
  password= request.form['password']
  device= request.form['device']
  convert= SID(email=email, password=password, device=device”)
  format = {"sid": f'{convert}'}
  web = jsonify(format)
  return web

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)
