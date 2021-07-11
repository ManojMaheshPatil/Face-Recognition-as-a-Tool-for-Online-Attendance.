from tkinter import *
from tkinter import ttk
import PIL
from PIL import Image,ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Facial Recognition System")

        # Background Image
        img=Image.open(r"images\background.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.background=ImageTk.PhotoImage(img)

        bg_img=Label(root,image=self.background)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        # Title
        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("Merriweather",36,"bold"),bg="white",fg="teal")
        title_lbl.place(x=0,y=50,width=1530,height=50)


        # Buttons
        # 1) Student Details

        st_img=Image.open(r"images\student.jpg")
        st_img=st_img.resize((220,220),Image.ANTIALIAS)
        self.st_photoImg=ImageTk.PhotoImage(st_img)

        st_btn=Button(bg_img,image=self.st_photoImg,command=self.student_details,cursor="hand2")
        st_btn.place(x=200,y=200,width=220,height=220)

        st_txt_btn=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        st_txt_btn.place(x=200,y=400,width=220,height=40)


        # 2) Detect Faces

        face_img=Image.open(r"images\face_detector.jpg")
        face_img=face_img.resize((220,220),Image.ANTIALIAS)
        self.face_photoImg=ImageTk.PhotoImage(face_img)

        face_btn=Button(bg_img,image=self.face_photoImg,command=self.face_data,cursor="hand2")
        face_btn.place(x=500,y=200,width=220,height=220)

        face_txt_btn=Button(bg_img,text="Face Detector",command=self.face_data,cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        face_txt_btn.place(x=500,y=400,width=220,height=40)


        # 3) Attendance Button

        att_img=Image.open(r"images\attendance.jpg")
        att_img=att_img.resize((220,220),Image.ANTIALIAS)
        self.att_photoImg=ImageTk.PhotoImage(att_img)

        att_btn=Button(bg_img,image=self.att_photoImg,cursor="hand2")
        att_btn.place(x=800,y=200,width=220,height=220)

        att_txt_btn=Button(bg_img,text="Attendance",cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        att_txt_btn.place(x=800,y=400,width=220,height=40)


        # 4) Help Button

        help_img=Image.open(r"images\help.jpg")
        help_img=help_img.resize((220,220),Image.ANTIALIAS)
        self.help_photoImg=ImageTk.PhotoImage(help_img)

        help_btn=Button(bg_img,image=self.help_photoImg,cursor="hand2")
        help_btn.place(x=1100,y=200,width=220,height=220)

        help_txt_btn=Button(bg_img,text="Help",cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        help_txt_btn.place(x=1100,y=400,width=220,height=40)


        # 5) Train Button

        train_img=Image.open(r"images\train_face.jpg")
        train_img=train_img.resize((220,220),Image.ANTIALIAS)
        self.train_photoImg=ImageTk.PhotoImage(train_img)

        train_btn=Button(bg_img,image=self.train_photoImg,cursor="hand2",command=self.train_data)
        train_btn.place(x=200,y=500,width=220,height=220)

        train_txt_btn=Button(bg_img,text="Train",command=self.train_data,cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        train_txt_btn.place(x=200,y=700,width=220,height=40)


        # 6) Photos Button

        photo_img=Image.open(r"images\photo.jpeg")
        photo_img=photo_img.resize((220,220),Image.ANTIALIAS)
        self.photo_photoImg=ImageTk.PhotoImage(photo_img)

        photo_btn=Button(bg_img,image=self.photo_photoImg,cursor="hand2",command=self.open_img)
        photo_btn.place(x=500,y=500,width=220,height=220)

        face_txt_btn=Button(bg_img,text="Photos",command=self.open_img,cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        face_txt_btn.place(x=500,y=700,width=220,height=40)


        # 7) Developer Button

        dev_img=Image.open(r"images\developer.png")
        dev_img=dev_img.resize((220,220),Image.ANTIALIAS)
        self.dev_photoImg=ImageTk.PhotoImage(dev_img)

        dev_btn=Button(bg_img,image=self.dev_photoImg,cursor="hand2")
        dev_btn.place(x=800,y=500,width=220,height=220)

        dev_txt_btn=Button(bg_img,text="Developer",cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        dev_txt_btn.place(x=800,y=700,width=220,height=40)


        # 8) Exit Button

        exit_img=Image.open(r"images\exit.jpg")
        exit_img=exit_img.resize((220,220),Image.ANTIALIAS)
        self.exit_photoImg=ImageTk.PhotoImage(exit_img)

        exit_btn=Button(bg_img,image=self.exit_photoImg,cursor="hand2")
        exit_btn.place(x=1100,y=500,width=220,height=220)

        exit_txt_btn=Button(bg_img,text="Exit",cursor="hand2",font=("Merriweather",16,"bold"),bg="blue",fg="white")
        exit_txt_btn.place(x=1100,y=700,width=220,height=40)

    def open_img(self):
        os.startfile("data")


    # --------------Functionalities to the Buttons---------
    def student_details(self):
        self.newWindow=Toplevel(self.root)
        self.app=Student(self.newWindow)


    def train_data(self):
        self.newWindow=Toplevel(self.root)
        self.app=Train(self.newWindow)


    def face_data(self):
        self.newWindow=Toplevel(self.root)
        self.app=Face_Recognition(self.newWindow)






if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.attributes("-fullscreen", True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    root.mainloop()

