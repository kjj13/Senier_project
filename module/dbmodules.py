# file name : dbModule.py
# pwd : /myflask/module/dbModule.py
 
import pymysql
 
class Database():
    def __init__(self):
        self.db= pymysql.connect(host='18.212.183.253',
                     port=3306,
                     user='jjoong',
                     passwd='1234',
                     db='pi',
                     charset='utf8')
        self.cursor= self.db.cursor(pymysql.cursors.DictCursor)
 
    def execute(self, query, args={}):
        self.cursor.execute(query, args) 
 
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def executeAll(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row
 
    def commit():
        self.db.commit()

    def close():
        self.db.close()
