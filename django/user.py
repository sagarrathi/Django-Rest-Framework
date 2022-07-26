import sqlite3

from flask_restful import Resource

class User:
    def __init__(self,_id, username, password):
        self.id=_id #puthon keyword
        self.username=username
        self.password=password

    @classmethod
    def find_by_username(cls,username):
        connection =sqlite3.connect('data.db')
        cursor=connection.cursor()
        
        query="SELECT * FROM users WHERE username=?"

        result=cursor.execute(query, (username,) ) #Becasue it acceps only tuples hence comma and bracket
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        
        connection.close()

        return user 

    @classmethod
    def find_by_id(cls,_id):
        connection =sqlite3.connect('data.db')
        cursor=connection.cursor()
        
        query="SELECT * FROM users WHERE id=?"
        result=cursor.execute(query, (_id,) ) #Becasue it acceps only tuples hence comma and bracket
        row=result.fetchone()
        if row:
            user=cls(*row)
        else:
            user=None
        
        connection.close()

        return user


class UserRegister(Resource):
    def post(self):
        connection =sqlite3.connect('data.db')
        cursor=connection.cursor()
        query="INSERT INTO users VALUES (NULL, ?,?)"
        cursor.execute(query, (data['username'], data['password']))
        connection.commit()
        connection.close()
