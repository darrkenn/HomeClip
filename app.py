import sqlite3

from flask import Flask, render_template, abort, request, jsonify

from database.setup_db import setup_db
from routes.linkCrud import addLink_bp, editLink_bp, deleteLink_bp, updateLinkClick_bp
from routes.linkRetrieve import (
    allLinks_bp,
    getLinkData_bp,
    getFilteredTags_bp,
    getTagData_bp,
    topFiveClicks_bp, getSearchResults_bp,
)
from routes.tags import getLinksInTag_bp

app = Flask(__name__)

setup_db()

# THIS IS SO STUPID ISTG, but it works!
# Retrieval Functions
app.register_blueprint(allLinks_bp, url_prefix="/api")
app.register_blueprint(topFiveClicks_bp, url_prefix="/api")
app.register_blueprint(getLinkData_bp, url_prefix="/api")
app.register_blueprint(getFilteredTags_bp, url_prefix="/api")
app.register_blueprint(getSearchResults_bp, url_prefix="/api")
# CRUD Functions
app.register_blueprint(addLink_bp, url_prefix="/api")
app.register_blueprint(editLink_bp, url_prefix="/api")
app.register_blueprint(deleteLink_bp, url_prefix="/api")
app.register_blueprint(updateLinkClick_bp, url_prefix="/api")


app.register_blueprint(getLinksInTag_bp, url_prefix="/tags")

@app.route("/")
def home():
    try:
        return render_template("homepage.html")
    except Exception:
        abort(404)


@app.route("/allLinks")
def allLinks():
    try:
        return render_template("allLinksPage.html")
    except Exception:
        abort(404)
@app.route("/search")
def search():
    if not request.args:
        try:
            return render_template("search.html")
        except Exception:
            abort(404)
    else:
        requestType = request.args.get("type")
        if requestType == "title":
            requestValue = request.args.get("title")
            return render_template("search.html", type="title", value=requestValue )
        elif requestType == "tag":
            requestValue = request.args.get("tag")
            return render_template("search.html", type="tag", value=requestValue)
        elif requestType == "folder":
            requestValue = request.args.get("folder")
            return render_template("search.html", type="folder", value=requestValue)
        else:
            return abort(404)


@app.route("/folders")
def folders():
    try:
        return render_template("folders.html")
    except Exception:
        abort(404)

@app.route("/tags")
def tags():
    try:
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("SELECT Tag FROM Tags",)
        tags = c.fetchall()
        tags = [tag[0] for tag in tags]
        conn.close()
        return render_template("tags.html", tags=tags)
    except Exception:
        abort(404)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
