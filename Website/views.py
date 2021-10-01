from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        book_name = request.form.get('book_name')
        book_genre = request.form.get('book_genre')
        book_author = request.form.get('book_author')
        book_description = request.form.get('book_description')

        new_note = Note(book_id=book_id, book_name=book_name, book_genre=book_genre, book_author=book_author, book_description=book_description, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Books Information added Successfully!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
