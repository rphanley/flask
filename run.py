import os
import json
from flask import Flask, render_template

app = Flask(__name__)

#     app.run(host=os.environ.get("IP"),port=int(os.environ.get("PORT")),debug=True)
# app.run(debug=True)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    data = []
    with open("data/company.json","r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", list_of_numbers=[1,2,3],company=data)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")


if __name__ == "__main__":
     app.run(debug=True)

     
    