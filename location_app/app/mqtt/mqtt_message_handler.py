from geopy.geocoders import Nominatim
import sqlite3 as sql
import json, os, time


database_locations = 'app/databases/locations.db'

def getMsg(msg):
    con = sql.connect(database_locations)                                   
    cur = con.cursor()
    geolocator = Nominatim(user_agent="Web_app")
    try:
        cur.execute("CREATE TABLE Location(tid VARCHAR2(2), battery INT(3), longitude NUMBER(10,6), latitude NUMBER(10,6), city VARCHAR2(20), road VARCHAR2(30), date VARCHAR2(15), time VARCHAR2(15));") 
    except:
        pass                                                            
    data = json.loads(msg.payload.decode("utf8"))                       
    tid = data["tid"]
    batt = data["batt"]
    lat = data["lat"]
    lon = data["lon"]
    location = geolocator.reverse(f"{data['lat']},{data['lon']}")
    city = location.raw["address"]["city"]
    road = location.raw["address"]["road"]
    rtst = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(data["tst"])).split(" ")
    
    print(rtst, ' ---- ', tid)
    
    cur.execute(f"INSERT INTO Location values('{tid}','{batt}','{lon}','{lat}','{city}','{road}','{rtst[0]}','{rtst[1]}');")
    
    con.commit()
    cur.close()
    con.close()
    