import sqlite3 as sql
import time


database_user = "app/databases/users.db"   
database_locations = "app/databases/locations.db"   


# user
def get_user_for(username):
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT * FROM UserDatabase WHERE username='{username}';").fetchone()

        
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
    
def get_filtered_data_for_admin():
    all_data = []
    tids = get_all_tids()
    for tid in tids:
        data_city = get_frequency_for('city', tid)
        data_road = get_frequency_for('road', tid)
        data_batt = get_frequency_for('battery', tid)
        all_data.append([tid, data_city, data_road, data_batt])
    return all_data    
    
def get_filtered_data_for(tid):
    data_city = get_frequency_for('city', tid)
    data_road = get_frequency_for('road', tid)
    data_batt = get_frequency_for('battery', tid)
    return [data_city, data_road, data_batt]

        
# main
def get_locations_for(username):
    locations = []
    with sql.connect(database_locations) as cur:
        if username == 'admin':
            res = cur.execute(f"SELECT DISTINCT * From Location ORDER BY tid, date, time;")
        else:
            res = cur.execute(f"SELECT DISTINCT * From Location WHERE tid='{username}' ORDER BY date, time;")
        for tid, batt, lon, lat, city, road, date, time, in res:
            locations.append([tid, batt, lon, lat, city, road, date, time])
    return locations
        
    
# map
def get_map_locations_for(username):
    locations = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT DISTINCT tid, longitude, latitude, date, time From Location WHERE tid='{username}' ORDER BY tid, date, time;")
        for tid, lon, lat, date, time, in res:
            locations.append([tid, lon, lat, date, time])
    return locations

def get_map_location_dates(username):
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT DISTINCT date From Location WHERE tid='{username}' ORDER BY date;")
        date_list = list(map(lambda x: x[0], res))
    return date_list

