from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from student import Student
from train import Train
import os
from face_recognition import Face_Recognition
from attendance import Attendance

class FaceRecognisation:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x800+0+0")
        self.root.title("Face recognisation system")
        self.root.config(bg="#b0cbf7")

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
        frames.place(x=0,y=150,width=1500,height=650)

        # Text Heading
        title_lbl = Label(frames,text="Face Recognition attendance system",font="Helvatica 35 bold",bg="white",fg="#0089ff")
        title_lbl.place(x=0,y=0,width=1500,height=55)

        # Student Button
        stu_img = Image.open(".\\college_images\\stu.jpg")
        img_stu = stu_img.resize((220,220),Image.ANTIALIAS)
        self.stu = ImageTk.PhotoImage(img_stu)

        b1 = Button(frames,image=self.stu,cursor="hand2",command=self.student_details)
        b1.place(x=200,y=100,width=220,height=220) 
        
        b1_1 = Button(frames,text="Student Details",command=self.student_details,cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff")
        b1_1.place(x=200,y=300,width=220,height=40)

        # Detect Face Button
        face_img = Image.open(".\\college_images\\detect.png")
        face_stu = face_img.resize((220,220),Image.ANTIALIAS)
        self.face = ImageTk.PhotoImage(face_stu)

        b2 = Button(frames,image=self.face,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220) 
        
        b2_1 = Button(frames,text="Detect Face",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff",command=self.face_data)
        b2_1.place(x=500,y=300,width=220,height=40)

        # Attendance Face Button
        att_img = Image.open(".\\college_images\\attendance.jpg")
        att_stu = att_img.resize((220,220),Image.ANTIALIAS)
        self.att = ImageTk.PhotoImage(att_stu)

        b3 = Button(frames,image=self.att,cursor="hand2",command=self.add_attendance)
        b3.place(x=800,y=100,width=220,height=220) 
        
        b3_1 = Button(frames,text="Attendance",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff",command=self.add_attendance)
        b3_1.place(x=800,y=300,width=220,height=40)

        # Help Button
        help_img = Image.open(".\\college_images\\help.png")
        help_stu = help_img.resize((220,220),Image.ANTIALIAS)
        self.help = ImageTk.PhotoImage(help_stu)

        b4 = Button(frames,image=self.help,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220) 
        
        b4_1 = Button(frames,text="Help",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff")
        b4_1.place(x=1100,y=300,width=220,height=40)

        # Train Face Button
        train_img = Image.open(".\\college_images\\train.jpg")
        train_stu = train_img.resize((220,220),Image.ANTIALIAS)
        self.train = ImageTk.PhotoImage(train_stu)

        b4 = Button(frames,image=self.train,cursor="hand2",command=self.train_data)
        b4.place(x=200,y=375,width=220,height=220) 
        
        b4_1 = Button(frames,text="Train Face",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff",command=self.train_data)
        b4_1.place(x=200,y=575,width=220,height=40)

        # Photos Button
        photos_img = Image.open(".\\college_images\\img.jpg")
        photos_stu = photos_img.resize((220,220),Image.ANTIALIAS)
        self.photos = ImageTk.PhotoImage(photos_stu)

        b5 = Button(frames,image=self.photos,cursor="hand2",command=self.os_image)
        b5.place(x=500,y=375,width=220,height=220) 
        
        b5_1 = Button(frames,text="Photos",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff",command=self.os_image)
        b5_1.place(x=500,y=575,width=220,height=40)

        # Developer Button
        dev_img = Image.open(".\\college_images\\developer.jpg")
        dev_stu = dev_img.resize((220,220),Image.ANTIALIAS)
        self.dev = ImageTk.PhotoImage(dev_stu)

        b6 = Button(frames,image=self.dev,cursor="hand2")
        b6.place(x=800,y=375,width=220,height=220) 
        
        b6_1 = Button(frames,text="Developer",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff")
        b6_1.place(x=800,y=575,width=220,height=40)

        # Exit Button
        exit_img = Image.open(".\\college_images\\exit.jpg")
        exit_stu = exit_img.resize((220,220),Image.ANTIALIAS)
        self.exit = ImageTk.PhotoImage(exit_stu)

        b7 = Button(frames,image=self.exit,cursor="hand2",command=self.iexit)
        b7.place(x=1100,y=375,width=220,height=220) 
        
        b7_1 = Button(frames,text="Exit",cursor="hand2",font="Helvatica 15 bold",bg="#003161",fg="#fff",command=self.iexit)
        b7_1.place(x=1100,y=575,width=220,height=40)


    # Functions for buttons
    def student_details(self):
        self.app = Student(self.root)

    # Os image
    def os_image(self):
        os.startfile("data")

    # Train data
    def train_data(self):
        self.new_window = Toplevel(self.r)
        self.app = Train(self.root)

    # Face data
    def face_data(self):
        self.app = Face_Recognition(self.root)

    # Add Attendance
    def add_attendance(self):
        self.app = Attendance(self.root)

    # Exit
    def iexit(self):
        self.iexit = messagebox.askyesno("EXIT","Do you really wanna exit?")
        if self.iexit > 0:
            self.root.destroy()
        else:
            return


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognisation(root)
    root.mainloop()  