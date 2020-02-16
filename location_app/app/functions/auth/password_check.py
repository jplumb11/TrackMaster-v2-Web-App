import sqlite3 as sql


database_user = "app/databases/users.db" 
database_locations = 'app/databases/locations.db'

def if_user_exists(username):
    print(f"checked for existance - {username}")
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT count(*) FROM UserDatabase WHERE username='{username}';").fetchone()[0]
        if res == 0:
            return False
        else:
            return True
        
def if_tid_exists(username):
    print(f"checked for tid existance - {username}")
    with sql.connect(database_locations) as cur:
        res = cur.execute(f"SELECT count(*) FROM Location WHERE tid='{username}';").fetchone()[0]
        if res == 0:
            return False
        else:
            return True
    
def password_for(username, password):
    print(f"checked password - {username}")
    with sql.connect(database_user) as cur:
        res = cur.execute(f"SELECT password FROM UserDatabase WHERE username='{username}';").fetchone()[0]
        if password == res:
            return True
        else:
            return False

def make_user(username, password):
    print(f"created a new user - {username}")
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    cur.execute(f"INSERT INTO UserDatabase values('{username}','{password}');")
    con.commit()
    cur.close()
    con.close()

def change_password(username, new_password):
    print(f"created a new password - {username}")
    con = sql.connect(database_user)                                   
    cur = con.cursor()
    cur.execute(f"UPDATE UserDatabase SET password='{new_password}' WHERE username='{username}';")
    con.commit()
    cur.close()
    con.close()

def username_and_password(username, password):
    with sql.connect(database_user) as cur:
        try:
            cur.execute("CREATE TABLE UserDatabase(username VARCHAR2(20), password VARCHAR2(20));") 
        except:
            pass
    if username == "admin" and password == "admin":
        return "L"
    if if_user_exists(username):
        if password_for(username, password):
            return "L"
        else:
            return "WP"
    else:
        if if_tid_exists(username):
            make_user(username, password)
            return "L"
        else:
            return "NO"