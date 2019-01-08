# coding: utf-8
# Author: August Arnoldsson

from bottle import route, run, template, request

@route("/")
def list_articles():
    """
    This is the home page, which shows a list of links to all articles
    in the wiki.
    """
    return "Hello World!" # TODO

@route('/wiki/<pagename>/')
def show_article(pagename):
    """Displays a single article (loaded from a text file)."""
    pass # TODO

@route('/edit/')
def edit_form():
    """
    Shows a form which allows the user to input a title and content
    for an article. This form should be sent via POST to /update/.
    """
    pass #TODO

@route('/update/', method="POST")
def update_article():
    """
    Receives page title and contents from a form, and creates/updates a
    text file for that page.
    """
    pass #TODO


run(host='localhost', port=8080, debug=True, reloader=True)