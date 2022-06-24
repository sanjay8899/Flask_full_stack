import sqlite3 as sql
from os import path

root = path.dirname(path.abspath(__file__))
def create_post(name , content):
    con = sql.connect(path.join(root,'database.db'))
    cur =  con.cursor()
    cur.execute('insert into posts (name,content) values(?,?)', (name,content))
    con.commit()
    con.close()

def get_posts():
    con = sql.connect(path.join(root,'database.db'))
    cur = con.cursor()
    cur.execute('select * from posts')
    posts = cur.fetchall()
    con.commit()
    con.close()
    return posts    

def verify_user(username, passwaord):
    con = sql.connect(path.join(root,'database.db'))
    cur = con.cursor()
    cur.execute('select * from users where username = username and password = password')
    user = cur.fetchall()
    return user

