from flask import Flask, render_template, abort


from database.setup_db import setup_db
from routes.linkCrud import addLink_bp, editLink_bp, deleteLink_bp, updateLinkClick_bp
from routes.linkRetrieve import (
    allLinks_bp,
    getLinkData_bp,
    getFilteredTags_bp,
    getTagData_bp,
    topFiveClicks_bp, getSearchResults_bp,
)
from routes.search import showResults

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
app.register_blueprint(getTagData_bp, url_prefix="/tags")

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
    try:
        return render_template("search.html")
    except Exception:
        abort(404)
app.register_blueprint(showResults, url_prefix="/search")

@app.route("/folders")
def folders():
    try:
        return render_template("folders.html")
    except Exception:
        abort(404)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
