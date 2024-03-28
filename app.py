from flask import Flask, render_template, request， render_template
from textblob import TextBlob

import google.generativeai as palm
palm.configure(api_key="AIzaSyDh2ML6owqHfulsHp8wKGTgHuq4cNjDq-g")
model = {"model":"models/chat-bison-001"}

name = ""
flag=1

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("w10.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    global name,flag
    if flag == 1;
        name = request.form.get("q")
        flag=0
    return(render_template("main.html", r=name))

@app.route("/text",methods=["GET","POST"])
def text():
    return(render_template("text.html"))

@app.route("/text_generator",methods=["GET","POST"])
def text_generator():
    q = request.form.get("q")
    r = plam.chat(**model, messages=q)
    return(render_template("text_generator.html"))


@app.route("/end",methods=["GET","POST"])
def end():
    print("ending process...")
    flag = 1
    return(render_template("index.html"))

if __name__ == "__main__"
