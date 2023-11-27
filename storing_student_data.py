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
    try:
        stu_db.insert(student)
        lbl_action.config(text='last action : inserted data sucsesfully',fg='blue')
    except:
        lbl_action.config(text='last action : inserted data went wrong try again',fg='red')

def delete(): 
    try:
        id_ = student[0]
        stu_db.delete(id_)
        lbl_action.config(text='last action : deleted data sucsesfully',fg='blue')
    except:
        lbl_action.config(text='last action : deleted data went wrong try again',fg='red')


def show():
    try:
        i=1
        data_temp = list(stu_db.show_all())
        text.delete("1.0","end")
        for data_item in data_temp:
            data = {'id':data_item[0],'name':data_item[1],'family':data_item[2],
                'stu_number':data_item[3],'major':data_item[4]}
            text.insert(INSERT,f'{i} -> ');i+=1
            for key,value in data.items():
                text.insert(INSERT,key)
                text.insert(INSERT,' : ')
                text.insert(INSERT,value)
                if key!='major':
                    text.insert(INSERT,'\t  ,\t   ')
            text.insert(INSERT,'\n')
        lbl_action.config(text='last action : show data sucsesfully',fg='blue')
    except:
        lbl_action.config(text='last action : show data went wrong try again',fg='red')


def search():
    try:
        id_ = student[0]
        data_temp = list(stu_db.search(id_))
        text.delete("1.0","end")
        if data_temp[0]==-1:
            text.insert(INSERT,'not found')
        else:
            text.insert(INSERT,'hole data about searched person : \n')
            data = {'id':data_temp[0][0],'name':data_temp[0][1],'family':data_temp[0][2],
                'stu_number':data_temp[0][3],'major':data_temp[0][4]}
            for key,value in data.items():
                text.insert(INSERT,key)
                text.insert(INSERT,' : ')
                text.insert(INSERT,value)
                if key!='major':
                    text.insert(INSERT,'\t  ,\t   ')
        lbl_action.config(text='last action : search data sucsesfully',fg='blue')
    except:
        lbl_action.config(text='last action : search data went wrong try again',fg='red')



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
    # creat frame
    frame_entry = LabelFrame(window,text='entry box',fg='blue')
    frame_entry.grid(row=1,column=3,ipadx=5,ipady=5)
    # creat entry
    lbl_id = Label(frame_entry,text='id')
    lbl_id.grid(row=2,column=0)
    enter_id = Entry(frame_entry)
    enter_id.grid(row=2,column=1,padx=1,pady=1)
    lbl_name = Label(frame_entry,text='name')
    lbl_name.grid(row=4,column=0)
    enter_name = Entry(frame_entry)
    enter_name.grid(row=4,column=1,padx=1,pady=1)
    lbl_family = Label(frame_entry,text='family')
    lbl_family.grid(row=6,column=0)
    enter_family = Entry(frame_entry)
    enter_family.grid(row=6,column=1,padx=1,pady=1)
    lbl_stu_number = Label(frame_entry,text='stu_number')
    lbl_stu_number.grid(row=8,column=0)
    enter_stu_number = Entry(frame_entry)
    enter_stu_number.grid(row=8,column=1,padx=1,pady=1)
    lbl_major = Label(frame_entry,text='major')
    lbl_major.grid(row=10,column=0)
    enter_major = Entry(frame_entry)
    enter_major.grid(row=10,column=1,padx=1,pady=1)
    btn = Button(frame_entry,text='enter data',command=get_entery)
    btn.grid(row=11,column=0)
    lbl_action = Label(frame_entry,text='              last action : none                    ')
    lbl_action.grid(row=12,column=0)
    # creat frame
    frame_inform = LabelFrame(window,text='show box',fg='blue')
    frame_inform.grid(row=2,column=3,ipadx=5,ipady=5,padx=100,pady=5)
    # creat textbox
    text = Text(frame_inform,height=25,width=100)
    text.pack(padx=5)
    # creat scrollbar
    # scrolbar_text = Scrollbar(window)
    # scrolbar_text.grid(column=4)
    # scrolbar_text.config(command=text.yview)
    
    window.mainloop()