import csv
import sqlite3
import json
from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
conn = sqlite3.connect('tinder.db')
c = conn.cursor()

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='profile' ''')

#if the count is 1, then table exists
if c.fetchone()[0]!=1 :
    # Create table
    c.execute('''CREATE TABLE IF NOT EXISTS profile
        (firstName text,
        lastName text,
        gender text,
        genderPreference text,
        email text,
        profession text,
        lat real,
        long real,
        city text,
        favoriteAnimal text,
        favoriteMusicGenre text,
        age int,
        smoking text,
        astrologicalSign text,
        highestEducationLevel text)''')

    with open('UVEC-Fall-2020-Seed.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                sqlite_insert_with_param = """INSERT INTO profile
                    (firstName,lastName,gender,genderPreference,email,profession,lat,long,city,favoriteAnimal,favoriteMusicGenre,age,smoking,astrologicalSign,highestEducationLevel) 
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""

                c.execute(sqlite_insert_with_param, (row))
                conn.commit()
            line_count += 1

@app.route('/postEmail', methods=['GET', 'POST'])
def postEmail():
    if request.method == 'POST':
        data = json.loads(request.data)['email']
        with sqlite3.connect("tinder.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM profile WHERE email=?", (data,))
            rows = c.fetchall()

            if len(rows) == 0:
                return make_response({'data': None}, 400)
            
            responses = getMatch(parseDict(rows[0]), c)
            return make_response({'data': responses}, 200)
        return make_response({'data': None}, 400)

def getMatch(data, c):
    if data['genderPreference'] != 'anybody':
        c.execute("SELECT * FROM profile WHERE gender=?", (data['genderPreference'],))
        rows = c.fetchall()
        return rows

# easy to get
def parseDict(data):
    keys = ['firstName','lastName','gender','genderPreference','email','profession','lat','long','city','favoriteAnimal','favoriteMusicGenre','age','smoking','astrologicalSign','highestEducationLevel']
    dict = {}
    for i in range(len(data)):
        dict[keys[i]] = data[i]
    return dict

#close the connection
conn.close()

if __name__ == '__main__':
    app.run()