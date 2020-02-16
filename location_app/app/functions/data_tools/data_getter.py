import sqlite3 as sql
import time


database_user = "app/databases/users.db"   
database_locations = "app/databases/locations.db"   

def get_user_for(username):
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT * FROM UserDatabase WHERE username='{username}';").fetchone()

def get_filtered_data_for(tid):
    data_city = get_frequency_for('city', tid)
    data_road = get_frequency_for('road', tid)
    data_batt = get_frequency_for('battery', tid)
    return [data_city, data_road, data_batt]

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
        
def get_locations():
    locations = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT DISTINCT * From Location ORDER BY tid, timestamp;")
        for tid, batt, lon, lat, city, road, tst, in res:
            rtst = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(tst))
            locations.append([tid, batt, lon, lat, city, road, rtst])
    print(locations)
    return locations
        