from flask import Flask, render_template,request
import datetime
from pymongo import MongoClient
import certifi

app = Flask(__name__,template_folder="templates")

client = MongoClient("mongodb+srv://Shaiful:saiful2206@entry.ay9oa2w.mongodb.net/",tlsCAFile = certifi.where())
app.db = client.microblog

@app.route("/",methods = ["GET","POST"])
def main():
    if request.method == "POST":
        diary_content = request.form.get("content")
        formatteddate = datetime.datetime.today().strftime("%Y-%m-%d")
        app.db.entries.insert_one({"diary_log":diary_content, "date":formatteddate})

    entries_with_date=[
        (
            entry["diary_log"],
            entry["date"],
            datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in app.db.entries.find({})
    ]
        
    return render_template("home.html",entries = entries_with_date)

