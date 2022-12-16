from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'bA5qzruPYLAyyx5QFNUVCg223eddksnlkd8d0uudij'

from application.routes import routes