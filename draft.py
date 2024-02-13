#!/usr/bin/python3
import requests
from datetime import datetime
from collections import defaultdict


from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def diseaseoutbreaknews():
    response = requests.get('https://www.who.int/api/news/diseaseoutbreaknews')
    data = response.json()

    
    items = []
    for item in response.json()['value']:
        date_created = datetime.strptime(item['DateCreated'], "%Y-%m-%dT%H:%M:%SZ")
        items.append(item['Title'])
    return jsonify({'items': items})

if __name__ == '__main__':
    app.run(debug=True)