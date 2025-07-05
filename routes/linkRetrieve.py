import sqlite3

from flask import Blueprint, jsonify, abort, render_template

from database.getLinks import final_links

allLinks_bp = Blueprint('allLinks', __name__)
topFiveClicks_bp = Blueprint('topFiveClicks', __name__)
getLinkData_bp = Blueprint('getLinkData', __name__)
getFilteredTags_bp = Blueprint('getFilteredTags', __name__)
getTagData_bp = Blueprint('getTagData', __name__)
getSearchResults_bp = Blueprint('getSearchResults', __name__)


@allLinks_bp.route('/allLinks')
def all_links():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("SELECT l.LinkId, l.Title, l.Link, t.tag, f.Folder FROM Links as l LEFT JOIN Tags as t on L.TagId = t.TagId LEFT JOIN Folders as f on l.FolderId = f.FolderId")
    links = c.fetchall()
    c.close()
    conn.close()
    return jsonify(final_links(links))

@topFiveClicks_bp.route('/topFiveClicks')
def top_five_clicks():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("SELECT l.LinkId, l.Title, l.Link, t.Tag, l.Clicks FROM Links as l LEFT JOIN Tags as t on L.TagId = t.TagId ORDER BY l.Clicks DESC LIMIT 5")
    links = c.fetchall()
    c.close()
    conn.close()
    return jsonify(final_links(links))

@getLinkData_bp.route('/getLinkData/<int:id>', methods=['GET'])#
def get_link_data(id):
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("SELECT l.LinkId, l.Title, l.Link, t.Tag, f.Folder FROM Links as l LEFT JOIN Tags as t on l.TagId = t.TagId LEFT JOIN Folders as f on l.FolderId = f.FolderId WHERE LinkId = ?", (id,))
    link = c.fetchone()
    c.close()
    conn.close()
    return jsonify(link)

@getFilteredTags_bp.route('/getFilteredTags/', methods=['GET'])
def get_filtered_tags():
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    c.execute("SELECT t.Tag FROM Tags as l LEFT JOIN Tags as t on l.TagId = t.TagId")
    tags = c.fetchall()
    individualTags = []
    for tag in tags:
        if tag not in individualTags:
            individualTags.append(tag)
    return jsonify(individualTags)

@getTagData_bp.route('/<int:tagId>', methods=['GET'])
def tag(tagId):
    try:
        conn = sqlite3.connect('links.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM Links WHERE TagId = ?", (tagId,))
        links = cur.fetchall()
        conn.close()
        return render_template("tag.html", links=final_links(links))
    except:
        abort(404)

@getSearchResults_bp.route('/getSearchResults/title=<title>', methods=['GET'])
def get_search_results_title(title):
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    title = f'{title}%'
    c.execute("SELECT  Title, Link FROM Links  WHERE Title LIKE ?", (title,))
    links = c.fetchall()
    conn.close()
    return jsonify(links)
@getSearchResults_bp.route('/getSearchResults/tag=<selectedTag>', methods=['GET'])
def get_search_results_tag(selectedTag):
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    selectedTag = f'{selectedTag}%'
    c.execute("SELECT Tag From Tags WHERE Tag LIKE ?", (selectedTag,))
    links = c.fetchall()
    conn.close()
    return jsonify(links)
@getSearchResults_bp.route('/getSearchResults/folder=<folder>', methods=['GET'])
def get_search_results_folder(folder):
    conn = sqlite3.connect('links.db')
    c = conn.cursor()
    folder = f'{folder}%'
    c.execute("SELECT Folder From Folders WHERE Folder LIKE ?", (folder,))
    links = c.fetchall()
    conn.close()
    return jsonify(links)

