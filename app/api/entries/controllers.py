from flask import Blueprint, request, render_template, \
                  redirect, url_for, jsonify
from app import db
from .models import Entry


mod = Blueprint('entries', __name__, url_prefix='/api/entries')


@mod.route('/')
def show_entries():
    entries = Entry.query.all()
    return jsonify([e.serialize() for e in entries])


@mod.route('/add/', methods=['POST'])
def add_entry():
    entry = Entry(request.form['title'], request.form['text'])
    db.session.add(entry)
    db.session.commit()
    return jsonify(entry.serialize())
