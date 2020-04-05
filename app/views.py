from flask import render_template
from . import controllers as controller
from app import app

@app.route('/')
def index():
	return render_template('index.html')

