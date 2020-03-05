import sqlite3 as sql
from datetime import datetime


database_user = "app/databases/users.db" 
database_locations = 'app/databases/locations.db'

def create():
    with sql.connect(database_user) as cur:
        try:
            cur.execute("CREATE TABLE UserDatabase(username VARCHAR2(20), password VARCHAR2(20), realname VARCHAR2(20), gender VARCHAR2(20), dob VARCHAR2(20), height VARCHAR2(20), weight VARCHAR2(20));") 
        except:
            pass

def user_exists(username):
    with sql.connect(database_user) as cur:
        com = f"SELECT count(*) FROM UserDatabase WHERE username='{username}';"
        print(com)
        res = cur.execute(com).fetchone()[0]
        if res == 0:
            return False
        else:
            return True
        
def tid_exists(username):
    with sql.connect(database_locations) as cur:
        com = f"SELECT count(*) FROM Location WHERE tid='{username}';"
        print(com)
        res = cur.execute(com).fetchone()[0]
        if res == 0:
            return False
        else:
            return True
        
def compare(username, value_in, value_type):
    with sql.connect(database_user) as cur:
        com = f"SELECT {value_type} FROM UserDatabase WHERE username='{username}';"
        print(com)
        res = cur.execute(com).fetchone()[0]
        print(f"comparing - {value_in} == {res}")
        if value_in == res:
            return True
        else:
            return False
        
def check_month(month, day):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if (day > 0 and day <= 31):
            return True
        else:
            return False
    elif month == 2:
        if (day > 0 and day <= 28):
            return True
        else:
            return False
    else:
        if (day > 0 and day <= 30):
            return True
        else:
            return False
        
def check_date(day, month, year):
    today = datetime.today().strftime('%Y-%m-%d').split("-")
    if int(year) > int(today[0]):
        return False
    elif int(year) == int(today[0]):
        if int(month) >= int(today[1]):
            return False
        else:
            if int(day) >= int(today[2]):
                return False
            else:
                return check_month(int(today[1]), int(today[2]))
    else:
        return check_month(int(month), int(day))
    