#!/usr/bin/python
# _*_ coding: utf-8 _*_

import os
import sqlite3

os.chdir("./sqlite3")


class db_operate(object):
    def __init__(self):
        self.db = self.openDb()
        self.cursor = self.db.cursor()

    def openDb(self):
        db = sqlite3.connect('test.db')
        print("数据库打开成功")
        return db

    def createTable(self, tablename):
        try:
            self.cursor.execute("create table "+tablename +
                                "(key varchar(20) primary key , value varchar(20))")
            self.db.commit()
            print("表创建成功")
        except:
            print("表已经存在")

    def insert(self, tablename, key, value):
        try:
            self.cursor.execute(
                "insert into "+tablename+" (key,value) values ('"+key+"','"+value+"')")
            self.db.commit()
        except:
            print("插入失败")

    def closeDb(self):
        self.db.close()
        print("数据库关闭成功")

    def select(self, tablename):
        try:
            self.cursor.execute("select * from "+tablename)
            data = self.cursor.fetchall()
            print(data)
        except:
            print("查询失败")

    def update(self, tablename, key, value):
        self.cursor.execute("update "+tablename +
                            " set value = '"+value+"' where key='"+key+"'")
        print("更新成功"+key+"的值为"+value)


if __name__ == '__main__':
    mDb = db_operate()
    mDb.createTable("test")
    mDb.insert("test", "xieyao", "test")
    mDb.select("test")
    mDb.update("test", "xieyao", "test2")
    mDb.select("test")
