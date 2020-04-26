from flask import render_template, request, flash, redirect, url_for
from urllib.parse import urlparse
from . import controllers as controller
from app import app
from .forms import SearchForm
from validator_collection import checkers, errors
from urllib.parse import urlsplit
import time


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', form=SearchForm())

@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['search']

        if checkers.is_url(query):
            u = urlsplit(query).netloc
            data = controller.parse_url(query)
            return render_template('analysis.html', org=u, url=query, data=data)
        else:
            flash('not url')
            return redirect('/')
    return redirect('/')
