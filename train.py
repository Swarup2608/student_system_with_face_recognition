from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector as connect
import cv2
import os
import numpy as np


class Train:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1500x1000+0+0")
        self.root.title("Face recognisation system")
        self.root.config(bg="#b0cbf7")

        title_lbl = Label(self.root,text="Train Data set",font="Helvatica 35 bold",bg="#0089ff",fg="#fff")
        title_lbl.place(x=0,y=0,width=1500,height=55)

        img_top = Image.open(".\\college_images\\facialrecognition.png")
        img_top = img_top.resize((1500,420),Image.ANTIALIAS)
        self.img_top = ImageTk.PhotoImage(img_top)

        f1_lbl = Label(self.root,image=self.img_top)
        f1_lbl.place(x=0,y=55,width=1500,height=420)

        img_btm = Image.open(".\\college_images\\img.jpg")
        img_btm = img_btm.resize((1500,450),Image.ANTIALIAS)
        self.img_btm = ImageTk.PhotoImage(img_btm)

        f2_lbl = Label(self.root,image=self.img_btm)
        f2_lbl.place(x=0,y=550,width=1500,height=450)

        b1_btn = Button(self.root,text="Train the data",cursor="hand2",font="Helvatica 15 bold",bg="#fff",fg="#0089ff",command=self.train_classifier)
        b1_btn.place(x=0,y=475,width=1530,height=80)

    def train_classifier(self):
        data_dir = ("data")
        path  = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L") # Gray scale image
            imageNp = np.array(img,'uint8')
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # Train Classifier and save
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("Classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Trained all the data")

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop() 