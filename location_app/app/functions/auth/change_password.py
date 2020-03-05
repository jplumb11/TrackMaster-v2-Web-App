import sqlite3 as sql
from app.functions.auth import base


database_user = "app/databases/users.db" 
database_locations = 'app/databases/locations.db'

def change_password(data):
    base.create()
    _status = check_pass_data(data)
    if _status == "success":
        new_password(data)
    return _status
    
def check_pass_data(data):
    _status = check_empty(data)
    if _status == "ok":
        if base.tid_exists(data['username']):
            _date = f"{data['day']}-{data['month']}-{data['year']}"
            if not base.compare(data['username'], _date, "dob"):
                return "wrong_date"
            if not (data['password'] == data['r_password']):
                return "pass_no_match"
            return "success"
        return "no_user"
    else:
        return _status
        

def check_empty(data):
    if data['username'] == "":
        return "empty_id"
    elif data['day'] == "0":
        return "empty_day"
    elif data['month'] == "0":
        return "empty_month"
    elif data['year'] == "0":
        return "empty_year"
    elif data['password'] == "":
        return "empty_pass"
    else:
        return "ok"

def new_password(data):
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    com = f"UPDATE UserDatabase SET password='{data['password']}' WHERE username='{data['username']}';"
    print(com)
    cur.execute(com)
    con.commit()
    cur.close()
    con.close()