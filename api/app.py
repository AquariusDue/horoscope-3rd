from flask import Flask
import json

app = Flask(__name__)

# TODO: Data is stored in memory, once the file is updated by the scraper the in-memory api data falls behind
# try route middleware?
with open('../horoscopes.json', 'r') as f:
    horoscopes = json.load(f)


@app.route('/')
def hello_world():
    return horoscopes.get('taur') 
