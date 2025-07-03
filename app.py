from flask import Flask, render_template, jsonify, request, redirect
import sqlite3

from database.getLinks import final_links
from database.setup_db import setup_db

app = Flask(__name__)

setup_db()

@app.route('/')
def hello_world():
    return render_template("homepage.html")


@app.route('/allLinks', methods=['GET'])
def get_all_links():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Links")
    links = c.fetchall()
    c.close()
    conn.close()
    return jsonify(final_links(links))

@app.route('/addLink', methods=['POST'])
def add_link():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("INSERT INTO Links VALUES (NULL, ?, ?)", (title, link))
        conn.commit()
        conn.close()
        return redirect("/")
    return None

@app.route('/deleteLink', methods=['POST'])
def delete_link():
    if request.method == 'POST':
        link_id = request.form['id']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        print(link_id)
        c.execute("DELETE FROM Links WHERE id = ?", (link_id,))
        conn.commit()
        conn.close()
        return redirect("/")
    return None


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
