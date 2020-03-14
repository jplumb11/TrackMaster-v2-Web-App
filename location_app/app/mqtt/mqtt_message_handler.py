from geopy.geocoders import Nominatim
import sqlite3 as sql
import json, os, time


database_locations = 'app/databases/locations.db'


def getMsg(msg):
    """
    Takes in a message from the mqtt and saves the data inside
    a database if one exists, if not creates it
    """
    con = sql.connect(database_locations)                              
    cur = con.cursor()
    geolocator = Nominatim(user_agent = "Trackmaster")
    try:
        cur.execute("""
                     CREATE TABLE Location(tid VARCHAR2(2),
                                           longitude NUMBER(10,6),
                                           latitude NUMBER(10,6),
                                           city VARCHAR2(20), 
                                           road VARCHAR2(30),
                                           date VARCHAR2(20),
                                           time VARCHAR2(20),
                                           tst INT(15));
                    """) 
    except:
        pass 
    data = json.loads(msg.payload.decode("utf8"))                      
    location = geolocator.reverse(f"{data['lat']},{data['lon']}")
    city = location.raw["address"]["city"]
    road = location.raw["address"]["road"]
    tst = data["tst"]
    _time = time.strftime("%H:%M:%S", time.localtime(tst))
    _date = time.strftime("%d-%m-%Y", time.localtime(tst))
    cur.execute(f"""
                  INSERT INTO Location values('{data["tid"]}',
                                              '{data["lon"]}',
                                              '{data["lat"]}',
                                              '{city}',
                                              '{road}',
                                              '{_date}',
                                              '{_time}',
                                              '{tst}');
                 """)
    print(f"{data['tid']} -- {_date} {_time}")
    con.commit()
    cur.close()
    con.close()
    