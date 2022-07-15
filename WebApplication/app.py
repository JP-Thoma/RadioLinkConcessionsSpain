# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:37:59 2022

@author: jthoma
"""

from flask import Flask,render_template


app = Flask(__name__,template_folder="templates")

@app.route("/")
#@app.route("/home")
def home():
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)