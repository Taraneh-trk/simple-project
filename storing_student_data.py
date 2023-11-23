from tkinter import *
import sqlite3

class db:
    def __init__(self):
        self._db_conection = sqlite3.connect('student.db')
        self._db_cursor = self._db_conection.cursor()
    
    def creat_table(self):
        creat = """
        CREAT TABLE if not exists student(
        'id' INTEGER,
        'name' TEXT,
        'family' TEXT,
        'stu-number' INTEGER,
        'major' TEXT
        );
        """
        self._db_cursor.execute(creat)
        
    def insert(self,student):
        add="""
        insert into student values (?,?,?,?,?)
        """
        try:
            self._db_cursor.execute(add,student)
            self._db_conection.commit()
        except sqlite3.Error as e:
            self._db_conection.rollback()
    
    def delete(self,student):
        del_="""
        delete from student where id=?
        """
        try:
            self._db_cursor.execute(del_,student[0])
            self._db_conection.commit()
        except sqlite3.Error as e:
            self._db_conection.rollback()
    
    def show_all(self):
        show="""
        select * from student
        """
        try:
            self._db_cursor.execute(show)
            data = self._db_cursor.fetchall()

        except sqlite3.Error as e:
            self._db_conection.rollback()
    
    def search(self,student):
        serch="""
        select * from student where id=?
        """
        try:
            self._db_cursor.execute(serch,student[0])
            data = self._db_cursor.fetchall()

        except sqlite3.Error as e:
            self._db_conection.rollback()

class tk:
    pass


if __name__=='__main__':
    pass