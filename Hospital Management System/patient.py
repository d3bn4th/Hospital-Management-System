from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector 

# Setting up the DATABASE and TABLES in MySQL
# using mysql.connector in python
mycon = mysql.connector.connect(
                                host = 'localhost',
                                user = 'root'
                              )
# creating cursor object to execute query from python code
cur = mycon.cursor()
cur.execute("Show databases;")
flag = False
for dbname in cur:
    if ("HOSPITAL" in dbname):
        flag = True
        break
if not flag:
    # To create database HOSPITAL if not exists in MySQL
    cur.execute("Create database if not exists HOSPITAL")
    print("database HOSPITAL created!")
else:
    print("database HOSPITAL already exists.")   
    
# Connecting to MySQL database already created "HOSPITAL" 
# creating object con to using .connect method in mysql.connector module
con = mycon.connect(
    host = "localhost",
    user = "root",
    database = "HOSPITAL"
)

# Check for connection to the database
if mycon.is_connected():
    # CONNECTION MADE
    print("database opened")
else:
    # Error when not connected
    print("error opening database") 
    
# To create table Patient
# Executing query from python to create tables to store patient info.
t_query1 = """CREATE table if not exists patient(
    Dep varchar(45),
    Past varchar(45), 
    Room varchar(45),
    Floor varchar(45),
    patient_id INT,
    Name varchar(45),
    Division varchar(45),
    Roll varchar(45),
    Gender varchar(45),
    Dob varchar(45),
    Email varchar(45),
    Phone varchar(45),
    Address varchar(45),
    Doctor varchar(45))"""
cur = mycon.cursor()
cur.execute(t_query1)

# Class for GUI and Patient Data Mangement and access 
class Patient:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1366x695+0+0")
        self.root.title("HOSPITAL MANAGEMENT SYSTEM")
        # Program Variables
        self.var_dep = StringVar()
        self.var_past = StringVar()
        self.var_room = StringVar()
        self.var_floor = StringVar()
        self.var_patient_id = StringVar()
        self.var_patient_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_doctor = StringVar()

        # Fecthing the images
        # Adding images to GUI
        # 1st iimage
        img = Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\1st.jpg")
        img = img.resize((480,120), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        # To diaplay the images
        self.btn_1 = Button(self.root, image = self.photoimg, cursor = "hand2")
        self.btn_1.place(x = 0, y = 0, width = 480, height = 120)

        # 2nd image
        img_2 = Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\Turing.jpg")
        img_2 = img_2.resize((480,120), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)
        
        # To diaplay the images
        self.btn_2 = Button(self.root, image = self.photoimg_2, cursor = "hand2")
        self.btn_2.place(x = 480, y = 0, width = 480, height = 120)

        # 3rd image
        img_3 = Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\5th.jpg")
        img_3 = img_3.resize((480,120), Image.ANTIALIAS)
        self.photoimg_3 = ImageTk.PhotoImage(img_3)
        
        # To diaplay the images
        self.btn_3 = Button(self.root, image = self.photoimg_3, cursor = "hand2")
        self.btn_3.place(x = 960, y = 0, width = 480, height = 120)


        # Backgroud Image for the program
        img_4 = Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\hospital.jpg")
        img_4 = img_4.resize((1366,695), Image.ANTIALIAS)
        self.photoimg_4 = ImageTk.PhotoImage(img_4)
        
        bg_lbl = Label(self.root, image = self.photoimg_4, bd =2, relief = RIDGE)
        bg_lbl.place(x = 0, y = 100, width = 1366, height = 600)

        lbl_title = Label(bg_lbl, text = "HOSPITAL MANAGEMENT SYSTEM", font = ('times new roman', 27, 'bold'), fg = "Black", bg = "white")
        lbl_title.place(x = 0, y = 0, width = 1366, height = 40)

        # Title Label 
        Management_frame = Frame(bg_lbl, bd =2, relief = RIDGE, bg = 'white')
        Management_frame.place(x = 15, y = 45, width = 1330, height = 540)

        # Left frame
        DataLeftFrame = LabelFrame(Management_frame, bd = 4, relief = RIDGE, padx=2,text="Patient Information",font=('times new roman', 12,'bold'),fg="red",bg="white")
        DataLeftFrame.place(x = 10, y = 10, width  = 650, height = 540)

        # Hospital Department information/ Rules of the Hospital
        img_5 = Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\rules.jpg")
        img_5 = img_5.resize((650,120), Image.ANTIALIAS)
        self.photoimg_5 = ImageTk.PhotoImage(img_5)
        
        my_img = Label(DataLeftFrame, image = self.photoimg_5, bd =2, relief = RIDGE)
        my_img.place(x = 0, y = 0, width = 650, height = 120)

        # Hospital Department information
        # Current past LabelFrame information
        std_lbl_info_frame =LabelFrame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,text="Hospital Department information",font=('times new roman',12,'bold'),fg="red",bg="white")
        std_lbl_info_frame.place(x = 0, y = 120, width  = 650, height = 110)

        # Hospital Department
        lbl_dept = Label(std_lbl_info_frame, text = "Department : ",font = ('arial', 10, 'bold'), bg = "white")
        lbl_dept.grid(row = 0 , column = 0, padx = 2, sticky = W)

        combo_dep = ttk.Combobox(std_lbl_info_frame, textvariable = self.var_dep, font = ('arial', 10, 'bold'), width = 17, state = "readonly")
        combo_dep["value"] = ("Select Department", "Physician", "Cardiovascular", "Medicine", "Pediatricain", "Neurosurgery", "Respratory")
        combo_dep.current(0)
        combo_dep.grid(row = 0, column = 1, padx = 2, pady = 5, sticky = W)
        
        # Prior Health issues
        past_std = Label(std_lbl_info_frame, font = ('arial', 10, 'bold'),text = " Prior Health issues : ", bg = "white")
        past_std.grid(row = 0, column = 2, sticky = W, padx = 2, pady = 10)
        com_txtpast_std = ttk.Combobox(std_lbl_info_frame, textvariable = self.var_past, font = ('arial', 10, 'bold'), width = 17, state = "readonly")
        com_txtpast_std["value"] = ("Select Yes/ No", "YES", "NO", "Don't know")
        com_txtpast_std.current(0)
        com_txtpast_std.grid(row = 0, column = 3, sticky = W, padx = 2, pady =10)

        # Room Type
        current_room = Label(std_lbl_info_frame, font = ('arial', 10, 'bold'),text = "Room Type :", bg = "white")
        current_room.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 10)

        com_txt_current_room = ttk.Combobox(std_lbl_info_frame,  textvariable = self.var_room, font = ('arial', 10, 'bold'), width = 17, state = "readonly")
        com_txt_current_room["value"] = ("Select Rooom Type", "Normal", "Medium", "High", "VIP")
        com_txt_current_room.current(0)
        com_txt_current_room.grid(row = 1, column = 1, sticky = W, padx = 2)

        # Hospital Floor alloted tot the patient
        label_Floor = Label(std_lbl_info_frame, font = ('arial', 10, 'bold'),text = "Hospital Floor :", bg = "white")
        label_Floor.grid(row = 1, column = 2, sticky = W, padx = 2, pady = 10)
        comFloor = ttk.Combobox(std_lbl_info_frame, textvariable = self.var_floor, font = ('arial', 10, 'bold'), width = 17, state = "readonly")
        
        comFloor["value"] = ("Select Floor", "Floor-1", "Floor-2", "Floor-3", "Floor-4")
        comFloor.current(0)
        comFloor.grid(row = 1, column = 3, sticky = W, padx = 2, pady =10)

        # Patient info display Frame
        std_lbl_class_frame = LabelFrame(DataLeftFrame, bd = 4, relief = RIDGE, padx = 2, text = " Patient Frame information", font = ('times new roman', 12, 'bold'), fg = "red", bg = "white")
        std_lbl_class_frame.place(x = 0, y = 235, width  = 650, height = 200)
        
        # Lables entry
        # Patient ID
        lbl_id = Label( std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "PatientID :", bg = "white")
        lbl_id.grid(row = 0, column = 0, sticky = W, padx = 2, pady = 7)

        id_entry = ttk.Entry(std_lbl_class_frame, textvariable = self.var_patient_id,  font = ('arial', 10, 'bold'), width = 22)
        id_entry.grid(row = 0, column = 1, sticky = W, padx = 2, pady = 7)

        # Patient Name
        lbl_Name = Label( std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Patient Name :", bg = "white")
        lbl_Name.grid(row = 0, column = 2, sticky = W, padx = 2, pady = 7)

        txt_name = ttk.Entry(std_lbl_class_frame, textvariable = self.var_patient_name, font = ('arial', 10, 'bold'), width = 22)
        txt_name.grid(row = 0, column = 3, sticky = W, padx = 2, pady = 7)

        # Hospital Division
        lbl_div = Label( std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Class Division :", bg = "white")
        lbl_div.grid(row = 1, column = 0, sticky = W, padx = 2, pady = 7)

        com_txt_div = ttk.Combobox(std_lbl_class_frame, textvariable = self.var_div, font = ('arial', 10, 'bold'), width = 18, state = "readonly")
        com_txt_div['value'] = ("Select Division", "A", "B" ,"C")
        com_txt_div.current(0)
        com_txt_div.grid(row = 1, column = 1, sticky = W, padx = 2, pady =7)

        # Patient No.
        lbl_roll = Label( std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Patient No : ", bg = "white")
        lbl_roll.grid(row = 1, column = 2, sticky = W, padx = 2, pady = 7)

        txt_roll = ttk.Entry(std_lbl_class_frame, textvariable = self.var_roll, font = ('arial', 10, 'bold'), width = 22)
        txt_roll.grid(row = 1, column = 3, sticky = W, padx = 2, pady = 7)

        # Gender of the Patient
        lbl_gender = Label( std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Gender :", bg = "white")
        lbl_gender.grid(row = 2, column = 0, sticky = W, padx = 2, pady = 7)

        com_txt_gender = ttk.Combobox(std_lbl_class_frame, textvariable = self.var_gender, font = ('arial', 10, 'bold'), width = 18, state = "readonly")
        com_txt_gender['value'] = ("Select gender", "Male", "Female" ,"Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row = 2, column = 1, sticky = W, padx = 2, pady =7)

        # DOB
        lbl_dob = Label(std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "DOB :", bg = "white")
        lbl_dob.grid(row = 2, column = 2, sticky = W, padx = 2, pady = 7)

        txt_dob = ttk.Entry(std_lbl_class_frame, textvariable = self.var_dob, font = ('arial', 10, 'bold'), width = 22)
        txt_dob.grid(row = 2, column = 3, padx = 2, pady = 7)

        # Email
        lbl_email = Label(std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Email :", bg = "white")
        lbl_email.grid(row = 3, column = 0, sticky = W, padx = 2, pady = 7)

        txt_email = ttk.Entry(std_lbl_class_frame, textvariable = self.var_email, font = ('arial', 10, 'bold'), width = 22)
        txt_email.grid(row = 3, column = 1, padx = 2, pady = 7)

        # Phone
        lbl_phone = Label(std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Phone No : ", bg = "white")
        lbl_phone.grid(row = 3, column = 2, sticky = W, padx = 2, pady = 7)

        txt_phone = ttk.Entry(std_lbl_class_frame, textvariable = self.var_phone, font = ('arial', 10, 'bold'), width = 22)
        txt_phone.grid(row = 3, column = 3, padx = 2, pady = 7)

        # Address
        lbl_address = Label(std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Address : ", bg = "white")
        lbl_address.grid(row = 4, column = 0, sticky = W, padx = 2, pady = 7)

        txt_address = ttk.Entry(std_lbl_class_frame, textvariable = self.var_address, font = ('arial', 10, 'bold'), width = 22)
        txt_address.grid(row = 4, column = 1, padx = 2, pady = 7)

        # Doctor
        lbl_doctor = Label(std_lbl_class_frame, font = ('arial', 10, 'bold'),text = "Doctor : ", bg = "white")
        lbl_doctor.grid(row = 4, column = 2, sticky = W, padx = 2, pady = 7)

        txt_doctor = ttk.Entry(std_lbl_class_frame, textvariable = self.var_doctor, font = ('arial', 10, 'bold'), width = 22)
        txt_doctor.grid(row = 4, column = 3, padx = 2, pady = 7)

        # Button frame
        btn_frame = Frame(DataLeftFrame, bd =2, relief = RIDGE, bg = 'white')
        btn_frame.place(x = 0, y = 435, width = 650, height = 38)

        btn_Add = Button(btn_frame, text = "Save", command = self.add_data, font = ('arial', 10, 'bold'), width = 17, bg = 'blue', fg = 'white')
        btn_Add.grid(row =0, column = 0, padx =1)

        btn_update = Button(btn_frame, text = "Update", command = self.update_data, font = ('arial', 10, 'bold'), width = 17, bg = 'blue', fg = 'white')
        btn_update.grid(row =0, column = 1, padx =1)

        btn_delete = Button(btn_frame, text = "Delete",  command = self.delete_data, font = ('arial', 10, 'bold'), width = 17, bg = 'blue', fg = 'white')
        btn_delete.grid(row =0, column = 2, padx =1)

        btn_reset = Button(btn_frame, text = "Reset", command = self.reset_data, font = ('arial', 10, 'bold'), width = 17, bg = 'blue', fg = 'white')
        btn_reset.grid(row =0, column = 3, padx =1)

       
        # Right frame
        DataRightFrame = LabelFrame(Management_frame, bd = 4, relief = RIDGE, padx = 2, text = "Patient Information ", font = ('times new roman', 12, 'bold'), fg = "red", bg = "white")
        DataRightFrame.place(x = 650, y = 10, width  = 650, height = 540)
        
        # Right frame picture
        img_6= Image.open(r"C:\Users\thicc\Desktop\Python\Work\Learn\Hospital Mangement\Hospital images\6th.jpg")
        img_6 = img.resize((630,200), Image.ANTIALIAS)
        self.photoimg_6 = ImageTk.PhotoImage(img_6)
        
        # to diaplay the images
        self.btn_6 = Button(DataRightFrame, image = self.photoimg_6, cursor = "hand2")
        self.btn_6.place(x = 0, y = 0, width = 630, height = 120)

        # Search Patient Info frame
        Search_Frame = LabelFrame(DataRightFrame, bd = 4, relief = RIDGE, padx = 2, text = "Search Patient Info ", font = ('times new roman', 12, 'bold'), fg = "red", bg = "white")
        Search_Frame.place(x = 0, y = 120, width  = 630, height = 70)
        
        # Search By
        search_by = Label(Search_Frame, font = ('arial', 10, 'bold'),text = "Search By:", fg = 'red',bg = "black")
        search_by.grid(row = 0, column = 0, sticky = W, padx = 2)
        
        # Search Data from the GUI
        self.var_com_search = StringVar()
        com_txt_search = ttk.Combobox(Search_Frame, textvariable=self.var_com_search , font = ('arial', 10, 'bold'), width = 18, state = "readonly")
        com_txt_search['value'] = ("Select Option", "Patient No", "Phone" ,"Patient ID")
        com_txt_search.current(0)
        com_txt_search.grid(row = 0, column = 1, sticky = W, padx = 5)
        
        self.var_search = StringVar()
        txt_search = ttk.Entry(Search_Frame, textvariable=self.var_search ,font = ('arial', 10, 'bold'), width = 22)
        txt_search.grid(row = 0, column = 2, padx = 5)

        btn_search = Button(Search_Frame,command = self.search_data, text = "Search",  font = ('arial', 10, 'bold'), width = 10, bg = 'blue', fg = 'white')
        btn_search.grid(row =0, column = 3, padx =5)

        btn_ShowAll = Button(Search_Frame, command = self.fetch_data, text = "Show All",  font = ('arial', 10, 'bold'), width = 10, bg = 'blue', fg = 'white')
        btn_ShowAll.grid(row =0, column = 4, padx =5)


        table_frame = Frame(DataRightFrame, bd = 4, relief = RIDGE)
        table_frame.place(x = 0, y = 190, width = 640, height = 300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.patient_table=ttk.Treeview(table_frame,column=("dep","past","room","floor","id","name","div","roll","gender","dob","email","phone","address","doctor",), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.patient_table.xview)
        scroll_y.config(command = self.patient_table.yview)

        self.patient_table.heading("dep", text = "Department")
        self.patient_table.heading("past", text = "Past Health")
        self.patient_table.heading("room", text = "Rooms")
        self.patient_table.heading("floor", text = "Floor")
        self.patient_table.heading("id", text = "patient ID")
        self.patient_table.heading("name", text = "patient Name")
        self.patient_table.heading("div", text = "Class Div")
        self.patient_table.heading("roll", text = "Roll No")
        self.patient_table.heading("gender", text = "Gender")
        self.patient_table.heading("dob", text = "DOB")
        self.patient_table.heading("email", text = "Email")
        self.patient_table.heading("phone", text = "Phone No")
        self.patient_table.heading("address", text = "Address")
        self.patient_table.heading("doctor", text = "Doctor Name")

        self.patient_table["show"] = "headings"

        self.patient_table.column("dep", width = 100)
        self.patient_table.column("past", width = 100)
        self.patient_table.column("room", width = 100)
        self.patient_table.column("floor", width = 100)
        self.patient_table.column("id", width = 100)
        self.patient_table.column("name", width = 100)
        self.patient_table.column("div", width = 100)
        self.patient_table.column("roll", width = 100)
        self.patient_table.column("gender", width = 100)
        self.patient_table.column("dob", width = 100)
        self.patient_table.column("email", width = 100)
        self.patient_table.column("phone", width = 100)
        self.patient_table.column("address", width = 100)
        self.patient_table.column("doctor", width = 100)
        
        self.patient_table.pack(fill = BOTH, expand = 1)
        self.patient_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()


    # Adding Data from the GUI
    def add_data(self):
        if (self.var_dep.get() == "" or self.var_email.get == "" or self.var_patient_id.get() == ""):
            messagebox.showerror("Error", "All Fields are required")

        else:
            try:
                conn = mysql.connector.connect(
                                                host = "localhost",
                                                user = "root",
                                                database = "HOSPITAL" 
                                            )
                my_cursur = conn.cursor()
                my_cursur.execute("insert into Patient values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_past.get(),
                                                                                                            self.var_room.get(),
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_patient_id.get(),
                                                                                                            self.var_patient_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_doctor.get()
                                                                                                         ))
                conn.commit()
                self.fetch_data()
                conn.close()
                # to show POPUP message when the function is executed
                messagebox.showinfo("Success", "Patient has been added", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)


    # Fetch Patient DATA from the Database Hospital and Table Patient
    def fetch_data(self):
        conn = mysql.connector.connect(
                    host = "localhost",
                    user = "root",
                    database = "HOSPITAL" 
                )
        my_cursur = conn.cursor()
        my_cursur.execute("select *  from patient")
        data = my_cursur.fetchall()
        if len(data) != 0:
            self.patient_table.delete(*self.patient_table.get_children())
            for i in data:
                self.patient_table.insert("", END, values = i)
            conn.commit()
        conn.close()


    # To Display/Show data in the GUI
    def get_cursor(self, event = ""):
            cursor_row = self.patient_table.focus()
            content = self.patient_table.item(cursor_row)
            data = content["values"]
            self.var_dep.set(data[0]),
            self.var_past.set(data[1]),
            self.var_room.set(data[2]),
            self.var_floor.set(data[3]),
            self.var_patient_id.set(data[4]),
            self.var_patient_name.set(data[5]),
            self.var_div.set(data[6]),
            self.var_roll.set(data[7]),
            self.var_gender.set(data[8]),
            self.var_dob.set(data[9]),
            self.var_email.set(data[10]),
            self.var_phone.set(data[11]),
            self.var_address.set(data[12]),
            self.var_doctor.set(data[13])


    # Update DATA from the GUI
    def update_data(self):
        if (self.var_dep.get() == "" or self.var_email.get == "" or self.var_patient_id.get() == ""):
                messagebox.showerror("Error", "All Fields are required")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure update this patient data", parent = self.root)
                if update > 0:
                        conn = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        database = "HOSPITAL" 
                                        )
                        my_cursur = conn.cursor()
                        my_cursur.execute("update patient set Dep=%s,past=%s,Room=%s,floor=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Doctor=%s where patient_id =%s",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_past.get(),
                                                                                                            self.var_room.get(),
                                                                                                            self.var_floor.get(),
                                                                                                            self.var_patient_name.get(),
                                                                                                            self.var_div.get(),
                                                                                                            self.var_roll.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_doctor.get(),
                                                                                                            self.var_patient_id.get()                                                                                                           
                                                                                                         ))
                else:
                        if not update:
                                return
                conn.commit()
                self.fetch_data()
                conn.close()
                
                # to show POPUP message when the function is executed
                messagebox.showinfo("Success", "Updated!", parent = self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)


    # Delete Data
    def delete_data(self):
            if self.var_patient_id.get()=="":
                messagebox.showerror("Error", "All Fields are required")
            else:
                try:
                    Delete = messagebox.askyesno("Delete", "Are you sure you wanna delete this Patient", parent = self.root)
                    if Delete > 0:
                        conn = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        database = "HOSPITAL" 
                                        )
                        my_cursur = conn.cursor()
                        sql = "delete from patient where patient_id = %s"
                        value = (self.var_patient_id.get(),)
                        my_cursur.execute(sql, value)
                    else:
                        if not Delete:
                                return

                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    
                     # to show POPUP message when the function is executed
                    messagebox.showinfo("Delete", "Your Patient has been deleted!", parent = self.root)
                except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)

            
    # Reset data display in GUI
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_past.set("Select Past Healt"),
        self.var_room.set("Select Room"),
        self.var_floor.set("Select Floor"),
        self.var_patient_id.set(""),
        self.var_patient_name.set(""),
        self.var_div.set("Select Division"),
        self.var_roll.set(""),
        self.var_gender.set(""),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_doctor.set("")

         
    # Search Data from the GUI
    def search_data(self):
            if self.var_con_search.get()=="" or self.var_search.get() == "":
                messagebox.showerror("Error", "Please Select option", parent =self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                                        host = "localhost",
                                        user = "root",
                                        database = "HOSPITAL" 
                                        )
                    my_cursur = conn.cursor()
                    my_cursur.execute("select * from patient where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'")
                    data = my_cursur.fetchall()
                    if len(data) != 0:
                        self.patient_table.delete(*self.patient_table.get_children())
                        for i in data:
                            self.patient_table.insert("", END, values = i)
                        conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error", f"Due To: {str(es)}", parent = self.root)

                    
# __main__
if __name__ == "__main__":
    root = Tk()
    obj = Patient(root)
    root.mainloop()
