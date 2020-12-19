from flask import flash, render_template, url_for, redirect, g, send_from_directory, request
from project import app



@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')
