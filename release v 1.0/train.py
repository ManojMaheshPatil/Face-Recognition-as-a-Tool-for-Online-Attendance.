from tkinter import*
from tkinter import ttk #Has stylish toolkits
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np

class Train:
    def __init__ (self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        title_lbl=Label(self.root,text="Train Dataset",font=("Merriweather",32,"bold"),bg="white",fg="teal")
        title_lbl.place(x=15,y=15,height=45,width=1230)

        img=Image.open(r"images/bgtrain.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.background=ImageTk.PhotoImage(img)

        bg_img=Label(root,image=self.background)
        bg_img.place(x=0,y=0)
        
        # Button

        t_btn=Button(self.root,text="Click Me to Train Data!👇",command=self.train_classifier,cursor="hand2",font=("Merriweather",25,"bold"),bg="lightblue",fg="black")
        t_btn.place(x=0,y=380,width=1530,height=60)

    # We will be using LBPH algorithm , refer video 5 for more explanation
    def train_classifier(self):
        data_dir =("data")
        path = [os.path.join(data_dir,file) for file in os.listdir(data_dir) ] # List Comprehension

        #create 2 empty lists
        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L') # This is an alternate way to convert to gray scale , the other is cv2.cvtColor_BGR2GRAY
            imageNp = np.array(img,'uint8') # uint8 is a datatyep  , we do this step to convert images to grid format (refer video 5 time 40:23)
            id = int(os.path.split(image)[1].split('.')[1])   # This takes only the id from the big name of the image

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        
        ids=np.array(ids) # We use numpy because the performance is better in conversion of array

        # =========================== Train Classifier ======================================
        #create an object
        clf = cv2.face.LBPHFaceRecognizer_create()
        # now train the file , LBPH algorithm uses 2 parameters faces and their ids , always the same face should have same id
        clf.train(faces , ids)
        # now write this in a file
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Data Sets Completed!!!")








 




if __name__ == "__main__" :
    root = Tk()
    obj=Train(root)
    root.mainloop()