from flask import Blueprint, jsonify, request
from flask_restful import marshal_with, fields
from extensions import db

from models.word import Word, word_fields

words_bp = Blueprint('words', __name__)


@words_bp.route('/', methods=['GET'])
@marshal_with(word_fields)
def get_words():
    words = Word.query.all()
    return words


@words_bp.route('/', methods=['POST'])
@marshal_with(word_fields)
def create_word():
    data = request.get_json()
    word = Word(data['english'], data['italian'], data['dutch'])
    db.session.add(word)
    db.session.commit()
    return word, 201


@words_bp.route('/<int:word_id>', methods=['GET'])
@marshal_with(word_fields)
def get_word(word_id):
    word = Word.query.get(word_id)
    return word


@words_bp.route('/<int:word_id>', methods=['PUT'])
@marshal_with(word_fields)
def update_word(word_id):
    word = Word.query.get(word_id)
    data = request.get_json()
    word.english = data['english']
    word.italian = data['italian']
    word.dutch = data['dutch']
    db.session.commit()
    return word
