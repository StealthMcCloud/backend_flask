from flask import Flask
from flask import render_template
from tinydb import TinyDB
import random
app = Flask(__name__)
db = TinyDB('db.json')

@app.route('/')
def index():
    random_recipe = random.choice(db.all())
    return render_template('index.html', item=random_recipe)

if __name__ == "__main__":
    pass