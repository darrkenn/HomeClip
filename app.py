from flask import Flask, render_template, jsonify, request, redirect, abort
import sqlite3


from database.setup_db import setup_db
from routes.linkCrud import addLink_bp, editLink_bp, deleteLink_bp
from routes.linkRetrieve import allLinks_bp, getLinkData_bp, getFilteredTags_bp

app = Flask(__name__)

setup_db()

#Retrieval Functions
app.register_blueprint(allLinks_bp, url_prefix='/api')
app.register_blueprint(getLinkData_bp, url_prefix='/api')
app.register_blueprint(getFilteredTags_bp, url_prefix='/api')

#CRUD Functions
app.register_blueprint(addLink_bp, url_prefix='/api')
app.register_blueprint(editLink_bp, url_prefix='/api')
app.register_blueprint(deleteLink_bp, url_prefix='/api')

@app.route('/')
def hello_world():
    try:
        return render_template("homepage.html")
    except:
        abort(404)

@app.route("/tag/<string:tag>")
def tag(tag):
    conn = sqlite3.connect('links.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM links WHERE tag = ?", (tag,))
    links = cur.fetchall()
    conn.close()
    return jsonify(links)




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
