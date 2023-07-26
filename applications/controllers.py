import os
import sqlite3 
from flask import render_template
from flask import current_app as app
from applications.config import *
from applications.models import *


@app.route('/trains', methods = ['GET'])
def  trains():
    if not check_roll_number(ROLL_NUMBER):
        return jsonify({'error': 'Roll number used while registering your company does not match your university/college roll number.'})
    response = responnse.get('https://api.example.com/trains')
    trains =     trains = [train for train in response.json() if train['departure_time'] > 30]
    update_ticket_prices()
    update_seat_availability()
    sorted_trains = sorted(trains, key=lambda x: (x['price'], -x['tickets'], -x['departure_time']))
    delayed_trains = [train for train in response.json() if train['departure_time'] > 30]
    all_trains = sorted_trains + delayed_trains
    
    return jsonify(sorted_trains)

def update_ticket_prices():
    pass

def seat_available():
    pass

def get_sorted_trains():
    return trains()

def check_roll_number(roll_number):
    return roll_number == ROLL_NUMBER

def get_access_code():
    pass

def authenticate():
    pass

def get_trains():
    if not check_roll_number(ROLL_NUMBER):
        return jsonify({'error': 'Roll number used while registering your company does not match your university/college roll number.'})