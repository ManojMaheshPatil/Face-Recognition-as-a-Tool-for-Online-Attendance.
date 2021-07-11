from tkinter import*
from tkinter import ttk #Has stylish toolkits
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Face_Recognition:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")


        title_lbl=Label(self.root,text="Face Recognition",font=("Merriweather",32,"bold"),bg="white",fg="teal")
        title_lbl.place(x=15,y=15,height=45,width=1230)

        img=Image.open(r"images/bgface_rec.jpg")
        img=img.resize((1275,750),Image.ANTIALIAS)
        self.background=ImageTk.PhotoImage(img)

        bg_img=Label(root,image=self.background)
        bg_img.place(x=0,y=0)

        # Button
        f_rec_btn=Button(self.root,text="Click Me to Start Face Recognition!👇",command=self.face_recog,cursor="hand2",font=("Merriweather",16,"bold"),bg="black",fg="white")
        f_rec_btn.place(x=450,y=380,width=380,height=60)


    # ============================= Face Recognition =====================================================================

    def face_recog(self):
    
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors) #This contains faces in box 

            # create an empty list that contains coordinates
            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])


                # retrieve data already stored 
                conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
                cur=conn.cursor()

                cur.execute("select Name from student where ID="+str(id))
                n = cur.fetchone()
                n = "+".join(n)

                cur.execute("select Department from student where ID="+str(id))
                d = cur.fetchone()
                d = "+".join(d)

                cur.execute("select Semester from student where ID="+str(id))
                s = cur.fetchone()
                s = "+".join(s)


                # refer to "predict" formula from video 6 at time 20:14 , Remember : Lesser the confidence , better is the measure (Don't get confused)
                confidence = int((100*(1-predict/300)))


                if confidence>77 : # Random number (But take more)
                    cv2.putText(img,f"Name:{n}", (x,y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}", (x,y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3)
                    cv2.putText(img,f"Semester:{s}", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face", (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255,255,255), "Face", clf)
            return img

        faceCascade =  cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # Detects Face (Haar Cascade Algo)
        clf=cv2.face.LBPHFaceRecognizer_create()  # LBPH algo , used to "recognize" . This algo is already trained in train.py
        # read from the classifier.xml file that has already been created in train.py file in line no. 58
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0) # 0 means default camera

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()      


if __name__ == "__main__" :
    root = Tk()
    obj=Face_Recognition(root)
    root.mainloop()

