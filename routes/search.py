from flask import Blueprint, render_template, abort


showResults = Blueprint('showResults', __name__)
@showResults.route('/tag=<selectedTag>')
def showTag(selectedTag):
    try:
        return render_template("tags.html", selectedTag=selectedTag)
    except Exception:
        abort(404)

@showResults.route('/title=<selectedTitle>')
def showTitle(selectedTitle):
    return selectedTitle