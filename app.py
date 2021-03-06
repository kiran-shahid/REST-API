import os
from flask import Flask, jsonify, request, json,render_template, url_for

app = Flask(__name__)


data = [
  {
    "country": "England",
    "team-matches-played": 746,
    "matches-won": 375,
    "matches-lost": 334
  },
  {
    "country": "Australia",
    "team-matches-played": 949,
    "matches-won": 575,
    "matches-lost": 331
  },
  {
    "country": "South Africa",
    "team-matches-played": 625,
    "matches-won": 385,
    "matches-lost": 216
  },
  {
    "country": "West Indies",
    "team-matches-played": 822,
    "matches-won": 401,
    "matches-lost": 381
  },
  {
    "country": "New Zealand",
    "team-matches-played": 772,
    "matches-won": 351,
    "matches-lost": 374
  },
  {
    "country": "India",
    "team-matches-played": 987,
    "matches-won": 513,
    "matches-lost": 424
  },
  {
    "country": "Pakistan",
    "team-matches-played": 927,
    "matches-won": 486,
    "matches-lost": 413
  },
  {
    "country": "Sri Lanka",
    "team-matches-played": 852,
    "matches-won": 389,
    "matches-lost": 421
  },
  {
    "country": "Zimbabwe",
    "team-matches-played": 529,
    "matches-won": 138,
    "matches-lost": 373
  },
  {
    "country": "Bermuda",
    "team-matches-played": 35,
    "matches-won": 7,
    "matches-lost": 28
  },
  {
    "country": "Netherlands",
    "team-matches-played": 80,
    "matches-won": 31,
    "matches-lost": 45
  },
  {
    "country": "Bangladesh",
    "team-matches-played": 376,
    "matches-won": 128,
    "matches-lost": 241
  },
  {
    "country": "Kenya",
    "team-matches-played": 154,
    "matches-won": 42,
    "matches-lost": 107
  },
  {
    "country": "Namibia",
    "team-matches-played": 14,
    "matches-won": 5,
    "matches-lost": 9
  },
  {
    "country": "Ireland",
    "team-matches-played": 156,
    "matches-won": 67,
    "matches-lost": 78
  },
  {
    "country": "Scotland",
    "team-matches-played": 115,
    "matches-won": 42,
    "matches-lost": 66
  },
  {
    "country": "Afghanistan",
    "team-matches-played": 126,
    "matches-won": 59,
    "matches-lost": 63
  }
]
@app.route('/')

def index():
    return 'API for querying static data'

@app.route('/data', methods = ['GET'])
def list():
    return jsonify({'data': data})

# @app.route('/data/<string:country>', methods=['GET'])
# def single(country):
#     # country = json.loads(str)
#     return jsonify({'data':data[country]})
@app.route('/fetch', methods=['GET'])
def single():
    country = [x for x in data if x['country'] == 'Scotland' ]
    return jsonify({'country':country})

@app.route('/sort', methods = ['GET'])
def sort():
    order = sorted(data, key=lambda data:data['matches-won'], reverse = True)  
    return jsonify({'order':order})
    
@app.route('/filter', methods=['GET'])
def filter():
  #  y = json.loads(data)
  #  filtered = [x for x in data if x['matches-lost'] == 63 & x['matches-won'] == 59]
   filtered = [x for x in data if x['matches-won'] >= 500 ] 
   return jsonify({'filtered':filtered})

    


if __name__ == "__main__":
    app.run(debug=True)