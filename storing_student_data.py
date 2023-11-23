from tkinter import *
from tkinter import messagebox
import sqlite3
student = (0,0,0,0,0)
class db:
    # def __init__(self):
    #     self._db_conection = sqlite3.connect('student.db')
    #     self._db_cursor = self._db_conection.cursor()
    _db_conection = sqlite3.connect('student.db')
    _db_cursor = _db_conection.cursor()

    def creat_table(self):
        creat = """
        CREATE TABLE if not exists student(
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
    
    def delete(self,id):
        del_="""
        delete from student where id=?
        """
        try:
            self._db_cursor.execute(del_,(id,))
            self._db_conection.commit()
        except sqlite3.Error as e:
            self._db_conection.rollback()
            print(e)
    
    def show_all(self):
        show="""
        select * from student
        """
        try:
            self._db_cursor.execute(show)
            data = self._db_cursor.fetchall()
            return data
        except sqlite3.Error as e:
            self._db_conection.rollback()
            print(e)
    
    def search(self,id):
        serch="""
        select * from student where id=?
        """
        try:
            self._db_cursor.execute(serch,(id,))
            data = self._db_cursor.fetchall()
            if(len(data)==0):
                return [-1]
            return data
        except sqlite3.Error as e:
            self._db_conection.rollback()
            print(e)
            return [-1]

def get_entery():
    global student
    student = (enter_id.get(),enter_name.get(),enter_family.get(),enter_stu_number.get(),enter_major.get())
    enter_id.delete(0,END)
    enter_name.delete(0,END)
    enter_family.delete(0,END)
    enter_stu_number.delete(0,END)
    enter_major.delete(0,END)

def insert():
    stu_db.insert(student)

def delete(): 
    id_ = student[0]
    stu_db.delete(id_)

def show():
    i=0
    data_temp = list(stu_db.show_all())
    text.delete("1.0","end")
    for data_item in data_temp:
        data = {'id':data_item[0],'name':data_item[1],'family':data_item[2],
            'stu_number':data_item[3],'major':data_item[4]}
        text.insert(INSERT,f'{i} -> ');i+=1
        text.insert(INSERT,data)
        text.insert(INSERT,'\n')

def search():
    id_ = student[0]
    data_temp = list(stu_db.search(id_))
    text.delete("1.0","end")
    if data_temp[0]==-1:
        text.insert(INSERT,'not found')
    else:
        data = {'id':data_temp[0][0],'name':data_temp[0][1],'family':data_temp[0][2],
            'stu_number':data_temp[0][3],'major':data_temp[0][4]}
        text.insert(INSERT,data)


if __name__=='__main__':
    stu_db = db()
    stu_db.creat_table()

    window = Tk()
    # window's features
    window.geometry('1000x450')
    window.title('student.app')
    # window.iconbitmap('.ico')
    # messagebox.showinfo('author','this app is created by taraneh')
    # creat menu
    menu_bar = Menu(window)
    menu_bar.add_command(label='insert',command=insert)
    menu_bar.add_command(label='delete',command=delete)
    menu_bar.add_command(label='show',command=show)
    menu_bar.add_command(label='search',command=search)
    window.config(menu=menu_bar)
    # creat entry
    lbl_id = Label(window,text='id')
    lbl_id.grid(row=2,column=0)
    enter_id = Entry(window)
    enter_id.grid(row=2,column=1,padx=1,pady=1)
    lbl_name = Label(window,text='name')
    lbl_name.grid(row=4,column=0)
    enter_name = Entry(window)
    enter_name.grid(row=4,column=1,padx=1,pady=1)
    lbl_family = Label(window,text='family')
    lbl_family.grid(row=6,column=0)
    enter_family = Entry(window)
    enter_family.grid(row=6,column=1,padx=1,pady=1)
    lbl_stu_number = Label(window,text='stu_number')
    lbl_stu_number.grid(row=8,column=0)
    enter_stu_number = Entry(window)
    enter_stu_number.grid(row=8,column=1,padx=1,pady=1)
    lbl_major = Label(window,text='major')
    lbl_major.grid(row=10,column=0)
    enter_major = Entry(window)
    enter_major.grid(row=10,column=1,padx=1,pady=1)
    btn = Button(window,text='enter data',command=get_entery)
    btn.grid(row=11,column=0)
    # creat textbox
    text = Text(window,height=25,width=100)
    text.grid(row=12,rowspan=6,column=2)
    
    window.mainloop()
