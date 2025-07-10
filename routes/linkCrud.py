import sqlite3

from flask import Blueprint, jsonify, request, redirect

addLink_bp = Blueprint('addLink', __name__)
editLink_bp = Blueprint('editLink', __name__)
deleteLink_bp = Blueprint('deleteLink', __name__)
updateLinkClick_bp = Blueprint('updateLinkClick', __name__)

@addLink_bp.route('/addLink', methods=['POST'])
def add_link():
    if request.method == 'POST':
        title = request.form['title']
        link = request.form['link']
        tag = request.form['tag']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        print("Tag length {}",len(tag))
        print("Tag Value {}", tag)
        if len(tag) > 0:
            c.execute("INSERT OR IGNORE INTO Tags (TagId, Tag)  VALUES (NULL,?)", (tag,))
            c.execute("SELECT TagId From Tags WHERE Tag = ?", (tag,))
            tagId = c.fetchone()[0]
            c.execute("INSERT INTO Links (Title, Link, TagId) VALUES (?, ?, ?) ", (title, link, tagId))
        elif len(tag) == 0:
            c.execute("INSERT INTO Links (Title, Link) VALUES (?,?)", (title, link))

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
        current_url = request.form['url']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        current_url = f'{current_url}'
        if len(tag) > 0:
            c.execute("INSERT OR IGNORE INTO Tags (TagId, Tag)  VALUES (NULL,?)", (tag,))
            c.execute("SELECT TagId From Tags WHERE Tag = ?", (tag,))
            tagId = c.fetchone()[0]
            c.execute("UPDATE Links SET Title = ?, Link = ?, TagId = ? WHERE LinkId = ? ", (title,link,tagId,link_id))
        elif len(tag) == 0:
            c.execute("UPDATE Links SET Title = ?, Link = ?, TagId = NULL WHERE LinkID = ?", (title, link, link_id))
        conn.commit()
        conn.close()
        print(current_url)
        print("im working")
        return redirect(current_url)
    return None

@deleteLink_bp.route('/deleteLink', methods=['POST'])
def delete_link():
    if request.method == 'POST':
        link_id = request.form['id']
        current_url = request.form['url']
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("DELETE FROM Links WHERE LinkId = ?", (link_id,))
        conn.commit()
        conn.close()
        return redirect(current_url)
    return None

@updateLinkClick_bp.route('/updateLinkClick', methods=['POST'])
def update_link_click():
    if request.method == 'POST':
        link_id = request.json.get('id')
        conn = sqlite3.connect('links.db')
        c = conn.cursor()
        c.execute("UPDATE Links SET Clicks = Clicks + 1 WHERE LinkId = ?", (link_id,))
        conn.commit()
        conn.close()
        return jsonify({'success':True})
    return None