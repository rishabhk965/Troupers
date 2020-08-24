from flask import render_template
from flask_login import login_required
from .import admin

@admin.route('/')
def app():
    return render_template("Welcome")