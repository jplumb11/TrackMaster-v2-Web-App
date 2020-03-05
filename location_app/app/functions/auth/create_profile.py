import sqlite3 as sql
from app.functions.auth import base


database_user = "app/databases/users.db" 
database_locations = 'app/databases/locations.db'
 
def create_profile(data):
    base.create()
    _status = check_prof_data(data)
    if _status == "success":
        make_user(data)
    return _status
        
def check_prof_data(data):
    _status = check_empty(data)
    if _status == "ok":
        if base.tid_exists(data['username']):
            if not base.user_exists(data['username']):
                if not (data['password'] == data['r_password']):
                    return "pass_no_match"
                elif not base.check_date(data['day'], data['month'], data['year']):
                    return "bad_date"
                else:
                    return "success"
            else:
                return "user_exists"
        else:
            return "no_id"
    return _status

def check_empty(data):
    if data['username'] == "":
        return "empty_id"
    elif data['realname'] == "":
        return "empty_name"
    elif data['day'] == "0":
        return "empty_day"
    elif data['month'] == "0":
        return "empty_month"
    elif data['year'] == "0":
        return "empty_year"
    elif data['gender'] == "":
        return "empty_gender"
    elif data['height'] == "":
        return "empty_height"
    elif data['weight'] == "":
        return "empty_weight"
    elif data['password'] == "":
        return "empty_pass"
    else:
        return "ok"
    
def make_user(data):
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    _date = f"{data['day']}-{data['month']}-{data['year']}"
    com = f"INSERT INTO UserDatabase values('{data['username']}','{data['password']}','{data['realname']}','{data['gender']}','{_date}','{data['height']}','{data['weight']}');"
    print(com)
    cur.execute(com)
    con.commit()
    cur.close()
    con.close()
    
    
#     ImmutableMultiDict([
#     ('username', '69'), 
#     ('realname', 'Adi'),
#     ('day', '23'), 
#     ('month', '1'), 
#     ('year', '1998'), 
#     ('gender', 'male'), 
#     ('height', '183'), 
#     ('weight', '75'), 
#     ('password', 'fisgib-duwxut-4Rowhi'), 
#     ('r_password', 'fisgib-duwxut-4Rowhi')])

