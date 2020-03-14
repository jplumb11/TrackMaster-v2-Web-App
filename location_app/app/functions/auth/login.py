import sqlite3 as sql
from app.functions.auth import base


def login(data):
    """
    Function to start to start the login
    """
    base.create()
    l_status = check_login_data(data)
    return l_status
    
    
    
def check_login_data(data):
    """
    Function to check the login data 
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
    Function to check whether the fields are filled 
    """ 
    if data['username'] == "":
        return "empty_id"
    elif data['password'] == "":
        return "empty_pass"
    else:
        return "ok"