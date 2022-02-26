import datetime
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as connect
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x805+0+0")
        self.root.title("Face recognisation system")
        self.root.config(bg="#b0cbf7")

        title_lbl = Label(self.root,text="Face Recognition",font="Helvatica 20 bold",bg="#0089ff",fg="#fff")
        title_lbl.place(x=0,y=0,width=1300,height=55)

        img_top = Image.open(".\\college_images\\train.jpg")
        img_top = img_top.resize((650,700),Image.ANTIALIAS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f1_lbl = Label(self.root,image=self.img_top)
        f1_lbl.place(x=0,y=55,width=650,height=700)

        img_bottom = Image.open(".\\college_images\\face.jpg")
        img_bottom = img_bottom.resize((650,700),Image.ANTIALIAS)
        self.img_bottom = ImageTk.PhotoImage(img_bottom)

        f1_lbl = Label(self.root,image=self.img_bottom)
        f1_lbl.place(x=650,y=55,width=650,height=700)

        b1_btn = Button(self.root,text="Face Recognition",cursor="hand2",font="Helvatica 15 bold",bg="#0089ff",fg="#fff",command=self.face_recog)
        b1_btn.place(x=0,y=750,width=1300,height=55)

    def mark_attendance(self,r,n,d):
        r = r[0]
        d = d[0]
        n = n[0]
        with open("fee.csv","r+",newline="\n") as f:
            myDataList = f.readlines()
            nameList = []
            for line in myDataList:
                entry = line.split(",")
                nameList.append(entry[0])
            if (r not in nameList):
                now = datetime.datetime.now()
                d1 = now.strftime("%d%m%Y")
                dtstring = now.strftime("%H:%M:%S")
                f.writelines(f"\n{r},{n},{d},{dtstring},{d1},Present")
                print(n)


    # Face Recognition
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf):
            gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_img,scaleFactor,minNeighbours)

            coord = []

            for (x,w,y,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3) 
                id,predict = clf.predict(gray_img[y:y+h,x:x+w])
                confidence = int(100*(1-predict/300))

                conn = connect.connect(host="localhost",username="root",password="",database="student")
                mycur = conn.cursor()
                mycur.execute("SELECT name FROM student WHERE id=%s",(id,))
                n = mycur.fetchone()
                mycur.execute("SELECT roll_no FROM student WHERE id=%s",(id,))
                r = mycur.fetchone()
                mycur.execute("SELECT dep FROM student WHERE id=%s",(id,))
                d = mycur.fetchone()
                
                if confidence > 77:
                    cv2.putText(img,f"Roll No: {r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name: {n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department: {d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(r,n,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                    cv2.putText(img,f"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        cap = cv2.VideoCapture(0)
        while True:
            _,img = cap.read()
            img = recognize(img=img,clf=clf,faceCascade=faceCascade)
            cv2.imshow("Welcome",img)

            if cv2.waitKey(1) == 13:
                break
        cap.release()
        cv2.destroyAllWindows()    

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop() 