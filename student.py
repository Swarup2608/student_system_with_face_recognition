from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as connect
import cv2


class Student:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x1000+0+0")
        self.root.title("Face recognisation system")
        self.root.config(bg="#b0cbf7")

        # Variables
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stu_id = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_dob = StringVar()
        self.var_phno = StringVar()
        self.var_address = StringVar()
        self.var_dep = StringVar()
        self.radio1 = StringVar()


        # Image1
        image = Image.open(".\college_images\Stanford.jpg")
        img = image.resize((750,150),Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoImage)
        f_lbl.place(x=0,y=0,height=150,width=750)

        # Image 2
        image1 = Image.open(".\\college_images\\facialrecognition.png")
        img1 = image1.resize((750,150),Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root,image=self.photoImage1)
        f_lbl1.place(x=750,y=0,height=150,width=750)

        frames = Frame(self.root,bg="#0080ff")
        frames.place(x=0,y=150,width=1500,height=850)

        # Text Heading
        title_lbl = Label(frames,text="Student Management system",font="Helvatica 35 bold",bg="white",fg="#0089ff")
        title_lbl.place(x=0,y=0,width=1500,height=55)

        main_frame = Frame(frames,bd=2)
        main_frame.place(x=10,y=65,width=1480,height=775)

        # Left Label Frame
        lft_lbl_frame = LabelFrame(main_frame,relief=RIDGE,text="Student Details",font="Helvatica 15 bold",bd=4)
        lft_lbl_frame.place(x=10,y=10,width=730,height=755)

        # Students Image
        stu_img = Image.open(".\\college_images\\stu.jpg")
        img_stu = stu_img.resize((730,200),Image.ANTIALIAS)
        self.stu = ImageTk.PhotoImage(img_stu)

        f1_lbl = Label(lft_lbl_frame,image=self.stu)
        f1_lbl.place(x=10,y=0,width=705,height=220)

        # Current Course Info
        curr_course = LabelFrame(lft_lbl_frame,bd=4,relief=RIDGE,text="Current Course Info",font="Helvatica 15 bold")
        curr_course.place(x=10,y=230,width=705,height=150)

        # Course Label
        course_lbl = Label(curr_course,text="Course :",font="Helvatica 15 bold")
        course_lbl.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        course_combo = ttk.Combobox(curr_course,font="Helvatica 15 bold",textvariable=self.var_course,width=17,state="readonly")
        course_combo['values'] = ("Select the Course","B.Tech","B.Sc","B.Com","B.Arc","Pharmacy")
        course_combo.current(0)
        course_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # Department Label
        dep_lbl = Label(curr_course,text="Department :",font="Helvatica 15 bold")
        dep_lbl.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        dep_combo = ttk.Combobox(curr_course,font="Helvatica 15 bold",textvariable=self.var_dep,width=17,state="readonly")
        dep_combo['values'] = ("Select the Department","CSE","IT","ECE","EEE","MECH","CIVIL","ECM")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=3,padx=5,pady=10,sticky=W)

        # Semester Label
        sem_lbl = Label(curr_course,text="Semester :",font="Helvatica 15 bold")
        sem_lbl.grid(row=1,column=0,padx=5,pady=10,sticky=W)

        sem_combo = ttk.Combobox(curr_course,font="Helvatica 15 bold",textvariable=self.var_sem,width=17,state="readonly")
        sem_combo['values'] = ("Select the Semester","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=5,pady=10,sticky=W)

        # Year Label
        year_lbl = Label(curr_course,text="Year :",font="Helvatica 15 bold")
        year_lbl.grid(row=1,column=2,padx=5,pady=10,sticky=W)

        year_combo = ttk.Combobox(curr_course,font="Helvatica 15 bold",textvariable=self.var_year,width=17,state="readonly")
        year_combo['values'] = ("Select the year","2018-2022","2019-2023","2020-2024","2021-2025")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=5,pady=10,sticky=W)        

        # Class Student Info
        stu_course = LabelFrame(lft_lbl_frame,bd=4,relief=RIDGE,text="Class Student Info",font="Helvatica 15 bold")
        stu_course.place(x=10,y=400,width=705,height=320)

        # Student Id
        stu_id = Label(stu_course,text="Student Id :",font="Helvatica 12 bold")
        stu_id.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        stu_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_stu_id)
        stu_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Student Nmae
        stu_name = Label(stu_course,text="Student Name :",font="Helvatica 12 bold")
        stu_name.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        stuname_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_name)
        stuname_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Student dob
        stu_dob = Label(stu_course,text="Student DOB :",font="Helvatica 12 bold")
        stu_dob.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        studob_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_dob)
        studob_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Student rno
        stu_rno = Label(stu_course,text="Student R.No :",font="Helvatica 12 bold")
        stu_rno.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        sturno_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_roll)
        sturno_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student phno
        stu_phno = Label(stu_course,text="Student Ph.No :",font="Helvatica 12 bold")
        stu_phno.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        stuphno_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_phno)
        stuphno_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Student adrs
        stu_adrs = Label(stu_course,text="Student Adress :",font="Helvatica 12 bold")
        stu_adrs.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        stuadrs_entry = Entry(stu_course,width=12,font="Helvatica 12 bold",textvariable=self.var_address)
        stuadrs_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        # Radio Buttons
        radiobttn =Radiobutton(stu_course,text="Take Photo Sample",value="Yes",font="Helvatica 15 bold",variable=self.radio1)
        radiobttn.grid(row=3,column=0)

        radiobttn1 =Radiobutton(stu_course,text="No Photo Sample",value="No",font="Helvatica 15 bold",variable=self.radio1)
        radiobttn1.grid(row=3,column=1)

        # Buttons Frame

        btn_frame = Frame(stu_course,bd=4,relief=RIDGE)
        btn_frame.place(x=15,y=180,width=672,height=50)

        # Save btn
        save_btn = Button(btn_frame,text="Save",width=13,font="Helvatica 15 bold",bg="#0089ff",fg="white",command=self.add_data)
        save_btn.grid(row=0,column=0)
        # Update btn
        upd_btn = Button(btn_frame,text="Update",width=13,font="Helvatica 15 bold",bg="#003161",fg="white",command=self.update_data)
        upd_btn.grid(row=0,column=1)
        # Delete btn
        del_btn = Button(btn_frame,text="Delete",width=13,font="Helvatica 15 bold",bg="#ff0000",fg="white",command=self.delete_data)
        del_btn.grid(row=0,column=2)
        # Reset btn
        reset_btn = Button(btn_frame,text="Reset",width=13,font="Helvatica 15 bold",bg="#9d00ff",fg="white",command=self.reset_data)
        reset_btn.grid(row=0,column=3)

        # Buttons Frame 2

        btn_frame1 = Frame(stu_course,bd=4,relief=RIDGE)
        btn_frame1.place(x=12,y=235,width=675,height=50)

        # Save btn
        take_pic_btn = Button(btn_frame1,text="Take Photo Sample",width=27,font="Helvatica 15 bold",bg="#0089ff",fg="white",command=self.generate_dataset)
        take_pic_btn.grid(row=0,column=0)
        # Update btn
        upd_pic_btn = Button(btn_frame1,text="Update Photo Sample",width=27,font="Helvatica 15 bold",bg="#003161",fg="white")
        upd_pic_btn.grid(row=0,column=1)

        # Right Label Frame
        rgt_lbl_frame = LabelFrame(main_frame,relief=RIDGE,text="Student Details",font="Helvatica 15 bold",bd=4)
        rgt_lbl_frame.place(x=750,y=10,width=720,height=755)

        # Students Image
        stu_img_rgt = Image.open(".\\college_images\\stu2.jpg")
        img_stu_rgt = stu_img_rgt.resize((705,200),Image.ANTIALIAS)
        self.stu_rgt = ImageTk.PhotoImage(img_stu_rgt)

        f1_rgt_lbl = Label(rgt_lbl_frame,image=self.stu_rgt)
        f1_rgt_lbl.place(x=5,y=0,width=705,height=220)

        # Search Frame
        search_frame = LabelFrame(rgt_lbl_frame,bd=4,relief=RIDGE,text="Search System",font="Helvatica 15 bold")
        search_frame.place(x=5,y=220,width=705,height=70)
        
        # Search Label
        search_lbl = Label(search_frame,text="Search Here :",font="Helvatica 13 bold")
        search_lbl.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        # Search Combo
        search_combo = ttk.Combobox(search_frame,font="Helvatica 13 bold",width=13,state="readonly")
        search_combo['values'] = ("Select","Phone No","Roll No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # Search Entry
        search_entry = Entry(search_frame,width=14,font="Helvatica 13 bold")
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        # Search btn
        search_btn = Button(search_frame,text="Search",width=13,font="Helvatica 13 bold",bg="#0089ff",fg="white")
        search_btn.grid(row=0,column=3)

        # Show All btn
        showallBtn = Button(search_frame,text="Show All",width=13,font="Helvatica 13 bold",bg="#003161",fg="white")
        showallBtn.grid(row=0,column=4)

        # Table Frame
        table_frame = Frame(rgt_lbl_frame,bd=4,relief=RIDGE)
        table_frame.place(x=5,y=300,width=705,height=420)

        # Horizontal Scroller
        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)

        # Vertical Scroller
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)

        # Table
        self.student = ttk.Treeview(table_frame,column=("id","name","roll","dep","course","sem","year","dob","phone","address","radio"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.student.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.student.yview)

        self.student.heading("dep",text="Department")
        self.student.heading("course",text="Course")
        self.student.heading("year",text="Year")
        self.student.heading("sem",text="Semester")
        self.student.heading("id",text="Student Id")
        self.student.heading("name",text="Name")
        self.student.heading("roll",text="Roll No")
        self.student.heading("dob",text="DOB")
        self.student.heading("phone",text="Phone No")
        self.student.heading("address",text="Address")
        self.student['show'] = "headings"

        self.student.column("dep",width=150)
        self.student.column("course",width=150)
        self.student.column("year",width=150)
        self.student.column("sem",width=150)
        self.student.column("id",width=150)
        self.student.column("name",width=150)
        self.student.column("roll",width=150)
        self.student.column("dob",width=150)
        self.student.column("phone",width=150)
        self.student.column("address",width=150)


        self.student.pack(fill=BOTH,expand=1)
        self.student.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    # Functions
    # Insert data
    def add_data(self):
        try:
            conn = connect.connect(host="localhost",username="root",password="",database="student")
            mycur = conn.cursor()
            mycur.execute("INSERT INTO student(id, name, roll_no, course, dep, sem, year, dob,  ph_no, address,radio) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                self.var_stu_id.get(),
                self.var_name.get(),
                self.var_roll.get(),
                self.var_course.get(),
                self.var_dep.get(),
                self.var_sem.get(),
                self.var_year.get(),
                self.var_dob.get(),
                self.var_phno.get(),
                self.var_address.get(),       
                self.radio1.get()        
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Successs","Successfully added to database",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error","Due to :{}".format(e),parent=self.root)

    # Fetch Data
    def fetch_data(self):
        conn = connect.connect(host="localhost",username="root",password="",database="student")
        mycur = conn.cursor()
        mycur.execute("SELECT * FROM student")
        data = mycur.fetchall()
        if len(data) != 0:
            self.student.delete(*self.student.get_children())
            for i in data:
                self.student.insert("",END,values=i)
            conn.commit()
        conn.close()       

    # Get Cursor
    def get_cursor(self,event=""):
        cursor_focus = self.student.focus()
        content = self.student.item(cursor_focus)
        data = content['values']

        self.var_stu_id.set(data[0])
        self.var_name.set(data[1])
        self.var_roll.set(data[2])
        self.var_dep.set(data[3])
        self.var_course.set(data[4])
        self.var_sem.set(data[5])
        self.var_year.set(data[6])
        self.var_dob.set(data[7])
        self.var_phno.set(data[8])
        self.var_address.set(data[9])

    # Update data
    def update_data(self):
        try:
            update = messagebox.askyesno("Update","Do you want to update?",parent=self.root)
            if update>0:
                conn = connect.connect(host="localhost",username="root",password="",database="student")
                mycur = conn.cursor()
                mycur.execute("UPDATE student SET name=%s,roll_no=%s,dep=%s,course=%s,sem=%s,year=%s,dob=%s,ph_no=%s,address=%s,radio=%s WHERE id=%s",(
                self.var_name.get(),
                self.var_roll.get(),
                self.var_course.get(),
                self.var_dep.get(),
                self.var_sem.get(),
                self.var_year.get(),
                self.var_dob.get(),
                self.var_phno.get(),
                self.var_address.get(),       
                self.radio1.get(),
                self.var_stu_id.get() 
                ))
            else:
                if not update:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Successs","Successfully updated to database",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error","Due to :{}".format(e),parent=self.root)

    # Delete data
    def delete_data(self):
        try:
            delete = messagebox.askyesno("Update","Do you want to delete?",parent=self.root)
            if delete > 0:
                conn = connect.connect(host="localhost",username="root",password="",database="student")
                mycur = conn.cursor()
                mycur.execute("DELETE FROM student WHERE id=%s",(self.var_stu_id.get(),))
            else:
                if not delete:
                    return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Successs","Successfully Deleted from database",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error","Due to :{}".format(e),parent=self.root)

    # Reset Data
    def reset_data(self):
        self.var_address.set("")
        self.var_course.set("Select the Course")
        self.var_dep.set("Select the Department")
        self.var_dob.set("")
        self.var_name.set("")
        self.var_roll.set("")
        self.var_sem.set("Select the Semester")
        self.var_year.set("Select the year")
        self.var_stu_id.set("")
        self.var_phno.set("")

    # Generate the dataset
    def generate_dataset(self):
        # try:
            conn = connect.connect(host="localhost",username="root",password="",database="student")
            mycur = conn.cursor()
            mycur.execute("SELECT * FROM student")
            myresult= mycur.fetchall()
            id = self.var_stu_id.get()
            mycur.execute("UPDATE student SET name=%s,roll_no=%s,dep=%s,course=%s,sem=%s,year=%s,dob=%s,ph_no=%s,address=%s,radio=%s WHERE id=%s",(
                self.var_name.get(),
                self.var_roll.get(),
                self.var_course.get(),
                self.var_dep.get(),
                self.var_sem.get(),
                self.var_year.get(),
                self.var_dob.get(),
                self.var_phno.get(),
                self.var_address.get(),       
                self.radio1.get(),
                self.var_stu_id.get() 
            ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close

            # Load Predefined data on face frontals from opencv
            face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    cropped_img = img[y:y+h,x:x+w]
                    return cropped_img
            cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
            img_id = 0
            while True:
                ret,frame = cap.read()
                if face_cropped(frame) is not None:
                    img_id+=1
                    face = cv2.resize(face_cropped(frame),(450,450))
                    face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    file = 'data/user.'+str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file,face)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped",face)
                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets done")

        # except Exception as e:
        #     messagebox.showerror("Error","Due to :{}".format(e),parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()  