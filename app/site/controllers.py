from flask import Blueprint, render_template


mod = Blueprint('site', __name__)


@mod.route('/')
def show_index():
    return render_template('layout.html')
