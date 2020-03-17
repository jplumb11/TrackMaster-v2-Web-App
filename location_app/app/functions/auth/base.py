import sqlite3 as sql
from datetime import datetime


database_user = "app/databases/users.db"
database_locations = "app/databases/locations.db"


def create():
    """
    Creates a user database if it doesn't exist
    """
    with sql.connect(database_user) as cur:
        try:
            cur.execute("""
                         CREATE TABLE UserDatabase(username VARCHAR2(20),
                                                   password VARCHAR2(20),
                                                   realname VARCHAR2(20), 
                                                   dob VARCHAR2(20),
                                                   color VARCHAR2(20),
                                                   weight VARCHAR2(20));
                        """) 
        except:
            pass
        
def user_exists(username):      
    """
    Returns true or false depending on if the user exists
    """
    with sql.connect(database_user) as cur:
        res = cur.execute(f"""
                            SELECT count(*) 
                            FROM UserDatabase 
                            WHERE username='{username}';
                           """)
        if res.fetchone()[0] == 0: 
            return False
        else:
            return True
        
def tid_exists(username):           
    """
    Returns true or false depending on if there is any data
    for that username in the database
    """        
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"""
                            SELECT count(*) 
                            FROM Location 
                            WHERE tid='{username}';
                           """)
        if res.fetchone()[0] == 0:
            return False
        else:
            return True
        
def compare(username, value_in, value_type):
    """
    Takes in username, value and type and checks if they match with 
    the ones already saved in the database
    """
    with sql.connect(database_user) as cur:
        res = cur.execute(f"""
                            SELECT {value_type} 
                            FROM UserDatabase 
                            WHERE username='{username}';
                           """)
        if value_in == res.fetchone()[0]:
            return True
        else:
            return False

def check_month(month, day):
    """
    Takes in month and day and checks if the day
    is valid for that month
    Doesn't take in account leap years
    """       
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if (day > 0 and day <= 31):
            return True
        else:
            return False
    #February
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
    """
    Takes in a date and checks if it's in the future and then calls
    check_month to see if the month/day are valid
    """    
    today = datetime.today().strftime('%Y-%m-%d').split("-")
    if int(year) > int(today[0]):
        return False
    elif int(year) == int(today[0]):
        if int(month) > int(today[1]):
            return False
        else:
            if int(day) > int(today[2]):
                return False
            else:
                return check_month(int(month), int(day))
    else:
        return check_month(int(month), int(day))
    