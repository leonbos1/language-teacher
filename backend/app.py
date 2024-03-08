from flask import Flask
from routes.words import words_bp

app = Flask(__name__)

app.register_blueprint(words_bp, url_prefix='/words')

if __name__ == '__main__':
    app.run(debug=True)
