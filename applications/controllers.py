import os
import sqlite3 
from flask import render_template
from flask import current_app as app
import requests
from flask_login import LoginManager, login_required, logout_user, login_user, current_user
from sqlalchemy import values
from applications.config import *
from applications.models import *

ROLL_NUMBER = '1'
AUTH_TOKEN = 'abcdefghijklmnopqrstuvwxyzABCDEF'
API_ACCESS_CODE = 'VxeuTv'

def  get_trains():
    if not check_roll_number(ROLL_NUMBER):
        return jsonify({'error': 'Roll number used while registering your company does not match your university/college roll number.'})
    response = requests.get('http://127.0.0.1:5000/trains', params={'access_code': API_ACCESS_CODE}, headers={'Authorization': f'Bearer {AUTH_TOKEN}'})
    trains = [train for train in response.json() if train['departure_time'] > 30]
    update_ticket_prices()
    update_seat_availability()
    sorted_trains = sorted(trains, key=lambda x: (x['price'], -x['tickets'], -x['departure_time']))
    delayed_trains = [train for train in response.json() if train['departure_time'] > 30]
    all_trains = sorted_trains + delayed_trains
    
    return jsonify(all_trains)

def update_ticket_prices():
    pass

def seat_available():
    pass

@app.route('/trains', methods=['GET'])
def get_sorted_trains():
    return get_trains()

def check_roll_number(roll_number):
    return roll_number == ROLL_NUMBER

def get_access_code():
    pass

def authenticate():
    pass
