import sqlite3

from flask import Blueprint, jsonify, request, redirect, render_template

from database.getLinks import final_links

getLinksInTag_bp = Blueprint("getLinksInTags", __name__)


@getLinksInTag_bp.route("/tag=<selectedTag>")
def getLinksInTag(selectedTag):
    conn = sqlite3.connect("links.db")
    c = conn.cursor()
    c.execute(
        "SELECT l.LinkId, l.Title, l.Link, t.Tag, f.Folder FROM Links as l LEFT JOIN main.Tags t on l.TagId = t.TagId LEFT JOIN main.Folders f on f.FolderId = l.FolderId WHERE t.Tag LIKE ?",
        (selectedTag,),
    )
    values = c.fetchall()
    conn.close()
    return render_template("tag.html", links=final_links(values))

