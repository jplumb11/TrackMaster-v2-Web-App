import sqlite3 as sql
import time


database_user = "app/databases/users.db"                                    # Grabs the database
database_locations = "app/databases/locations.db"   


# user
def get_user_for(username):                                             
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT username, realname, dob, weight FROM UserDatabase WHERE username='{username}';").fetchone()
        return [res, get_filtered_data_for(username)]                       # Returns required data 
        

        
# freq   
def get_all_tids():
    with sql.connect(database_locations) as cur:
        tids = cur.execute("SELECT DISTINCT tid From Location;")
        tids_list = list(map(lambda x: x[0], tids))
    return tids_list

def get_frequency_for(data_type, tid): 
    with sql.connect(database_locations) as cur:
        data = cur.execute(f"SELECT {data_type} From Location WHERE tid = '{tid}';")
        data_list = list(map(lambda x: x[0], data))
        frequent_data = max(set(data_list), key = data_list.count)
        frequency_data = str(int((data_list.count(frequent_data)/len(data_list)) * 100))
    return [frequent_data, frequency_data]
        
def get_filtered_data_for(tid):
    data_city = get_frequency_for('city', tid)
    data_road = get_frequency_for('road', tid)
    return [data_city, data_road]

        
# main
def get_locations_for(username):
    locations = []
    with sql.connect(database_locations) as cur:
        if username == 'admin':
            res = cur.execute(f"SELECT DISTINCT * From Location ORDER BY tid, tst DESC;")
        else:
            res = cur.execute(f"SELECT DISTINCT * From Location WHERE tid='{username}' ORDER BY tst DESC;")
        for tid, lon, lat, city, road, _date, _time, tst, in res:
            locations.append([tid, lon, lat, city, road, _date, _time])
    return locations
        
    
# map
def get_weight_for(username):
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT weight From UserDatabase WHERE username='{username}';").fetchone()[0]
        return int(res)

def get_map_locations_for(username):
    locations = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT DISTINCT longitude, latitude, date, time From Location WHERE tid='{username}' ORDER BY tst DESC;")
        for lon, lat, _date, _time, in res:
            locations.append([lon, lat, _date, _time])
    return locations

def get_map_location_dates(username):
    date_list = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT DISTINCT date From Location WHERE tid='{username}' ORDER BY tst DESC;")
        for _date, in res:
            date_list.append(_date)
    return date_list

