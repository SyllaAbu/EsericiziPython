import flask
from flask import jsonify, request
import sqlite3
# from database import books

app = flask.Flask(__name__)
app.config['DEBUG'] = True


@app.route('/', methods=['GET'])
def home():
    return '<h1>Biblioteca online</h1><p>Prototipo di web API.</p>'


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    all_books = cur.execute('SELECT * FROM Biblioteca;').fetchall()

    conn.close()

    return jsonify(all_books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()

    all_books = cur.execute('SELECT * FROM Biblioteca;').fetchall()

    conn.close()

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id field provided. Please specify  an id.'

    results = []

    for book in all_books:
        print(book)
        if book[0] == id:
            results.append(book)

    return jsonify(results)


app.run()
