from flask import Flask, jsonify
import json

app = Flask(__name__)

# Define a custom Exception inherited from KeyError
class HoroscopeKeyError(KeyError):
    pass

# Read the whole horoscope data, check if the requested horoscope exists and return only the specific horoscope
def get_horoscopes(h_sign):
    with open('../horoscopes.json', 'r') as f:
        horoscopes = json.load(f)

        if h_sign in horoscopes:
            return {
                "sign": h_sign,
                "text": horoscopes.get(h_sign)
            }
        else:
            raise HoroscopeKeyError("Invalid astrological sign") 

# Flask error handler
@app.errorhandler(HoroscopeKeyError)
def handle_invalid_sign(error):
    response = {
        "status_code": 400,
        "error": repr(error),
        "message": "No such astrological sign",
        "detail": "Ensure there are no typos or missing letters in the sign name"
        }
    return jsonify(response), 400 

# Route to retrieve the requested horoscope based on h_sign e.g. berbec, rac, sagetator
@app.route('/horoscope/<h_sign>')
def send_horoscope(h_sign):
    horoscope = get_horoscopes(h_sign)
    return jsonify(horoscope)
