from flask import Flask
import json

app = Flask(__name__)

def get_horoscopes(h_sign):
    with open('../horoscopes.json', 'r') as f:
        horoscopes = json.load(f)
        
        if h_sign in horoscopes:
            return horoscopes.get(h_sign)
        else:
            return "Error: Not a valid astrological sign"

@app.route('/horoscope/<h_sign>')
def send_horoscope(h_sign):
    horoscope = get_horoscopes(h_sign)
    return horoscope

#TODO: Better error-checking, current version is inadequate.
