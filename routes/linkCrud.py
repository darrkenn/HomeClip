import sqlite3

from flask import Blueprint, jsonify, request, redirect

from database.getLinks import final_links

addLink_bp = Blueprint('addLink', __name__)
editLink_bp = Blueprint('editLink', __name__)
deleteLink_bp = Blueprint('deleteLink', __name__)

@addLink_bp.route('/addLink', methods=['POST'])
def add_link():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        tag = request.form['tag']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("INSERT INTO Links VALUES (NULL, ?, ?, ?)", (title, link, tag))
        conn.commit()
        conn.close()
        return redirect("/")
    return None

@editLink_bp.route('/editLink', methods=['POST'])
def edit_link():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        tag = request.form['tag']
        link_id = request.form['id']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("UPDATE Links SET Title = ?, Link = ?, Tag = ? WHERE id = ? ", (title,link,tag,link_id))
        conn.commit()
        conn.close()
        return redirect("/")
    return None

@deleteLink_bp.route('/deleteLink', methods=['POST'])
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