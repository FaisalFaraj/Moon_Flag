import os
import tkinter as tk
import tkinter.ttk as ttk 
from PIL import ImageTk
from time import  strftime
from tkinter import messagebox
import arabic_reshaper
from bidi.algorithm import get_display
import sys
from sqlite3 import connect

from selenium import webdriver
#import time
from selenium.webdriver.chrome.options import Options 
from webdriver_manager.chrome import ChromeDriverManager
import threading


try:
    current_dir = os.getcwd().replace('\\','/')
    data_folder = current_dir + "/data"
    os.mkdir(data_folder) 
except Exception:
    pass

'''
try:
    home = os.path.expanduser("~").replace('\\','/')
    moon_flag_downloads_path = home + "/Desktop" + "/Moon Flag Downloads"
    os.mkdir(moon_flag_downloads_path)
except Exception:
    pass
'''

current_dir = os.getcwd().replace('\\','/')
chrome_driver_download_path = f"{current_dir}/data"
chrome_driver_path = f"{current_dir}/data/.wdm/drivers/chromedriver/win32/102.0.5005.61/chromedriver.exe"
if not(os.path.exists(chrome_driver_path)):
    ChromeDriverManager(path=chrome_driver_download_path).install()


operations_con = connect('data/operations_DataBase.db', check_same_thread=False)


def operations_DataBase(execute_syntax):
    rows = []
    cursorObj_attendence = operations_con.cursor()

    cursorObj_attendence.execute("create table if not exists operations_DataBase( Number integer , Link text ,another_link text, create_date date, download_date date,download_case text)")
    operations_con.commit()


    if execute_syntax!= None:

     cursorObj_attendence.execute(f'SELECT {execute_syntax} FROM operations_DataBase')
     rows = cursorObj_attendence.fetchall()

    return cursorObj_attendence, rows


def arabic_text(text):
    reshaped_text = arabic_reshaper.reshape(str(text))
    bidi_text = get_display(reshaped_text)
    return bidi_text,reshaped_text



def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path.replace('/','\\'))


def app_icon():
    app_icon = resource_path("Icons/Launcher.ico")
    return app_icon


def adjust_column(rows_,column):
    if len(rows_) > 0:
        get_colmuns = [str(item[column]) for item in rows_]
        lengest_row = max(get_colmuns,key=len)
        size = len(lengest_row) * 5
        return size
    else:
        return None


def date_check(root):
    date_frame = tk.Frame(root,bg="white")
    date_frame.pack(fill='both', expand=True, side="left")
   
    current_time = [strftime("%Y"),strftime("%m"),strftime("%d"),strftime("%I"),strftime("%p")]
    
    hours = []
    for i in range(13):
        if i > 0:
           if i <=9:
             hours.append(str(0)+str(i))
           else:
             hours.append(str(i))

    d29 = []
    for i in range(30):
        if i > 0:
           if i <=9:
              d29.append(str(0)+str(i))
           else:
              d29.append(str(i))
    
    d30 = []
    for i in range(31):
        if i > 0:
           if i <=9:
               d30.append(str(0)+str(i))
           else:
               d30.append(str(i))


    d31 = []
    for i in range(32):
        if i > 0:
           if i <=9:
               d31.append(str(0)+str(i))
           else:
               d31.append(str(i))


    months_ = []
    for i in range(13):
        if i > 0:
           if i <=9:
               months_.append(str(0)+str(i))
           else:
               months_.append(str(i))


    years = list(range(2021, 2122))



    months = [
       None,
       d31,
       d29,
       d31,
       d30,
       d31,
       d30,
       d31,
       d31,
       d30,
       d31,
       d30,
       d31]

    
    
    cb_A_P = ttk.Combobox(date_frame, values=("AM", "PM"))
    cb_A_P.pack(fill='both', expand=True ,side="left")
    cb_A_P.set(current_time[4])



    cb_hour = ttk.Combobox(date_frame, values=hours)
    cb_hour.pack(fill='both', expand=True ,side="left")
    cb_hour.set(current_time[3])
 

   
   

    cb_day = ttk.Combobox(date_frame, values=months[0])
    cb_day.pack(fill='both', expand=True ,side="left")
    cb_day.set(current_time[2])
  
  


    cb_month = ttk.Combobox(date_frame, values=months_)
    cb_month.pack(fill='both', expand=True ,side="left")
    cb_month.set(current_time[1])
  

    cb_year = ttk.Combobox(date_frame, values=years)
    cb_year.pack(fill='both', expand=True ,side="left")
    cb_year.set(current_time[0])
 



class main:
    def __init__(self, root):
        self.main_root = root
        self.main_root.title('Moon Flag')
        self.main_root.geometry('750x600')
        self.main_root.resizable(False, False)
        
        self.main_root.configure(bg='white')
        #self.main_root.iconbitmap(default=app_icon())
    
        

        self.main_frame = tk.Frame(self.main_root,bg="white")
        self.main_frame.pack(fill='both', expand=True)

        
        frame1 = tk.Frame(self.main_frame,bg="white")
        frame1.pack(fill='both', expand=True, side="top")


        frame2 = tk.Frame(self.main_frame,bg="white")
        frame2.pack(fill='both', expand=True ,side="top")
        
        frame3 = tk.Frame(self.main_frame,bg="white")
        frame3.pack(fill='both', expand=True ,side="top")
        
        frame4 = tk.Frame(self.main_frame,bg="white")
        frame4.pack(fill='both', expand=True ,side="top")
        
        frame5 = tk.Frame(self.main_frame,bg="white")
        frame5.pack(fill='both', expand=True ,side="top")
        
        
        self.threading_list = [None]
        
        bg_label = tk.Label(frame1, text='', bd=0, bg= 'black')
        bg_label.pack(fill='both', side="top")       
        
        #Background Image
        bg_image = ImageTk.PhotoImage(master = self.main_root,file= 'D:/Programming/Python Projects/Moon Flag/data/Moon Flag.png' )
        bg_label = tk.Label(frame1, image=bg_image, bd=0, bg= 'black')
        bg_label.pack(fill='both', expand=True,side="top")       
        

        #Title and Subtitle
        title = tk.Label(frame1, text='Moon Flag\n', font=('Impact', 20, 'bold'), fg="tomato",bg='black').pack(fill='both', expand=True,side="top")
        
                
        self.another_link = tk.Entry(frame2, font=('Goudy old style', 12), bg='gray95')
        self.another_link.pack(fill='both', expand=True,side="left")
        
        lbl_another_link = tk.Label(frame2, text=arabic_text('ادخل الرابط الثانوي')[0], font=('Goudy old style', 12),fg='white', bg='black').pack(fill='both', expand=True,side="left")
        
        
        self.Link = tk.Entry(frame2, font=('Goudy old style', 12), bg='gray95')
        self.Link.pack(fill='both', expand=True,side="left")
        
        lbl_Link = tk.Label(frame2, text=arabic_text('ادخل الرابط')[0], font=('Goudy old style', 12),fg='white', bg='black').pack(fill='both', expand=True,side="left")
        
        
        current_time =[strftime("%Y"),strftime("%m"),strftime("%d"),strftime("%I"),strftime("%M"),strftime("%p")]
        
        minutes = ['00']
        for i in range(60):
            if i > 0:
                if i <=9:
                    minutes.append(str(0)+str(i))
                else:
                    minutes.append(str(i))
                    
        hours = []
        for i in range(13):
            if i > 0:
                if i <=9:
                    hours.append(str(0)+str(i))
                else:
                    hours.append(str(i))

        d29 = []
        for i in range(30):
            if i > 0:
                if i <=9:
                    d29.append(str(0)+str(i))
                else:
                    d29.append(str(i))
        
        d30 = []
        for i in range(31):
            if i > 0:
                if i <=9:
                    d30.append(str(0)+str(i))
                else:
                    d30.append(str(i))


        d31 = []
        for i in range(32):
            if i > 0:
                if i <=9:
                    d31.append(str(0)+str(i))
                else:
                    d31.append(str(i))


        months_ = []
        for i in range(13):
            if i > 0:
                if i <=9:
                    months_.append(str(0)+str(i))
                else:
                    months_.append(str(i))


        years = list(range(2021, 2122))



        months = [
        None,
        d31,
        d29,
        d31,
        d30,
        d31,
        d30,
        d31,
        d31,
        d30,
        d31,
        d30,
        d31]

        
        submit = tk.Button(frame3, cursor='hand2', command=self.save_link , text=arabic_text('اضافة الرابط')[0], bd=0, font=('Goudy old style', 12), fg='white', bg='black').pack(fill='both', expand=True,side="left")

        self.cb_A_P = ttk.Combobox(frame3,width=5,font=('arial',9), values=("AM", "PM"))
        self.cb_A_P.pack(fill='both', side="left")
        self.cb_A_P.set(current_time[5])
    
        #A_P_sb_lbl = tk.Label(frame3, text=arabic_text('')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")

        
        self.cb_minute = ttk.Combobox(frame3,width=5,font=('arial',9), values=minutes)
        self.cb_minute.pack(fill='both', side="left")
        self.cb_minute.set(current_time[4])
        
        min_sb_lbl = tk.Label(frame3, text=arabic_text('دقيقة')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")


        self.cb_hour = ttk.Combobox(frame3,width=5,font=('arial',9), values=hours)
        self.cb_hour.pack(fill='both', side="left")
        self.cb_hour.set(current_time[3])
        
    
        sec_hour_label = tk.Label(frame3, text=arabic_text('ساعة')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")
    

        self.cb_day = ttk.Combobox(frame3,width=5,font=('arial',9), values=months[1])
        self.cb_day.pack(fill='both', side="left")
        self.cb_day.set(current_time[2])
    
    
        day_sb_lbl = tk.Label(frame3, text=arabic_text('اليوم')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")


        self.cb_month = ttk.Combobox(frame3,width=5,font=('arial',9), values=months_)
        self.cb_month.pack(fill='both', side="left")
        self.cb_month.set(current_time[1])
    
        month_sb_lbl = tk.Label(frame3, text=arabic_text('شهر')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")
        
        
        self.cb_year = ttk.Combobox(frame3,width=5,font=('arial',9), values=years)
        self.cb_year.pack(fill='both', side="left")
        self.cb_year.set(current_time[0])
    
        year_sb_lbl = tk.Label(frame3, text=arabic_text('سنة')[0], font=('Goudy old style', 12),fg="black", bg='white').pack(fill='both', expand=True,side="left")


       
        
        
        lbl_time = tk.Label(frame3, text=arabic_text('ادخل وقت التحميل')[0], font=('Goudy old style', 12),fg="white", bg='black').pack(fill='both', expand=True,side="left")
        
        
       
        
        
         # setup_widgets   
       # Headers = ["رقم","عنوان الرابط","عنوان الرابط الثانوي" ,"وقت الاضافة", "وقت التحميل","حالة التحميل"] 
        Headers = ["رقم","عنوان الرابط","عنوان الرابط الثانوي" ,"وقت الاضافة", "وقت التحميل"] 
    
        # create a treeview with dual scrollbars
        self.tree = ttk.Treeview(frame4,columns=Headers, show="headings",height=10)
        vsb = ttk.Scrollbar(frame4,orient="vertical",
            command=self.tree.yview)
        hsb = ttk.Scrollbar(frame4,orient="horizontal",
            command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set,
            xscrollcommand=hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew', in_=frame4)
        vsb.grid(column=1, row=0, sticky='ns', in_=frame4)
        hsb.grid(column=0, row=1, sticky='ew', in_=frame4)
        frame4.grid_columnconfigure(0, weight=1)
        frame4.grid_rowconfigure(0, weight=1)
        
        rows = []
       
        for item in operations_DataBase("*")[1] :
            

            self.tree.insert('', '0', values=(item[0],item[1][-18:],item[2][-18:],item[3],item[4]))
        
            rows.append((item[0],item[1][-18:],item[2][-18:],item[3],item[4]))
            
    
        

        for col in range(len(Headers)):
                self.tree.heading(Headers[col], text=Headers[col].title())

                self.tree.column(Headers[col], width=adjust_column(rows,col))
        
        
        remove_link_button = tk.Button(frame5, cursor='hand2', command=self.remove_link , text=arabic_text('حذف الرابط')[0], bd=0, font=('arial',15), fg="tomato", bg='black').pack(fill='both', expand=True,side="left")

        #filter_link_button = tk.Button(frame5, cursor='hand2', command=self.remove_link , text=arabic_text('فلترة')[0], bd=0, font=('arial',15), fg="tomato", bg='black').pack(fill='both', expand=True,side="left")

        self.check_downloads()
        
        self.main_root.mainloop()
    
    
    def remove_link(self):
        selected_items = ([self.tree.item(x) for x in self.tree.selection()])
        selected_items_ = [ name['values'] for name in selected_items]
        
        for row in selected_items_:
            sqlite_delete_query = """DELETE FROM operations_DataBase WHERE Number = ?"""
            operations_DataBase(None)[0].executemany(sqlite_delete_query, [(str(row[0]),)])
            operations_con.commit()
        
        
        x = self.tree.get_children()
        for i in x:
            self.tree.delete(i)
            
       
        
        for item in operations_DataBase("*")[1] :
            

            self.tree.insert('', '0', values=(item[0],item[1][-18:],item[2][-18:],item[3],item[4]))
        
        
        messagebox.showinfo(arabic_text("تمت العملية بنجاح")[1], parent=self.main_root, detail= (arabic_text("تم الحذف" )[1] ))

        
    def check_downloads(self):
       
       current_time =  strftime("%Y-%m-%d-%I-%M-%p")
       for item in operations_DataBase("*")[1]:   
           if item[4] == current_time:
               
                if self.threading_list[-1] != item[1] and len(item[1]) > 5 and len(item[2]) > 5:
                   
                    def run_in_thread():
                        self.threading_list.append(item[1])
                        driver = webdriver.Chrome(executable_path=chrome_driver_path)


                        driver.maximize_window()
                        URL = item[1]
                        
                        
                        
                        driver.get(URL)
                         
                        driver.implicitly_wait(20)

                        element = driver.find_element_by_xpath(item[2])
                        webdriver.ActionChains(driver).move_to_element(element ).click(element ).perform()
                        
                        
                        
                    threading.Thread(target=run_in_thread).start()

                    #time.sleep(30000)

                #driver.close()
                
               
       self.main_root.after(5000, self.check_downloads)
     

    def save_link(self):
        current_time = strftime("%Y-%m-%d-%I-%M-%p")
        
        
        if len(operations_DataBase("Number")[1]) > 0:
            last_number = int(operations_DataBase("Number")[1][-1][0])
        else:
            last_number = 0
    
        Number = last_number + 1
        download_date = f"{self.cb_year.get()}-{self.cb_month.get()}-{self.cb_day.get()}-{self.cb_hour.get()}-{self.cb_minute.get()}-{self.cb_A_P.get()}"
        entities = (Number,self.Link.get(),self.another_link.get(),current_time,download_date,'No')
        operations_DataBase(None)[0].execute('''INSERT INTO operations_DataBase( Number, Link ,another_link , create_date , download_date ,download_case) VALUES(?,?,?,?,?,?)''', entities)
        operations_con.commit()
        
        x = self.tree.get_children()
        for i in x:
            self.tree.delete(i)
            
       
        
        for item in operations_DataBase("*")[1] :
            

            self.tree.insert('', '0', values=(item[0],item[1][-18:],item[2][-18:],item[3],item[4]))
            


root = tk.Tk()
obj = main(root)
root.mainloop()