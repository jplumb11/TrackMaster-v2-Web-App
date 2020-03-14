import sqlite3 as sql
import time


database_user = "app/databases/users.db"                                    
database_locations = "app/databases/locations.db"   

# user
def get_user_for(username):
    """
    Returns data from the database for the specified username
    """
    with sql.connect(database_user) as cur:
        res = cur.execute(f"""
                            SELECT username, realname, dob, color, weight
                            FROM UserDatabase 
                            WHERE username='{username}';
                           """)
        user_data = res.fetchone()
        return [user_data, get_filtered_data_for(username)]                       

def update_data_for(username, data):
    """
    Updates color and weight for the specified user
    """
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    cur.execute(f"""
                  UPDATE UserDatabase 
                  SET color = '{data['color']}', weight = '{data['weight']}'
                  WHERE username='{username}';
                 """)
    con.commit()
    cur.close()
    con.close()

# freq   
def get_all_tids():
    """
    Returns a list of all unique id's
    """
    with sql.connect(database_locations) as cur:
        tids = cur.execute("""
                            SELECT DISTINCT tid
                            From Location;
                           """)
        tids_list = list(map(lambda x: x[0], tids))
    return tids_list


def get_frequency_for(data_type, tid): 
    """
    Goes through a column and finds a value that is repeating
    the most times and returns it with the percentage
    """
    with sql.connect(database_locations) as cur:
        data = cur.execute(f"""
                             SELECT {data_type} 
                             From Location 
                             WHERE tid = '{tid}';
                            """)
        data_list = list(map(lambda x: x[0], data))
        frequent_data = max(set(data_list), key = data_list.count)
        frequency_data = data_list.count(frequent_data) / len(data_list)
    return [frequent_data, int(frequency_data * 100)]
       
def get_filtered_data_for(tid):
    """
    Gets frequencies for most visited road and city
    """
    data_city = get_frequency_for('city', tid)
    data_road = get_frequency_for('road', tid)
    return [data_city, data_road]

        
# main
def get_locations_for(username):
    """
    Returns a full detailed list of all location entries for
    the specified username, if the username is admin then it
    returns a list of all location entries
    """
    locations = []
    with sql.connect(database_locations) as cur:
        if username == 'admin':
            res = cur.execute(f"""
                                SELECT DISTINCT * 
                                From Location 
                                ORDER BY tid, tst DESC;
                               """)
        else:
            res = cur.execute(f"""
                                SELECT DISTINCT * 
                                From Location
                                WHERE tid='{username}' 
                                ORDER BY tst DESC;
                               """)
        for tid, lon, lat, city, road, _date, _time, tst, in res:
            locations.append([tid, lon, lat, city, road, _date, _time])
    return locations
        
    
# map
def get_weight_for(username):
    """
    Returns weight for the specified username
    """
    with sql.connect(database_user) as cur:
        res = cur.execute(f"""
                            SELECT weight 
                            From UserDatabase 
                            WHERE username='{username}';
                           """)
        _weight = res.fetchone()[0]
        return int(_weight)
    
def get_color_for(username):
    """
    Returns hex code color for the specified username
    """
    with sql.connect(database_user) as cur:
        res = cur.execute(f"""
                            SELECT color
                            From UserDatabase
                            WHERE username='{username}';
                           """)
        _color = res.fetchone()[0]
        return _color

def get_map_locations_for(username):
    """
    Returns a list of all location entries for that username
    and sorts them by date
    """
    locations = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"""
                            SELECT DISTINCT longitude, latitude, date, time 
                            From Location 
                            WHERE tid='{username}' 
                            ORDER BY tst DESC;
                           """)
        for lon, lat, _date, _time, in res:
            locations.append([lon, lat, _date, _time])
    return locations

def get_map_location_dates(username):
    """
    Returns a list of all unique dates from all location entries
    """
    date_list = []
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"""
                            SELECT DISTINCT date 
                            From Location 
                            WHERE tid='{username}'
                            ORDER BY tst DESC;
                           """)
        for _date, in res:
            date_list.append(_date)
    return date_list
