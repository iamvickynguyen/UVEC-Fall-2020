import csv
from flask import Flask, request, make_response
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
conn = sqlite3.connect('tinder.db')
c = conn.cursor()

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

c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='profile' ''')

#if the count is 1, then table exists
if c.fetchone()[0]!=1 :
    with open('UVEC-Fall-2020-Seed.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
        for tup in req:
            sqlite_insert_with_param = """INSERT INTO profile
                (firstName,lastName,gender,genderPreference,email,profession,lat,long,city,favoriteAnimal,favoriteMusicGenre,age,smoking,astrologicalSign,highestEducationLevel) 
                VALUES (?, ?, ?, ?, ?);"""

            c.execute(sqlite_insert_with_param, tup)
            conn.commit()


def postData():
    if request.method == 'POST':
        req = json.loads(request.data)['data']


#close the connection
conn.close()

if __name__ == '__main__':
    app.run()