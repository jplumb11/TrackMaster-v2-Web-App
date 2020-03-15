import sqlite3 as sql
from app.functions.auth import base
import re


database_user = "app/databases/users.db" 


def change_password(data):  
    """
    Takes in data for password change and checks if
    data matches the one in the database, then
    returns 'success' or an error message
    """
    base.create()
    _status = check_pass_data(data)
    if _status == "success":
        update_password(data)
    return _status

def check_pass_data(data):   
    """
    Compares dates of birth and if the new passwords match,
    then returns 'success' or an error message
    """
    _status = check_empty(data)
    if _status == "ok":
        if base.tid_exists(data['username']):
            _date = f"{data['day']}-{data['month']}-{data['year']}"
            if not base.compare(data['username'], _date, "dob"):
                return "wrong_date"
            if not (data['password'] == data['r_password']):
                return "pass_no_match"
            pass_status = is_pass_valid(data['password'])
            if pass_status != "ok":
                return pass_status
            return "success"
        return "no_id"
    else:
        return _status
        
def check_empty(data):  
    """
    Checks if all the fields in the dictionary are filled,
    if not tells which one is missing
    """
    if data['username'] == "":
        return "empty_id"
    elif data['day'] == "0":
        return "empty_bday"
    elif data['month'] == "0":
        return "empty_bday"
    elif data['year'] == "0":
        return "empty_bday"
    elif data['password'] == "":
        return "empty_pass"
    elif data['password'] == "":
        return "empty_rpass"
    else:
        return "ok"

def is_pass_valid(password):
    """
    Checks if the user inputted password matches all
    the criteria
    """
    if len(password) < 5: 
        return "too_short"
    elif len(password) > 15:
        return "too_long"
    elif not re.search("[A-Z]", password):
        return "no_up"
    elif not re.search("[a-z]", password):
        return "no_low"
    elif not re.search("[0-9]", password):
        return "no_num"
    elif not re.search("[^a-zA-Z0-9_]", password):
        return "no_sym"
    else:
        return "ok"   
    
def update_password(data):
    """
    Updates the password for the user
    """
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    cur.execute(f"""
                  UPDATE UserDatabase 
                  SET password='{data['password']}' 
                  WHERE username='{data['username']}';
                 """)
    con.commit()
    cur.close()
    con.close()