from geopy.geocoders import Nominatim                   # Imports nominatim API 
import sqlite3 as sql
import json, os, time


database_locations = 'app/databases/locations.db'

def getMsg(msg):
    con = sql.connect(database_locations)               # connecys to db, amkes cursor                      
    cur = con.cursor()
    geolocator = Nominatim(user_agent="Web_app")        # starts nominatim
    try:                                                # Tries SQL to create table
        cur.execute("CREATE TABLE Location(tid VARCHAR2(2), longitude NUMBER(10,6), latitude NUMBER(10,6), city VARCHAR2(20), road VARCHAR2(30), date VARCHAR2(20), time VARCHAR2(20), tst INT(15));") 
    except:
        pass                                                            
    data = json.loads(msg.payload.decode("utf8"))                      
    tid = data["tid"]
    lat = data["lat"]
    lon = data["lon"]
    location = geolocator.reverse(f"{data['lat']},{data['lon']}")
    city = location.raw["address"]["city"]              # Puts data into small array to be used later
    road = location.raw["address"]["road"]
    tst = data["tst"]
    _time = time.strftime('%H:%M:%S', time.localtime(tst))#sets time format
    _date = time.strftime('%d-%m-%Y', time.localtime(tst))
    com = f"INSERT INTO Location values('{tid}','{lon}','{lat}','{city}','{road}','{_date}','{_time}','{tst}');"
    print(com)
    cur.execute(com)
    
    con.commit()                                        # commits changes to db
    cur.close()
    con.close()#                                        # closes connection
    