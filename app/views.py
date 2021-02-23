# setup application and modules
from app import app
from flask import render_template, flash, redirect, url_for, request

# import config
from config import Config


# error pages
@app.errorhandler(404)
def not_found_error(error):
    # create error message
    errorMessage = '%s (%s)' % (error, request.path)

    # return error page
    return render_template('404.html', title='404 Error'), 404

@app.errorhandler(500)
def internal_error(error):
    # create error message
    errorMessage = '%s (%s)' % (error, request.path)

    # return error page
    return render_template('500.html', title='500 Error'), 500


# home page
@app.route("/")
def home():
    return render_template('home.html',
        title='home')
