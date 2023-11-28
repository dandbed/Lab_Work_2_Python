import datetime
import sqlite3
def get_timestamp(y, m, d):
    return int(datetime.datetime.timestamp(datetime.datetime(y, m, d)))

def get_timestamp_from_string(s):
    t=s.split('-')
    return get_timestamp(int(t[2]), int(t[1]), int(t[0]))

def checking_conditions(c, s_d, e_d):
    data = []
    with sqlite3.connect('Lab_Work_2.db') as db:
        cursor = db.cursor()
        query = """SELECT deliveries.id, deliveries.name, deliveries.delivery_date, deliveries.amount, deliveries.provider 
                   FROM deliveries 
                   JOIN items
                   WHERE items.category= :category 
                   AND items.name=deliveries.name 
                   AND deliveries.delivery_date BETWEEN :start_date AND :end_date"""
        cursor.execute(query, {"category": c, "start_date": s_d, "end_date": e_d})
        data=cursor
    return data