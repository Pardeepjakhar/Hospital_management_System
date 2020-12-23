from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox,filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter.ttk import Treeview
import pymysql
import time

def creat():
    user = usernameentry.get()
    passwor = passwordentry.get()
    if user == '' or passwor == '':
        messagebox.showerror("Error", "username password not be null")
    else:
        try:
            strrr = '''select * from usernamepassword'''
            mycursor.execute(strrr)
            res = mycursor.fetchall()

            for i in res:
                vv1 = i[0]
                vv2 = i[1]
                if user == vv1 and passwor == vv2:
                    messagebox.showinfo("Notification", "Successfully Login")
                    usernameentry.set('')
                    passwordentry.set('')
                    root.withdraw()
                    def Home():
                        homeame = Frame(hroot, bg="green")
                        homeame.place(x=145, y=53, width=1190, height=750)

                        dashbord = Label(hroot, text="Admin Deshboard", font="arial 15 bold", bg="gray")
                        dashbord.place(x=145, y=53, width=1190)
                        cdate=time.strftime("%d/%m/%y")
                        strr="select count(Id) from Patient where appointdate=%s"
                        mycursor.execute(strr,cdate)
                        p=mycursor.fetchall()
                        for i in p:
                           vv=[i[0]]
                        specilazationlabel = Label(hroot, text="Specialization\n", font="lucida 15 bold", bg="orange",fg="white")
                        specilazationlabel.place(x=170, y=100, width=250, height=90)

                        strr = "select count(DISTINCT DoctorSpecilization) from patient where appointdate=%s"
                        mycursor.execute(strr, cdate)
                        p = mycursor.fetchall()
                        for i in p:
                            vv = [i[0]]

                        p = vv
                        speclabel = Label(specilazationlabel, text="", font="lucida 15 bold", bg="orange", fg="black")
                        speclabel.place(x=100, y=50, width=30, height=30)
                        speclabel.config(text=p)



                        Doctorlabel = Label(hroot, text="Doctors\n ", font="lucida 15 bold", bg="skyblue", fg="white")
                        Doctorlabel.place(x=450, y=100, width=250, height=90)

                        strr = "select count(DISTINCT Appointdoctor) from patient where appointdate=%s"
                        mycursor.execute(strr, cdate)
                        p = mycursor.fetchall()
                        for i in p:
                            vv = [i[0]]

                        p = vv

                        Doctorlabel = Label(hroot,text="", font="lucida 15 bold", bg="skyblue", fg="black")
                        Doctorlabel.place(x=560, y=150, width=30, height=30)
                        Doctorlabel.config(text=p)


                        Patientlabel = Label(hroot, text="Patient\n", font="lucida 15 bold", bg="yellow", fg="white")
                        Patientlabel.place(x=750, y=100, width=250, height=90)
                        strr = "select count(PName) from patient where appointdate=%s"
                        mycursor.execute(strr, cdate)
                        p = mycursor.fetchall()
                        for i in p:
                            vv = [i[0]]

                        p = vv
                        speclabel = Label(Patientlabel, text="", font="lucida 15 bold", bg="yellow", fg="black")
                        speclabel.place(x=100, y=50, width=30, height=30)
                        speclabel.config(text=p)


                        Todaysappointmentlabel = Label(hroot, text="Today's Appontments\n", font="lucida 15 bold",
                                                       bg="cyan", fg="white")
                        Todaysappointmentlabel.place(x=1050, y=100, width=250, height=90)
                        strr = "select count(Id) from patient where appointdate=%s"
                        mycursor.execute(strr, cdate)
                        p = mycursor.fetchall()
                        for i in p:
                            vv = [i[0]]

                        p = vv
                        speclabel = Label(Todaysappointmentlabel, text="", font="lucida 15 bold", bg="cyan", fg="black")
                        speclabel.place(x=100, y=50, width=30, height=30)
                        speclabel.config(text=p)

                        todayappontmentframe = PanedWindow(hroot, orient=HORIZONTAL)
                        todayappontmentframe.place(x=170, y=200, width=1150, height=480)
                        style = ttk.Style()
                        style.configure("Treeview.Heading", font="lucida 13 bold", fg="black2")
                        style.configure("Treeview", fg="black", bg="red", font="times 13 bold")
                        scroll_y = Scrollbar(todayappontmentframe, orient=VERTICAL)
                        scroll_x = Scrollbar(todayappontmentframe, orient=HORIZONTAL)

                        hometable = Treeview(todayappontmentframe, column=(
                            "PatientId", "PatientName", "Patientcontact", "Symptoms", "DoctorSpecilization",
                            "AppointDoctor", "D.O.B", "Added Date", "Added Time"),
                                             yscrollcommand=scroll_y.set,
                                             xscrollcommand=scroll_x.set)

                        scroll_x.pack(side=BOTTOM, fill=X)
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_x.config(command=hometable.xview)
                        scroll_y.config(command=hometable.yview)
                        hometable.heading("PatientId", text="Id")
                        hometable.heading("PatientName", text="PatientName")
                        hometable.heading("Patientcontact", text="Patientcontact")
                        hometable.heading("Symptoms", text="Symptoms")
                        hometable.heading("DoctorSpecilization", text="DoctorSpecilization")
                        hometable.heading("AppointDoctor", text="AppointDoctor")
                        hometable.heading("D.O.B", text="D.O.B")
                        hometable.heading("Added Date", text="Date")
                        hometable.heading("Added Time", text="Time")
                        hometable["show"] = "headings"
                        hometable.pack(fill=BOTH, expand=1)
                        hometable.column("PatientId", width=50)
                        hometable.column("PatientName", width=180)
                        hometable.column("Patientcontact", width=150)
                        hometable.column("Symptoms", width=200)
                        hometable.column("DoctorSpecilization", width=220)
                        hometable.column("AppointDoctor", width=150)
                        hometable.column("D.O.B", width=100)
                        hometable.column("Added Date", width=100)
                        hometable.column("Added Time", width=100)
                        strr = "select * from Patient where appointdate=%s"
                        mycursor.execute(strr,cdate)
                        datas = mycursor.fetchall()
                        hometable.delete(*hometable.get_children())
                        for i in datas:
                            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[10], i[11]]
                            hometable.insert('', END, values=vv)

                    def Doctor():


                        def add():
                            global list
                            id=identry.get()
                            spec = specilizationentry.get()
                            spname = nameentry.get()
                            fees = consoltencyentry.get()
                            contact = Contactentry.get()
                            email = emailentry.get()
                            addres = addressentry.get()
                            cdate=time.strftime("%d/%m/%y")
                            if id=='':
                                messagebox.showerror('Notification',"Id must have an element")
                            else:
                             try:
                                strr = "insert into doctor(Id,specilization,Doctorname,address,fees,contactno,email,creationdate) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                                val = (id,spec, spname, addres, fees, contact, email,cdate)
                                mycursor.execute(strr,val)
                                con.commit()
                                messagebox.showinfo("Notification", "ID added successfully" )

                             except:
                                messagebox.showerror("error","Id already exist" )

                             strr = "select * from doctor"
                             mycursor.execute(strr)
                             datas = mycursor.fetchall()
                             Managedoctortable.delete(*Managedoctortable.get_children())
                             for i in datas:
                                vv = [i[0], i[1], i[4], i[5], i[6], i[7], i[8], i[2], i[3]]
                                Managedoctortable.insert('', END, values=vv)

                             list=[]
                             strr="select * from doctor where specilization=%s"
                             mycursor.execute(strr,spec)
                             datas=mycursor.fetchall()
                             Managedoctortable.delete(*Managedoctortable.get_children())
                             for i in datas:
                                 vv=[i[1]]
                                 Managedoctortable.insert('',END,values=vv)



                        def clear():
                            identry.set('')
                            specilizationentry.set('')
                            nameentry.set('')
                            consoltencyentry.set('')
                            Contactentry.set('')
                            emailentry.set('')
                            addressentry.set('')

                        def update():
                            id=identry.get()
                            spec = specilizationentry.get()
                            spname = nameentry.get()
                            fees = consoltencyentry.get()
                            contact = Contactentry.get()
                            email = emailentry.get()
                            addres = addressentry.get()
                            cdate = time.strftime("%d/%m/%y")
                            updatedate=time.strftime("%d/%m/%y")

                            strr="update doctor set specilization=%s,Doctorname=%s,address=%s,fees=%s,contactno=%s,email=%s,creationdate=%s, updationdate=%s where Id=%s"
                            mycursor.execute(strr,(spec,spname,addres,fees,contact,email,cdate,updatedate,id))
                            con.commit()
                            messagebox.showinfo("Notificarion","Id {} is update successfully".format(id))
                            strr="select * from doctor"
                            mycursor.execute(strr)
                            datas=mycursor.fetchall()
                            Managedoctortable.delete(*Managedoctortable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[4], i[5], i[6], i[7], i[8], i[2], i[3]]
                                Managedoctortable.insert('', END, values=vv)



                        def delete():
                            cc=Managedoctortable.focus()
                            contetn=Managedoctortable.item(cc)
                            pp=contetn['values'][0]
                            str="delete from doctor where Id=%s"
                            mycursor.execute(str,pp)
                            con.commit()
                            messagebox.showinfo("Notification ","ID {} is deleted successfully ".format(pp))
                            strr="select * from doctor"
                            mycursor.execute(strr)
                            datas=mycursor.fetchall()
                            Managedoctortable.delete(*Managedoctortable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[4], i[5], i[6], i[7], i[8], i[2], i[3]]
                                Managedoctortable.insert('', END, values=vv)


                        def showall():
                            strr="select * from doctor"
                            mycursor.execute(strr)
                            datas=mycursor.fetchall()
                            Managedoctortable.delete(*Managedoctortable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[4], i[5], i[6], i[7], i[8], i[2], i[3]]
                                Managedoctortable.insert('', END, values=vv)

                        def search():
                            name=doctorentry.get()
                            if name!='':
                                strr="select * from doctor where Doctorname=%s"
                                mycursor.execute(strr,name)
                                datas=mycursor.fetchall()
                                Managedoctortable.delete(*Managedoctortable.get_children())
                                for i in datas:
                                    vv = [i[0], i[1], i[4], i[5], i[6], i[7], i[8], i[2], i[3]]
                                    Managedoctortable.insert('', END, values=vv)

                        def click(event):
                            cc = Managedoctortable.focus()
                            contetn = Managedoctortable.item(cc)
                            pp = contetn['values']
                            if len(pp):
                                identry.set(pp[0])
                                specilizationentry.set(pp[1])
                                nameentry.set(pp[2])
                                consoltencyentry.set(pp[4])
                                Contactentry.set(pp[5])
                                emailentry.set(pp[6])
                                addressentry.set(pp[3])

                        doctorframe = Frame(hroot, bg="green")
                        doctorframe.place(x=145, y=53, width=1190, height=750)

                        board = Label(doctorframe, text="Doctor deshboard", font="arial 15 bold", bg="gray")
                        board.place(x=5, y=15, width=1190)

                        doctorframe = PanedWindow(hroot, orient=VERTICAL, bg="orange")
                        doctorframe.place(x=145, y=100, width=1190, height=750)
                        identry = StringVar()
                        specilizationentry = StringVar()
                        nameentry = StringVar()
                        consoltencyentry = StringVar()
                        Contactentry = StringVar()
                        emailentry = StringVar()
                        addressentry = StringVar()
                        doctorentry = StringVar()

                        managedoctorframe = LabelFrame(doctorframe, text="Add Doctor", bg="white", font="arial 15 bold")
                        managedoctorframe.place(x=10, y=30, width=450, height=550)
                        idlabel = Label(managedoctorframe, text="Id", bg="white", font="arial 14 bold")
                        idlabel.place(x=10, y=10)
                        idvalue = Entry(managedoctorframe, textvariable=identry, bd=4, font="arial 14 bold")
                        idvalue.place(x=170, y=10)

                        specilazitionlabel = Label(managedoctorframe, text="Specilization", bg="white",
                                                   font="arial 14 bold")
                        specilazitionlabel.place(x=10, y=70)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=specilizationentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=70)

                        specilazitionlabel = Label(managedoctorframe, text="Name ", bg="white", font="arial 14 bold")
                        specilazitionlabel.place(x=10, y=130)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=nameentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=130)

                        specilazitionlabel = Label(managedoctorframe, text="Consoltensy fees", bg="white",
                                                   font="arial 14 bold")
                        specilazitionlabel.place(x=5, y=190)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=consoltencyentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=190)

                        specilazitionlabel = Label(managedoctorframe, text="Contact No", bg="white",
                                                   font="arial 14 bold")
                        specilazitionlabel.place(x=10, y=250)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=Contactentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=250)

                        specilazitionlabel = Label(managedoctorframe, text="Email", bg="white", font="arial 14 bold")
                        specilazitionlabel.place(x=10, y=310)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=emailentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=310)

                        specilazitionlabel = Label(managedoctorframe, text="Address", bg="white", font="arial 14 bold")
                        specilazitionlabel.place(x=10, y=370)
                        specilazitionvalue = Entry(managedoctorframe, textvariable=addressentry, bd=4,
                                                   font="arial 14 bold")
                        specilazitionvalue.place(x=170, y=370, height=70)

                        speciliztionbtn = Button(managedoctorframe, text="ADD", bg="skyblue", font="lucida 15 bold",command=add)
                        speciliztionbtn.place(x=10, y=470, width=100)

                        speciliztionbtn = Button(managedoctorframe, text="update", bg="green", font="lucida 15 bold",command=update)
                        speciliztionbtn.place(x=120, y=470, width=100)
                        speciliztionbtn = Button(managedoctorframe, text="clear", bg="red", font="lucida 15 bold",command=clear)
                        speciliztionbtn.place(x=230, y=470, width=100)
                        speciliztionbtn = Button(managedoctorframe, text="Delete", bg="gray", font="lucida 15 bold",command=delete)
                        speciliztionbtn.place(x=340, y=470, width=100)

                        w1 = LabelFrame(doctorframe, text="Doctor Details", font="arial 15 bold")
                        w1.place(x=500, y=30, width=650, height=550)
                        doctorlabel = Label(w1, text="Enter Doctor Name", font="arial 15 bold")
                        doctorlabel.place(x=20, y=20)
                        doctorval = Entry(w1, textvariable=doctorentry, bd=4, font="arial 14 bold")
                        doctorval.place(x=220, y=20)
                        docsearch = Button(w1, text="Search", bg="blue", font="arial 12 bold",command=search)
                        docsearch.place(x=460, y=20)
                        docsearch = Button(w1, text="Show All", bg="orange", font="arial 12 bold",command=showall)
                        docsearch.place(x=540, y=20)
                        docdetailframe = Frame(w1, bg="green", borderwidth=6)
                        docdetailframe.place(x=10, y=80, width=620, height=450)
                        scroll_y = Scrollbar(docdetailframe, orient=VERTICAL)
                        scroll_x = Scrollbar(docdetailframe, orient=HORIZONTAL)

                        Managedoctortable = Treeview(docdetailframe, column=(
                            "Id", "Specilization", "Doctor Name", "Address", "Fees", "ContactNo", "Email",
                            "Creation Date", "Updation Date"),
                                                     yscrollcommand=scroll_y.set,
                                                     xscrollcommand=scroll_x.set)

                        scroll_x.pack(side=BOTTOM, fill=X)
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_x.config(command=Managedoctortable.xview)
                        scroll_y.config(command=Managedoctortable.yview)
                        Managedoctortable.heading("Id", text="Id")
                        Managedoctortable.heading("Specilization", text="Specilization")
                        Managedoctortable.heading("Doctor Name", text="Doctor Name")
                        Managedoctortable.heading("Address", text="Address")
                        Managedoctortable.heading("Fees", text="Fees")
                        Managedoctortable.heading("ContactNo", text="ContactNo")
                        Managedoctortable.heading("Email", text="Email")
                        Managedoctortable.heading("Creation Date", text="Creation Date")
                        Managedoctortable.heading("Updation Date", text="Updation Date")
                        Managedoctortable["show"] = "headings"
                        Managedoctortable.pack(fill=BOTH, expand=1)
                        Managedoctortable.column("Id", width=50)
                        Managedoctortable.column("Specilization", width=180)
                        Managedoctortable.column("Doctor Name", width=120)
                        Managedoctortable.column("Address", width=200)
                        Managedoctortable.column("Fees", width=150)
                        Managedoctortable.column("ContactNo", width=150)
                        Managedoctortable.column("Email", width=200)
                        Managedoctortable.column("Creation Date", width=150)
                        Managedoctortable.column("Updation Date", width=150)
                        Managedoctortable.bind("<ButtonRelease-1>",click)


                    def Patient():
                        def add():
                            id=PatientIdentry.get()
                            pname=Patientnameentry.get()
                            gender=Genderentry.get()
                            dob=dobentry.get()
                            contact=Conatctpatieentry.get()
                            email=psentEmailentry.get()
                            addres=pasentaddres.get()
                            symptoms=Symptomsentry.get()
                            doctor=selectdoctorentry.get()
                            spec=specilizationdoc.get()
                            date=time.strftime("%d/%m/%y")
                            ctime=time.strftime("%H:%M:%S")
                            print(spec)

                            try:
                                strr="insert into Patient(Id,Pname,Pcontact,Symptoms,DoctorSpecilization, Appointdoctor,DOB,gender,Email,address,appointdate,appointtime)values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                val=(id,pname,contact,symptoms,spec,doctor,dob,gender,email,addres,date,ctime)
                                mycursor.execute(strr,val)
                                con.commit()
                                messagebox.showinfo("Notofication ","Id added successfully")


                            except:
                                messagebox.showerror("Error","ID already exist")

                            strr = "select * from Patient"
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            patienttable.delete(*patienttable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                patienttable.insert('', END, values=vv)

                        def delete():
                            cc=patienttable.focus()
                            content=patienttable.item(cc)
                            pp=content['values'][0]
                            strr="delete from Patient where Id=%s"
                            mycursor.execute(strr,pp)
                            con.commit()
                            messagebox.showinfo("Notification","Id {} is deleted successfully".format(pp))
                            strr="select * from Patient"
                            mycursor.execute(strr)
                            datas=mycursor.fetchall()
                            patienttable.delete(*patienttable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                patienttable.insert('', END, values=vv)

                        def update():
                            id = PatientIdentry.get()
                            pname = Patientnameentry.get()
                            gender = Genderentry.get()
                            dob = dobentry.get()
                            contact = Conatctpatieentry.get()
                            email = psentEmailentry.get()
                            addres = pasentaddres.get()
                            symptoms = Symptomsentry.get()
                            doctor = selectdoctorentry.get()
                            spec=specilizationdoc.get()
                            date = time.strftime("%d/%m/%y")
                            ctime = time.strftime("%H:%M:%S")

                            strr="update Patient set Pname=%s,Pcontact=%s,Symptoms=%s,DoctorSpecilization=%s, Appointdoctor=%s,DOB=%s,gender=%s,Email=%s,address=%s,appointdate=%s,appointtime=%s where Id=%s"
                            mycursor.execute(strr,(pname,contact,symptoms,spec,doctor,dob,gender,email,addres,date,ctime,id))
                            con.commit()
                            messagebox.showinfo("Notification","ID is updated successfully")
                            strr = "select * from Patient"
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            patienttable.delete(*patienttable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                patienttable.insert('', END, values=vv)




                        def clear():

                            PatientIdentry.set('')
                            Patientnameentry.set('')
                            Genderentry.set('')
                            dobentry.set('')
                            Conatctpatieentry.set('')
                            psentEmailentry.set('')
                            pasentaddres.set('')
                            Symptomsentry.set('')
                            selectdoctorentry.set('')
                            specilizationdoc.set('')
                        def search():
                            sname=searcname.get()
                            if sname!='':
                                strr="select * from Patient where PName=%s"
                                mycursor.execute(strr,sname)
                                datas=mycursor.fetchall()
                                patienttable.delete(*patienttable.get_children())
                                for i in datas:
                                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                    patienttable.insert('', END, values=vv)

                        def showall():
                            strr = "select * from Patient"
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            patienttable.delete(*patienttable.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11]]
                                patienttable.insert('', END, values=vv)

                        def cler():
                            searcname.set('')

                        def click(event):
                            cc = patienttable.focus()
                            content = patienttable.item(cc)
                            pp = content['values']
                            if len(pp):
                                PatientIdentry.set(pp[0])
                                Patientnameentry.set(pp[1])
                                Genderentry.set(pp[7])
                                dobentry.set(pp[6])
                                specilizationdoc.set(pp[4])
                                Conatctpatieentry.set(pp[2])
                                psentEmailentry.set(pp[8])
                                pasentaddres.set(pp[9])
                                Symptomsentry.set(pp[5])
                                selectdoctorentry.set(pp[3])



                        PatientIdentry=StringVar()
                        Patientnameentry = StringVar()
                        Genderentry = StringVar()
                        dobentry = StringVar()
                        Conatctpatieentry = StringVar()
                        psentEmailentry = StringVar()
                        pasentaddres = StringVar()
                        Symptomsentry = StringVar()
                        selectdoctorentry = StringVar()
                        specilizationdoc=StringVar()
                        dateentry = StringVar()
                        tiementry = StringVar()
                        searcname=StringVar()

                        pwin = PanedWindow(hroot,orient=VERTICAL)
                        pwin.place(x=145, y=53, width=1190, height=750)

                        board = Label(pwin, text="Manage Patient", font="arial 15 bold", bg="gray")
                        board.place(x=5, y=0, width=1190)

                        pd = LabelFrame(pwin,text="Patient Details",font="arial 15 bold")
                        pd.place(x=10, y=50, width=350, height=370)

                        patientlabel = Label(pd, text="Patient Id", font="lucida 13 bold")
                        patientlabel.place(x=10, y=10)
                        patientval = Entry(pd, textvariable=PatientIdentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=10)

                        patientlabel = Label(pd, text="Patient Name", font="lucida 13 bold" )
                        patientlabel.place(x=10, y=50)
                        patientval = Entry(pd, textvariable=Patientnameentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=50)

                        patientlabel = Label(pd, text="Gender", font="lucida 13 bold")
                        patientlabel.place(x=10, y=90)
                        patientval = Entry(pd, textvariable=Genderentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=90)

                        patientlabel = Label(pd, text="D.O.B", font="lucida 13 bold" )
                        patientlabel.place(x=10, y=130)
                        patientval = Entry(pd, textvariable=dobentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=130)

                        patientlabel = Label(pd, text="Contact NO", font="lucida 13 bold" )
                        patientlabel.place(x=10, y=170)
                        patientval = Entry(pd, textvariable=Conatctpatieentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=170)

                        patientlabel = Label(pd, text="Email", font="lucida 13 bold" )
                        patientlabel.place(x=10, y=210)
                        patientval = Entry(pd, textvariable=psentEmailentry, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=210)

                        patientlabel = Label(pd, text="Address", font="lucida 13 bold" )
                        patientlabel.place(x=10, y=250)
                        patientval = Entry(pd, textvariable=pasentaddres, font="arial 13 bold", bd=3)
                        patientval.place(x=140, y=250, height=50)

                        appointdoctor = LabelFrame(pwin, text="Appoint Doctor",font=("arial 15 bold"))
                        appointdoctor.place(x=400, y=50, width=800, height=350)
                        sytmlabel = Label(appointdoctor, text="Symptoms", font="lucida 15 bold" )
                        sytmlabel.place(x=10, y=30)
                        sytmval = Entry(appointdoctor, textvariable=Symptomsentry, bd=3, font="arial 13 bold")
                        sytmval.place(x=150, y=30, height=70)

                        apointdoct = Label(appointdoctor, text="Select to appoint Doctor", font="arial 15 bold")
                        apointdoct.place(x=400, y=30)




                        list = []
                        doctorchoose = ttk.Combobox(appointdoctor, textvariable=specilizationdoc, width=30)


                        strr = "select * from doctor "
                        mycursor.execute(strr)
                        datas = mycursor.fetchall()

                        for i in datas:
                            vv = [i[1]]
                            list.append(vv)
                        doctorchoose['values'] = (list)
                        doctorchoose.place(x=410, y=70)
                        doctorchoose.current()
                        doctorchoose.bind("<ButtonRelease-1>")
                        doctorchoosen = ttk.Combobox(appointdoctor, textvariable=selectdoctorentry, width=30)

                        list2 = []

                        strr = "select * from doctor "
                        mycursor.execute(strr)
                        datas = mycursor.fetchall()

                        for i in datas:
                            vv = [i[4]]
                            list2.append(vv)
                        doctorchoosen['values'] = (list2)
                        doctorchoosen.place(x=410, y=100)
                        doctorchoosen.current()

                        datelabel = Label(appointdoctor, text="Enter Date(DD/MM/YYYY)",
                                          font="arial 13 bold")
                        datelabel.place(x=10, y=140)
                        dateval = Entry(appointdoctor, textvariable=dateentry, bd=3, font="aria 15 bold")
                        dateval.place(x=10, y=170)

                        timelabel = Label(appointdoctor, text="Enter Time(HH:MM:SS)",font="arial 13 bold")
                        timelabel.place(x=350, y=140)
                        timeval = Entry(appointdoctor, textvariable=tiementry, bd=3, font="aria 15 bold")
                        timeval.place(x=350, y=170)

                        btn = Button(appointdoctor, text="Add", bg="cyan", font="arial 13 bold",command=add)
                        btn.place(x=10, y=280, width=170)
                        btn = Button(appointdoctor, text="Update", bg="green", font="arial 13 bold",command=update)
                        btn.place(x=210, y=280, width=170)
                        btn = Button(appointdoctor, text="Delete", bg="red", font="arial 13 bold",command=delete)
                        btn.place(x=410, y=280, width=170)
                        btn = Button(appointdoctor, text="Clear", bg="gray", font="arial 13 bold",command=clear)
                        btn.place(x=610, y=280, width=170)

                        patientwindoe = LabelFrame(pwin,text="Patient Details",font="arila 15 bold" )
                        patientwindoe.place(x=10, y=420, width=1200, height=220)

                        patientdetailslabel = Label(patientwindoe, text="Enter Patient Name", font="arial 15 bold")
                        patientdetailslabel.place(x=20, y=25)

                        patientval = Entry(patientwindoe, textvariable=searcname, font="arial 15 bold", bd=4)
                        patientval.place(x=230, y=20)

                        seachbtn = Button(patientwindoe, text="Search", font="arial 13 bold", bg="blue",command=search)
                        seachbtn.place(x=500, y=20)
                        seachbtn = Button(patientwindoe, text="Clear", font="arial 13 bold", bg="gray",command=cler)
                        seachbtn.place(x=600, y=20)
                        seachbtn = Button(patientwindoe, text="Show All", font="arial 13 bold", bg="orange",command=showall)
                        seachbtn.place(x=700, y=20)

                        patientframe = Frame(patientwindoe, bg="white")
                        patientframe.place(x=5, y=70, width=1150, height=130)
                        scroll_y = Scrollbar(patientframe, orient=VERTICAL)
                        scroll_x = Scrollbar(patientframe, orient=HORIZONTAL)

                        patienttable = Treeview(patientframe, column=( "Id", "PatientName", "Patientcontact", "Symptoms", "DoctorSpecilization",
                            "AppointDoctor","D.O.B", "Gender", "Email", "Address","Date", "Time"),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)

                        scroll_x.pack(side=BOTTOM, fill=X)
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_x.config(command=patienttable.xview)
                        scroll_y.config(command=patienttable.yview)
                        patienttable.heading("Id", text="Id")
                        patienttable.heading("PatientName", text="PatientName")
                        patienttable.heading("Patientcontact", text="Patientcontact")
                        patienttable.heading("Symptoms", text="Symptoms")
                        patienttable.heading("DoctorSpecilization", text="DoctorSpecilization")
                        patienttable.heading("AppointDoctor", text="AppointDoctor")
                        patienttable.heading("D.O.B", text="D.O.B")
                        patienttable.heading("Gender", text="Gender")
                        patienttable.heading("Email", text="Email")
                        patienttable.heading("Address", text="Address")
                        patienttable.heading("Date", text="Appt Date")
                        patienttable.heading("Time", text="Appt Time")
                        patienttable["show"] = "headings"
                        patienttable.pack(fill=BOTH, expand=1)
                        patienttable.column("Id", width=50)
                        patienttable.column("PatientName", width=180)
                        patienttable.column("Patientcontact", width=150)
                        patienttable.column("Symptoms", width=200)
                        patienttable.column("DoctorSpecilization", width=200)
                        patienttable.column("AppointDoctor", width=150)
                        patienttable.column("D.O.B", width=100)
                        patienttable.column("Gender", width=100)
                        patienttable.column("Email", width=200)
                        patienttable.column("Address", width=200)
                        patienttable.column("Date", width=100)
                        patienttable.column("Time", width=100)
                        patienttable.bind("<ButtonRelease-1>",click)


                    def appointment():
                        def allappontment():
                            strr = "select * from Patient"
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            Appontmenttabel.delete(*Appontmenttabel.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[10], i[11]]
                                Appontmenttabel.insert('', END, values=vv)

                        def deletetodayap():
                            cdate=time.strftime("%d/%m/%y")

                            strr="delete from Patient where appointdate=%s"
                            mycursor.execute(strr,cdate)
                            messagebox.showinfo("Notificaion","Deleted todays appointment successfully")
                            strr = "select * from Patient"
                            mycursor.execute(strr)
                            datas = mycursor.fetchall()
                            Appontmenttabel.delete(*Appontmenttabel.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6],  i[10], i[11]]
                                Appontmenttabel.insert('', END, values=vv)

                        def todayapontment():
                            cdate = time.strftime("%d/%m/%y")
                            print(cdate)
                            strr = "select * from Patient where appointdate=%s"
                            mycursor.execute(strr, cdate)
                            con.commit()
                            datas = mycursor.fetchall()
                            Appontmenttabel.delete(*Appontmenttabel.get_children())
                            for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[10], i[11]]
                                Appontmenttabel.insert('', END, values=vv)
                            messagebox.showinfo("Notificaion", "Todays appointment ")

                        def deleteall():
                            res=messagebox.askyesno("Notification","Are you realy want to delelte")
                            if res==True:
                             strr = "delete from Patient"
                             mycursor.execute(strr)
                             messagebox.showinfo("Notificaion", "Deleted   successfully")
                             strr = "select * from Patient"
                             mycursor.execute(strr)
                             datas = mycursor.fetchall()
                             Appontmenttabel.delete(*Appontmenttabel.get_children())
                             for i in datas:
                                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[10], i[11]]
                                Appontmenttabel.insert('', END, values=vv)

                        def search():
                            entry=Patientnameentry.get()
                            if entry!='':
                                strr="select * from Patient where PName=%s"
                                mycursor.execute(strr,entry)
                                datas = mycursor.fetchall()
                                Appontmenttabel.delete(*Appontmenttabel.get_children())
                                for i in datas:
                                    vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6] , i[10], i[11]]
                                    Appontmenttabel.insert('', END, values=vv)

                        def clear():
                            Patientnameentry.set('')

                        Patientnameentry = StringVar()
                        pwin = PanedWindow(hroot, orient=HORIZONTAL)
                        pwin.place(x=145, y=53, width=1190, height=750)

                        board = Label(pwin, text="Patient | Appointment Histroy", font="arial 15 bold", bg="gray")
                        board.place(x=5, y=0, width=1190)

                        pd =LabelFrame(pwin,text="Search Appointment", bg="white",font="arial 12 bold")
                        pd.place(x=10, y=50, width=1150, height=80)

                        patientlabel = Label(pd, text="Patient Name :",bg="white", font="lucida 15 bold")
                        patientlabel.place(x=10, y=15)

                        patientval = Entry(pd, textvariable=Patientnameentry, font="lucida 13 bold", bd=5)
                        patientval.place(x=200, y=15)

                        searcjbtn = Button(pd, text="Search", font="lucida 13 bold", bg="blue",command=search)
                        searcjbtn.place(x=420, y=15, width=100)
                        searcjbtn = Button(pd, text="Clear", font="lucida 13 bold", bg="gray",command=clear)
                        searcjbtn.place(x=600, y=15, width=100)

                        pds =LabelFrame(pwin, text="AppointMent", bg="white",font="arial 15 bold")
                        pds.place(x=10, y=160, width=1150, height=80)

                        btn = Button(pds, text="Show today's appointment", font="arial 13 bold", bg="cyan",command=todayapontment)
                        btn.place(x=10, y=10, width=220)
                        btn = Button(pds, text="Show All appointment", font="arial 13 bold", bg="darkgreen",command=allappontment)
                        btn.place(x=300, y=10, width=220)
                        btn = Button(pds, text="Delete All", font="arial 13 bold", bg="red",command=deleteall)
                        btn.place(x=600, y=10, width=220)
                        btn = Button(pds, text="Delete today's History ", font="arial 13 bold", bg="cyan",command=deletetodayap)
                        btn.place(x=900, y=10, width=220)

                        pdst = PanedWindow(pwin, orient=VERTICAL, bg="white", bd=6)
                        pdst.place(x=10, y=260, width=1150, height=350)
                        scroll_y = Scrollbar(pdst, orient=VERTICAL)
                        scroll_x = Scrollbar(pdst, orient=HORIZONTAL)

                        Appontmenttabel = Treeview(pdst, column=(
                            "PatientId", "PatientName", "Patientcontact", "Symptoms", "DoctorSpecilization",
                            "AppointDoctor",
                            "D.O.B",
                            "Added Date", "Added Time"),
                                                   yscrollcommand=scroll_y.set,
                                                   xscrollcommand=scroll_x.set)

                        scroll_x.pack(side=BOTTOM, fill=X)
                        scroll_y.pack(side=RIGHT, fill=Y)
                        scroll_x.config(command=Appontmenttabel.xview)
                        scroll_y.config(command=Appontmenttabel.yview)
                        Appontmenttabel.heading("PatientName", text="PId")
                        Appontmenttabel.heading("Patientcontact", text="Patientcontact")
                        Appontmenttabel.heading("PatientId", text="PatientId")
                        Appontmenttabel.heading("Symptoms", text="Symptoms")
                        Appontmenttabel.heading("DoctorSpecilization", text="DoctorSpecilization")
                        Appontmenttabel.heading("AppointDoctor", text="AppointDoctor")
                        Appontmenttabel.heading("D.O.B", text="D.O.B")
                        Appontmenttabel.heading("Added Date", text="Date")
                        Appontmenttabel.heading("Added Time", text="Time")
                        Appontmenttabel["show"] = "headings"
                        Appontmenttabel.pack(fill=BOTH, expand=1)
                        Appontmenttabel.column("PatientName", width=50)
                        Appontmenttabel.column("PatientName", width=180)
                        Appontmenttabel.column("Patientcontact", width=150)
                        Appontmenttabel.column("Symptoms", width=200)
                        Appontmenttabel.column("DoctorSpecilization", width=200)
                        Appontmenttabel.column("AppointDoctor", width=100)
                        Appontmenttabel.column("D.O.B", width=100)
                        Appontmenttabel.column("Added Date", width=100)
                        Appontmenttabel.column("Added Time", width=100)

                    def Logout():
                        res=messagebox.askyesno("Notification","Are you want to logout or not")
                        if (res==True):
                            hroot.destroy()
                            root.deiconify()

                    def Exit():
                        res=messagebox.askyesnocancel("Notification","Are you want to exit")
                        if res==True:
                            hroot.destroy()
                            root.destroy()

                    hroot = Toplevel()
                    hroot.grab_set()
                    hroot.geometry("1350x670+0+0")
                    hroot.title(" Hospital Management System")
                    label = Label(hroot, text="Hospital Management System | Developed by Pardeep ", bg="darkblue",
                       fg="white",font="arial 25 bold")
                    label.place(x=0, y=0, width=1340, height=45)
                    logout = Button(label, text="Logout", font="arial 20 bold", bg="orange", fg="white",command=Logout)
                    logout.place(x=1200, y=2, height=40)

                    btnframe = Frame(hroot, relief=GROOVE, borderwidth=6)
                    btnframe.place(x=0, y=45, width=150, height=610)

                    welcome = Label(btnframe, text="Menu", width="30", font="arial 25 bold", bd=5)
                    welcome.pack(side=TOP, expand=True)

                    homeimg = PhotoImage(file="Home.png")
                    homebatn = Button(btnframe, text="Home", font="arial 10 bold", image=homeimg, compound=TOP, height=100,
                      command=Home)
                    homebatn.pack(side=TOP, expand=True)

                    Docimg = PhotoImage(file="icon2.png")
                    Docbatn = Button(btnframe, text="Doctor", font="arial 10 bold", image=Docimg,
                     compound=TOP, height=100,command=Doctor)
                    Docbatn.pack(side=TOP, expand=True)

                    patientimg = PhotoImage(file="patient.png")
                    patientbatn = Button(btnframe, text="Patient", font="arial 10 bold", image=patientimg, compound=TOP,
                         height=100,command=Patient)
                    patientbatn.pack(side=TOP, expand=True)

                    appointmentimg = PhotoImage(file="appoinmet.png")
                    appointmentbatn = Button(btnframe, text="appointment", font="arial 10 bold", image=appointmentimg,
                             compound=TOP, height=100,command=appointment)
                    appointmentbatn.pack(side=TOP, expand=True)

                    Exitimg = PhotoImage(file="exit.png")
                    Exitbatn = Button(btnframe, text="Exit", font="arial 10 bold", image=Exitimg, compound=TOP, height=100,command=Exit)
                    Exitbatn.pack(side=TOP, expand=True)
                    Home()



                    hroot.mainloop()

                else:
                    messagebox.showerror("Error","username and password not match")
        except:
            messagebox.showerror("Notification","not match")





root=Tk()
root.geometry("1400x670+0+0")
root.title("Login Admin Hospital Management System")
root.config(bg="cyan")

global con ,mycursor

con = pymysql.connect(host="localhost", user="root", password="root",database="hospitalmanagement")
mycursor = con.cursor()
usernameentry=StringVar()
passwordentry=StringVar()


frame2=Frame(root,bg="white")
frame2.place(x=250,y=150,width=300,height=350)
load=Image.open("icon2.png")
render=ImageTk.PhotoImage(load)
img=Label(frame2,image=render,text="Create Admin" )
img.place(x=20,y=40,width=70,height=70 )
label=Label(frame2,text="Login Here",font="lucida 20 bold",bg="white")
label.place(x=100,y=60)
label=Label(frame2,text="Welcome to Hospital Management System \n Developed by Pardeep ",font="arial 10 bold",bg="white",fg="gray")
label.place(x=10,y=130)
username=Label(frame2,text="Username",font="italic 14 bold",fg="black",bg="white")
username.place(x=40,y=180)
usernameval=Entry(frame2,textvariable=usernameentry,bg="darkgray",width=25)
usernameval.place(x=40,y=210)

password=Label(frame2,text="Password",font="italic 14 bold",fg="black",bg="white")
password.place(x=40,y=240)

passeval=Entry(frame2,textvariable=passwordentry,bg="darkgray",width=25)
passeval.place(x=40,y=270)

loginbutn=Button(frame2,text="Login",font="lucida 10 bold",bg="blue",fg='white',width=12,command=creat)
loginbutn.place(x=60,y=300)


frame1=Frame(root,bg="white")
frame1.place(x=550,y=150,width=500,height=350)
load1=Image.open("maindoc.png")
render1=ImageTk.PhotoImage(load1)
img1=Label(frame1,image=render1)
img1.pack()

root.mainloop()