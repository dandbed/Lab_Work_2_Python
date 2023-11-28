import datetime
import sqlite3
def get_timestamp(y, m, d):
    return int(datetime.datetime.timestamp(datetime.datetime(y, m, d)))

def get_timestamp_from_string(s):
    t=s.split('-')
    return get_timestamp(int(t[2]), int(t[1]), int(t[0]))

def condition(date):
    data={}
    del_data=[]
    ship_data=[]
    with sqlite3.connect('Lab_Work_2.db') as db:
        db.row_factory = sqlite3.Row
        cursor = db.cursor()
        query = """SELECT name, Sum(deliveries.amount) AS Amount FROM deliveries
                   WHERE delivery_date<= :date GROUP BY name"""
        cursor.execute(query, {"date": date})
        del_data=dict(cursor)
    data=del_data
    with sqlite3.connect('Lab_Work_2.db') as db:
        db.row_factory=sqlite3.Row
        cursor = db.cursor()
        query = """SELECT name, Sum(amount) AS Amount FROM shipments 
                    WHERE shipment_date<= :date GROUP BY name"""
        cursor.execute(query, {'date': date})
        ship_data=dict(cursor)
    for i in ship_data:
        if i in data:
            x=data.get(i)+ship_data.get(i)
            data[i]=x
    return data

def get_table_data(all_data):
    return [(i, all_data.get(i)) for i in all_data]