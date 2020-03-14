import sqlite3 as sql                                                       
from app.functions.auth import base


database_user = "app/databases/users.db" 
 
    
def create_profile(data):                                                   
    """
    Takes in data for account creation and checks if
    the account can be made and then calls a function
    to create the account 
    Returns 'success' or an error message on failure
    """
    base.create()
    _status = check_prof_data(data)
    if _status == "success":
        make_user(data)
    return _status
  
    
def check_prof_data(data):                                                  
    """
    Checks if the id exists if it's in use, if the 
    passwords match and if the date is valid
    and returns 'success' or an error message
    """
    _status = check_empty(data)
    if _status == "ok":
        if base.tid_exists(data['username']):
            if not base.user_exists(data['username']):
                if not (data['password'] == data['r_password']):
                    return "pass_no_match"
                elif not base.check_date(data['day'], 
                                         data['month'],
                                         data['year']):
                    return "wrong_date"
                else:
                    return "success"
            else:
                return "user_exists"
        else:
            return "no_id"
    return _status


def check_empty(data):
    """
    Checks if all the fields in the dictionary are filled,
    if not tells which one is missing
    """
    if data['username'] == "":
        return "empty_id"
    elif data['realname'] == "":
        return "empty_name"
    elif data['day'] == "0":
        return "empty_bday"
    elif data['month'] == "0":
        return "empty_bday"
    elif data['year'] == "0":
        return "empty_bday"
    elif data['weight'] == "":
        return "empty_weight"
    elif data['password'] == "":
        return "empty_pass"
    elif data['password'] == "":
        return "empty_rpass"
    else:
        return "ok"
    
    
    
def make_user(data):
    """
    Inserts new user data into the database
    """ 
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    _date = f"{data['day']}-{data['month']}-{data['year']}"
    cur.execute(f"""
                  INSERT INTO UserDatabase 
                  values('{data['username']}',
                         '{data['password']}',
                         '{data['realname']}',
                         '{_date}',
                         '{data['color']}',
                         '{data['weight']}');
                 """)
    con.commit()
    cur.close()
    con.close()