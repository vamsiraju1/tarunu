import os
import requests,re 
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, render_template

app = Flask(__name__)
app.config.from_object(__name__)

for file in os.listdir(os.curdir):
	if file.endswith("db"):
		db = file
app.config.update(dict(
	DATABASE=os.path.join(app.root_path, db),
	USER = "sai",
	PASS = "awesome"
	)
)

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/log_in", methods=['POST'])
def log_in():
	if request.method == "POST":
		user = request.form['User']
		password = request.form['password']
		values = dict(UserId=user, password=password, serviceName = "ProntoAuthentication")
		url = "http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://www.msftncsi.com/redirect"
		sai = requests.session()
		p = sai.post(url, values)	
	return check(p)

@app.route("/log_in")
def check(p):	
	if re.findall("Successful", str(p.content)) != None:
		return render_template("login.html", ans=p)	
	else:
		return render_template("index.html")

