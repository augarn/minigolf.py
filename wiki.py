# coding: utf-8
# Author: August Arnoldsson
import os
from bottle import route, run, template, request, static_file, request, redirect
# -*- coding: utf-8 -*-

@route("/")
def list_articles():
    """
    This is the home page, which shows a list of links to all articles
    in the wiki.
    """
    list_of_pages = []
    for files in os.listdir("./wiki/"):
        list_of_pages.append(files)
    return template('index', pages=list_of_pages)

@route('/wiki/<pagename>/')
def show_article(pagename):
    """Displays a single article (loaded from a text file)."""
    webpage = open("./wiki/"+pagename, "r+")
    webpage_content = webpage.read()
    return template('webpage', title=pagename, content=webpage_content) #TODO
    webpage.close()

@route('/create/')
def edit_form():
    """
    Shows a form which allows the user to input a title and content
    for an article. This form should be sent via POST to /update/.
    """
    return template('create') #TODO

@route('/edit/<pagename>/')
def edit_form(pagename):
    """
    Shows a form which allows the user to input a title and content
    for an article. This form should be sent via POST to /update/.
    """ 

    webpage = open("./wiki/"+pagename, "r+")
    webpage_content = webpage.read()
    return template('edit_existing', title=pagename, content=webpage_content) #TODO
    webpage.close()

@route('/update/', method=['POST'])
def update_article():
    """
    Receives page title and contents from a form, and creates/updates a
    text file for that page.
    """
    article_name_received = getattr(request.forms, 'article_name')
    article_content_received = getattr(request.forms, 'article_content')
    
    # 1. --- Create or overwrite file representing article ---
    webpage = open("./wiki/"+article_name_received, "w")
    webpage.write(article_content_received)
    return template('redirect_page', pagename=str(article_name_received))#TODO
    webpage.close()

run(host='localhost', port=23403, debug=True, reloader=True)