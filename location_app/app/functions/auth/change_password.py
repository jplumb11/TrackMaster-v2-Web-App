import sqlite3 as sql
from app.functions.auth import base


database_user = "app/databases/users.db" 


def change_password(data):  
    """
    Function to allow password change
    """
    base.create()
    _status = check_pass_data(data)
    if _status == "success":
        update_password(data)
    return _status


def check_pass_data(data):   
    """
    Function to check password data is valid
    """
    _status = check_empty(data)
    if _status == "ok":
        if base.tid_exists(data['username']):
            _date = f"{data['day']}-{data['month']}-{data['year']}"
            if not base.compare(data['username'], _date, "dob"):
                return "wrong_date"
            if not (data['password'] == data['r_password']):
                return "pass_no_match"
            return "success"
        return "no_id"
    else:
        return _status
        

        
def check_empty(data):  
    """
    Function to if the fields are empty
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

    
    
def update_password(data):
    """
    Function to update new password in the database 
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