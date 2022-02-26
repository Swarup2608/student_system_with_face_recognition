from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as connect
import cv2
import os
import csv
from tkinter import filedialog

mydata = []
class Attendance:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x1000+0+0")
        self.root.title("Face recognisation system")
        self.root.config(bg="#b0cbf7")
        
        self.att_id_var = StringVar()
        self.var_name = StringVar()
        self.var_roll = StringVar()
        self.var_date = StringVar()
        self.var_time = StringVar()
        self.var_dep = StringVar()
        self.var_sts = StringVar()


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
        title_lbl = Label(frames,text="Attendance Management system",font="Helvatica 35 bold",bg="white",fg="#0089ff")
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

        left_inner = Frame(lft_lbl_frame,bd=4,relief=RIDGE)
        left_inner.place(x=10,y=230,width=705,height=380)

        # Attendance id
        att_id = Label(left_inner,text="Attendance Id :",font="Helvatica 13 bold")
        att_id.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        att_id_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.att_id_var)
        att_id_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Dept
        dept = Label(left_inner,text="Department :",font="Helvatica 13 bold")
        dept.grid(row=0,column=2,padx=2,pady=10,sticky=W)

        dept_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.var_dep)
        dept_entry.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # name
        name = Label(left_inner,text="Name :",font="Helvatica 13 bold")
        name.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        name_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.var_name)
        name_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # roll
        roll = Label(left_inner,text="Roll Number :",font="Helvatica 13 bold")
        roll.grid(row=1,column=2,padx=2,pady=10,sticky=W)

        roll_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.var_roll)
        roll_entry.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # date
        date = Label(left_inner,text="Date :",font="Helvatica 13 bold")
        date.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        date_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.var_date)
        date_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # time
        time = Label(left_inner,text="Time :",font="Helvatica 13 bold")
        time.grid(row=2,column=2,padx=2,pady=10,sticky=W)

        time_entry = Entry(left_inner,width=12,font="Helvatica 13 bold",textvariable=self.var_time)
        time_entry.grid(row=2,column=3,padx=2,pady=10,sticky=W)

        sts_lbl = Label(left_inner,text="Attendance Status :",font="Helvatica 15 bold")
        sts_lbl.grid(row=4,column=0,padx=5,pady=10,sticky=W)

        sts_combo = ttk.Combobox(left_inner,font="Helvatica 15 bold",textvariable=self.var_sts,width=17,state="readonly")
        sts_combo['values'] = ("Select the Status","Present","Absent")
        sts_combo.current(0)
        sts_combo.grid(row=4,column=1,padx=5,pady=10,sticky=W)

        # Buttons Frame

        btn_frame = Frame(left_inner,bd=4,relief=RIDGE)
        btn_frame.place(x=15,y=250,width=672,height=50)

        # Save btn
        save_btn = Button(btn_frame,text="Import Csv",width=18,font="Helvatica 15 bold",bg="#0089ff",fg="white",command=self.importcsv)
        save_btn.grid(row=0,column=0)
        # Update btn
        upd_btn = Button(btn_frame,text="Export Csv",width=18,font="Helvatica 15 bold",bg="#003161",fg="white",command=self.exportcsv)
        upd_btn.grid(row=0,column=1)
        # Reset btn
        reset_btn = Button(btn_frame,text="Reset",width=18,font="Helvatica 15 bold",bg="#9d00ff",fg="white",command=self.reset)
        reset_btn.grid(row=0,column=3)


        # Right Label Frame
        rgt_lbl_frame = LabelFrame(main_frame,relief=RIDGE,text="Student Details",font="Helvatica 15 bold",bd=4)
        rgt_lbl_frame.place(x=750,y=10,width=720,height=755)

        # Students Image
        stu_img_rgt = Image.open(".\\college_images\\stu2.jpg")
        img_stu_rgt = stu_img_rgt.resize((705,200),Image.ANTIALIAS)
        self.stu_rgt = ImageTk.PhotoImage(img_stu_rgt)

        f1_rgt_lbl = Label(rgt_lbl_frame,image=self.stu_rgt)
        f1_rgt_lbl.place(x=5,y=0,width=705,height=220)

         # Table Frame
        table_frame = Frame(rgt_lbl_frame,bd=4,relief=RIDGE)
        table_frame.place(x=5,y=220,width=705,height=500)

        # Horizontal Scroller
        scroll_x = Scrollbar(table_frame,orient=HORIZONTAL)

        # Vertical Scroller
        scroll_y = Scrollbar(table_frame,orient=VERTICAL)

        self.attd = ttk.Treeview(table_frame,column=("id","name","dep","date","time","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)


        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_x.config(command=self.attd.xview)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.attd.yview)

        self.attd.heading("id",text="Attendance Id")
        self.attd.heading("name",text="Name")
        self.attd.heading("dep",text="Department")
        self.attd.heading("date",text="Date")
        self.attd.heading("time",text="Time")
        self.attd.heading("attendance",text="Attendance")
        self.attd['show'] = "headings"

        self.attd.column("id",width=100)
        self.attd.column("name",width=100)
        self.attd.column("dep",width=100)
        self.attd.column("date",width=100)
        self.attd.column("time",width=100)


        self.attd.pack(fill=BOTH,expand=1)
        
        self.attd.bind("<ButtonRelease>",self.get_cur)

    def fetch_data(self,rows):
        self.attd.delete(*self.attd.get_children())

        for i in rows:
            self.attd.insert("",END,values=i)

    def importcsv(self):
        global mydata
        mydata.clear()
        fln =  filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV files",".csv"),("All Files","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    def exportcsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No data","No data found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV files",".csv"),("All Files","*.*")),parent=self.root)
            with open(fln,mode='w',newline='') as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported","Your data is successfully exported")
        except Exception as e:
            messagebox.showerror("Error","Due to :{}".format(e),parent=self.root)

    def get_cur(self,event=""):
        cur_row = self.attd.focus()
        content = self.attd.item(cur_row)
        rows = content['values']
        self.att_id_var.set(rows[0])
        self.var_name.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_roll.set(rows[0])
        self.var_date.set(rows[3])
        self.var_time.set(rows[4])
        self.var_sts.set(rows[5])

    def reset(self):
        self.att_id_var.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_roll.set("")
        self.var_date.set("")
        self.var_time.set("")
        self.var_sts.set("Select the Status")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()  