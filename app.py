from flask import Flask, render_template,request
import datetime

app = Flask(__name__,template_folder="templates")

entries = []
@app.route("/",methods = ["GET","POST"])
def main():
    if request.method == "POST":
        diary_content = request.form.get("content")
        formatteddate = datetime.datetime.today().strftime("%Y-%m-%d")
        entries.append((diary_content,formatteddate))

    entries_with_date=[
        (
            entry[0],
            entry[1],
            datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d")
        )
        for entry in entries
    ]
        
    return render_template("home.html",entries = entries_with_date)

