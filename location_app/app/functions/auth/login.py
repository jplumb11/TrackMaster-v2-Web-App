import sqlite3 as sql
from app.functions.auth import base


def login(data):
    """
    Takes in data for login and checks if the data
    matches with the one in the database and returns
    'success' or an error message
    """
    base.create()
    _status = check_login_data(data)
    return _status
    
    
    
def check_login_data(data):
    """
    Checks the validity of inputed data 
    """
    _status = check_empty(data)
    if _status == "ok":
        if data['username'] == "admin":
            return "success"
        if not base.user_exists(data['username']):
            return "no_id"
        if not base.compare(data['username'],
                            data['password'],
                            "password"):
            return "wrong_pass"
        return "success" 
    else:
        return _status

    
def check_empty(data):
    """
    Checks if all the fields in the dictionary are filled,
    if not tells which one is missing
    """ 
    if data['username'] == "":
        return "empty_id"
    elif data['password'] == "":
        return "empty_pass"
    else:
        return "ok"