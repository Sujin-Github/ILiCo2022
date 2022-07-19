from flask import Flask, render_template, request, redirect, url_for
import sys
import database
application = Flask(__name__)


@application.route("/")
def hello():
    return render_template("main.html")

@application.route("/regist")
def regist():
    return render_template("regist.html")
    
@application.route("/list")
def see_list():
    lost_list = database.load_list()
    print(type(lost_list))
    length = len(lost_list)
    return render_template("list.html", lost_list = lost_list, length = length)

@application.route("/applyphoto")
def apply():
    name = request.args.get("name")
    owner = request.args.get("owner")
    explain = request.args.get("explain")
    upload_id = request.args.get("id")
    
    database.save(name, owner, explain, upload_id)

    return render_template("apply.html")

@application.route("/upload", methods = ["POST"])
def upload():
    uploaded_files = request.files['file']
    uploaded_files.save("static/img/{}.png".format(database.now_index()))
    return redirect(url_for("hello"))

@application.route("/lost_info/<int:index>/")
def info(index):
    lost_info = database.load_lost(index)
    name = lost_info["name"]
    owner = lost_info["owner"]
    expain = lost_info["expain"]
    upload_id = lost_info["upload_id"]
    
    photo = f"img/{index}.png"
    
    return render_template("info.html", name = name, owner = owner, expain = expain, upload_id = upload_id, photo = photo)
    

if __name__ == "__main__":
    application.run(host='0.0.0.0')