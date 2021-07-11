from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Facial Recognition System")

         # ----------Variables--------
      
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_dept=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_sem=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_teacher=StringVar()
        self.var_photo=StringVar()

    
        # Background Image
        img=Image.open(r"images\background.jpg")
        img=img.resize((1920,1080),Image.ANTIALIAS)
        self.background=ImageTk.PhotoImage(img)

        bg_img=Label(root,image=self.background)
        bg_img.place(x=0,y=0)

        # Title
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("Merriweather",32,"bold"),bg="white",fg="teal")
        title_lbl.place(x=0,y=50,width=1530,height=50)

        # main Frame
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=0,y=150,width=1920,height=850)

        # Left Label Frame
        left_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        left_label_frame.place(x=10,y=10,width=660,height=530)

        # current course
        cur_course_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",15,"bold"))
        cur_course_frame.place(x=5,y=5,width=645,height=150)

        # Department
        dep_label=Label(cur_course_frame,text="Department",font=("times new roman",15,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=8,sticky=W)

        dep_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_dept,font=("times new roman",15,"bold"),state="readonly",width=17)
        dep_combo["values"]=("Select Department","CSE","ECE","Mech","EEE","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Course
        course_label=Label(cur_course_frame,text="Course",font=("times new roman",15,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=8,sticky=W)

        course_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_course,font=("times new roman",15,"bold"),state="readonly",width=12)
        course_combo["values"]=("Select Course","B-Tech","M-Tech","PHD")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Semester
        sem_label=Label(cur_course_frame,text="Semester",font=("times new roman",15,"bold"),bg="white")
        sem_label.grid(row=1,column=0,padx=8,sticky=W)

        sem_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_sem,font=("times new roman",15,"bold"),state="readonly",width=17)
        sem_combo["values"]=("Select Semester","Odd","Even")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(cur_course_frame,text="Year",font=("times new roman",15,"bold"),bg="white")
        year_label.grid(row=1,column=2,padx=8,sticky=W)

        year_combo=ttk.Combobox(cur_course_frame,textvariable=self.var_year,font=("times new roman",15,"bold"),state="readonly",width=12)
        year_combo["values"]=("Select Year","1st","2nd","3rd","4th","5th")
        year_combo.current(0)
        year_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Student Information
        student_frame=LabelFrame(left_label_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",15,"bold"))
        student_frame.place(x=5,y=180,width=645,height=315)

        # ID 
        sID_label=Label(student_frame,bg="white",text="SRN :",font=("times new roman",16,"bold"))
        sID_label.grid(row=0,column=0,padx=2,pady=10,sticky=W)

        sID_entry=ttk.Entry(student_frame,textvariable=self.var_id,width=16,font=("times new roman",13,"bold"))
        sID_entry.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        # Name
        sName_label=Label(student_frame,bg="white",text="Name :",font=("times new roman",16,"bold"))
        sName_label.grid(row=0,column=2,padx=4,pady=10,sticky=W)

        sName_entry=ttk.Entry(student_frame,textvariable=self.var_name,width=16,font=("times new roman",13,"bold"))
        sName_entry.grid(row=0,column=3,padx=4,pady=10,sticky=W)

        # Gender
        sGender_label=Label(student_frame,bg="white",text="Gender :",font=("times new roman",16,"bold"))
        sGender_label.grid(row=1,column=0,padx=2,pady=10,sticky=W)

        sGender_entry=ttk.Entry(student_frame,textvariable=self.var_gender,width=16,font=("times new roman",13,"bold"))
        sGender_entry.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Email
        sEmail_label=Label(student_frame,bg="white",text="Email ID :",font=("times new roman",16,"bold"))
        sEmail_label.grid(row=1,column=2,padx=4,pady=10,sticky=W)

        sEmail_entry=ttk.Entry(student_frame,textvariable=self.var_email,width=16,font=("times new roman",13,"bold"))
        sEmail_entry.grid(row=1,column=3,padx=4,pady=10,sticky=W)

        # Phone Number
        sPh_label=Label(student_frame,bg="white",text="Ph No :",font=("times new roman",16,"bold"))
        sPh_label.grid(row=2,column=0,padx=2,pady=10,sticky=W)

        sPh_entry=ttk.Entry(student_frame,textvariable=self.var_phone,width=16,font=("times new roman",13,"bold"))
        sPh_entry.grid(row=2,column=1,padx=2,pady=10,sticky=W)

        # Teacher
        sTeacher_label=Label(student_frame,bg="white",text="Teacher Name :",font=("times new roman",16,"bold"))
        sTeacher_label.grid(row=2,column=2,padx=4,pady=10,sticky=W)

        sTeacher_entry=ttk.Entry(student_frame,textvariable=self.var_teacher,width=16,font=("times new roman",13,"bold"))
        sTeacher_entry.grid(row=2,column=3,padx=4,pady=10,sticky=W)

        # Radio Button

        self.var_radioBtn1=StringVar()
        radioBtn1=ttk.Radiobutton(student_frame,variable=self.var_radioBtn1,text="With photo sample",value="Yes")
        radioBtn1.grid(row=4,column=0,pady=15,padx=8)

        radioBtn2=ttk.Radiobutton(student_frame,variable=self.var_radioBtn1,text="Without photo sample",value="No")
        radioBtn2.grid(row=4,column=1,padx=8,pady=15)


        # Button Frame
        btn_frame=Frame(student_frame,bg="white",bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=195,height=48,width=580)

        # Save Button
        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        save_btn.grid(row=0,column=0,padx=5.5,pady=10)

        # Update Button
        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        update_btn.grid(row=0,column=1,padx=5.5,pady=10)

        # Reset Button
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        reset_btn.grid(row=0,column=2,padx=5.5,pady=10)

        # Delete Button
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        delete_btn.grid(row=0,column=3,padx=5.5,pady=10)


        # New Button Frame
        Newbtn_frame=Frame(student_frame,bg="white",bd=2,relief=RIDGE)
        Newbtn_frame.place(x=0,y=245,height=45,width=580)

        # Take Photo Sample Button
        takePhoto_btn=Button(Newbtn_frame,command=self.generate_dataset,text="Take photo sample",width=27,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        takePhoto_btn.grid(row=0,column=0,padx=3,pady=2)

        # Update Photo Sample Button
        updatePhoto_btn=Button(Newbtn_frame,text="Update photo sample",width=27,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        updatePhoto_btn.grid(row=0,column=1,padx=3,pady=2)


        # Right Label Frame
        right_label_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",15,"bold"))
        right_label_frame.place(x=680,y=10,width=750,height=600)

        #  ------ Search System --------

        search_frame=LabelFrame(right_label_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Helvetica",15,"bold"))
        search_frame.place(x=5,y=5,width=730,height=95)

        search_label=Label(search_frame,text="Search By :",font=("Helvetica",13,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=5,pady=10,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=10)
        search_combo["values"]=("Select","Roll No","Name","Phone No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=5,pady=10,sticky=W)

        # Search Entry
        search_entry=ttk.Entry(search_frame,width=12,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=5,pady=10,sticky=W)

        # search btn
        search_btn=Button(search_frame,text="Search",width=9,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        search_btn.grid(row=0,column=3,padx=5,pady=10)

         # Show All Button
        showAll_btn=Button(search_frame,text="Show All",width=9,font=("times new roman",13,"bold"),fg="black",bg="lightgreen")
        showAll_btn.grid(row=0,column=4,padx=5,pady=10)

        # -------Table Frame-----
        table_frame=LabelFrame(right_label_frame,bd=2,bg="white",relief=RIDGE,text="Table Information",font=("times new roman",15,"bold"))
        table_frame.place(x=5,y=100,width=730,height=430)

        # Scroll Bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.studentTable=ttk.Treeview(table_frame,columns=("id","name","dep","course","year","sem","gender","email","phone","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.studentTable.xview)
        scroll_y.config(command=self.studentTable.yview)

        self.studentTable.heading("id",text="SRN")
        self.studentTable.heading("name",text="Name")
        self.studentTable.heading("dep",text="Department")
        self.studentTable.heading("course",text="Course")
        self.studentTable.heading("year",text="Year")
        self.studentTable.heading("sem",text="Sem")
        self.studentTable.heading("gender",text="Gender")
        self.studentTable.heading("email",text="Email ID")
        self.studentTable.heading("phone",text="Phone")
        self.studentTable.heading("teacher",text="Teacher")
        self.studentTable.heading("photo",text="Photo")
        self.studentTable["show"]="headings"

        self.studentTable.column("id",width=100)
        self.studentTable.column("name",width=100)
        self.studentTable.column("dep",width=100)
        self.studentTable.column("course",width=100)
        self.studentTable.column("year",width=100)
        self.studentTable.column("sem",width=100)
        self.studentTable.column("gender",width=100)
        self.studentTable.column("email",width=100)
        self.studentTable.column("phone",width=100)
        self.studentTable.column("teacher",width=100)
        self.studentTable.column("photo",width=100)

        self.studentTable.bind("<ButtonRelease>",self.get_cursor_data)
        self.fetch_data()

        self.studentTable.pack(fill=BOTH,expand=1)

    # --------Function Declarations--------
    def add_data(self):
      if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
            conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
            cur=conn.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(self.var_id.get(),self.var_name.get(),self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_teacher.get(),self.var_radioBtn1.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Student Details inserted",parent=self.root)
        except Exception as E:
            messagebox.showerror("Error",f"Issue : {str(E)}",parent=self.root)

    # -----Fetch Data------
    def fetch_data(self):
      conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
      cur=conn.cursor()
      cur.execute("select * from student")
      data=cur.fetchall()

      if len(data)!=0:
        self.studentTable.delete(*self.studentTable.get_children())
        for i in data:
          self.studentTable.insert("",END,values=i)
        conn.commit()
      conn.close()

    # -----Cursor Data----
    def get_cursor_data(self,event=""):
      idx=self.studentTable.focus()
      content=self.studentTable.item(idx)
      data=content["values"]

      self.var_id.set(data[0]),
      self.var_name.set(data[1]),
      self.var_dept.set(data[2]),
      self.var_course.set(data[3]),
      self.var_year.set(data[4]),
      self.var_sem.set(data[5]),
      self.var_gender.set(data[6]),
      self.var_email.set(data[7]),
      self.var_phone.set(data[8]),
      self.var_teacher.set(data[9]),
      self.var_radioBtn1.set(data[10])
    
    # ---------Update Data---------
    def update_data(self):
      if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="":
        messagebox.showerror("Error","All fields are required",parent=self.root)
      else:
        try:
          update=messagebox.askyesno("Update ?","Do you want to update",parent=self.root)
          if update>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
            cur=conn.cursor()
            cur.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Gender=%s,EmailID=%s,PhoneNo=%s,Teacher=%s,PhotoSample=%s where ID=%s",(
              self.var_name.get(),self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_gender.get(),
              self.var_email.get(),self.var_phone.get(),self.var_teacher.get(),self.var_radioBtn1.get(),self.var_id.get()
            ))
            messagebox.showinfo("Success","Student Details successfully updated",parent=self.root)
            conn.commit()
            self.fetch_data()
            conn.close()

          else:
            return 
        except Exception as E:
          messagebox.showerror("Error",f"Issue : {str(E)}")
      
    # ------Delete Data------
    def delete_data(self):
        if self.var_id.get()=='':
            messagebox.showerror("Error","Student ID is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Delete ?","Do you want to delete ?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
                    cur=conn.cursor()
                    query="delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    cur.execute(query,val)
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student Details successfully deleted",parent=self.root)
                else:
                    return
            except Exception as E:
                messagebox.showerror("Error",f"Issue : {str(E)}")
    
    # -----Reset Data----
    def reset_data(self):
      self.var_id.set("")
      self.var_name.set("")
      self.var_dept.set("Select Department")
      self.var_course.set("Select Course")
      self.var_year.set("Select Year")
      self.var_sem.set("Select Semester")
      self.var_gender.set("")
      self.var_email.set("")
      self.var_phone.set("")
      self.var_teacher.set("")
      self.var_radioBtn1.set("")

    # ================= Generate data set or Take Photos Sample ===========================================
    def generate_dataset(self):
        if self.var_dept.get()=="Select Department" or self.var_course.get()=="Select Course" or self.var_sem.get()=="Select Semester" or self.var_year.get()=="Select Year" or self.var_id.get()=="" or self.var_name.get()=="" or self.var_gender.get()=="" or self.var_email.get()=="" or self.var_phone.get()=="" or self.var_teacher.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="yourpassword",database="face_recognizer")
                cur=conn.cursor()
                cur.execute("select * from student")
                myresult=cur.fetchall()
                id=0
                for x in myresult:
                        id = id+1
                cur.execute("update student set Name=%s,Department=%s,Course=%s,Year=%s,Semester=%s,Gender=%s,EmailID=%s,PhoneNo=%s,Teacher=%s,PhotoSample=%s where ID=%s",(self.var_name.get(),self.var_dept.get(),self.var_course.get(),self.var_year.get(),self.var_sem.get(),self.var_gender.get(),self.var_email.get(),self.var_phone.get(),self.var_teacher.get(),self.var_radioBtn1.get(),self.var_id.get()==id+1))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # ===================================== Load predefined data on face frntals from opencv =============================
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # This file is used for face detection

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling Factor = 1.3
                    # Minimum Neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        # first create a folder called Data
                        file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face, str(img_id), (50,50) ,cv2.FONT_HERSHEY_COMPLEX , 2 , (0 ,255, 0) , 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1)==13 or int(img_id)==100: # 13 means ENTER button
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating Data Sets Completed!")
            
            except Exception as E:
                messagebox.showerror("Error",f"Due To : {str(E)}", parent=self.root)


if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.attributes("-fullscreen", True)
    root.bind("<F11>", lambda event: root.attributes("-fullscreen",not root.attributes("-fullscreen")))
    root.bind("<Escape>", lambda event: root.attributes("-fullscreen", False))
    root.mainloop()