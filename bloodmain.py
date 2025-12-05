import mysql.connector as MySQLdb
from tkinter import *
import tkinter.messagebox
from PIL import Image
from tkinter import ttk

db=MySQLdb.connect(host="localhost",user="root",password="chinnu@123",database="db")
cursor=db.cursor()
root = Tk()
panel=Label(root,bg="black").place(x=0,y=0,relwidth=1,relheight=1)
root.title("BLOOD DONATION MANAGEMENT SYSTEM")
root.geometry("1920x1080")
root.configure(background='white')
l3=Label(root,text="BLOOD BANK SYSTEM",bg='white',font = "Helvetica 15 bold").place(x=450,y=40,w=300,h=40)
#l1=Label(root,text="Click to enter the details of the donor",bg='white',font="Helvetica 12").place(x=80,y=100,w=300,h=40)
b1=Button(root,text="Add Donor",command=lambda : donordetails()).place(x=80,y=150)
b4=Button(root,text="Donor Details",command=lambda : donorprofileupdate()).place(x=80,y=250)
#l2=Label(root,text="Click to enter the details of the blood",bg='white',font="Helvetica 12").place(x=80,y=200,w=300,h=40)
b2=Button(root,text="Blood Details",command=lambda : blooddetails()).place(x=80,y=350)	
#l3=Label(root,text="Click to make a request for blood",bg='white',font="Helvetica 12").place(x=80,y=300,w=300,h=40)
b3=Button(root,text="Request Blood",command=lambda : requestblood()).place(x=80,y=450)
b2=Button(root,text="Exit",command=lambda : stop(root)).place(x=80,y=550)	
v = IntVar()


def insertDonor(donorID,name,gender,age,bloodgroup,address,contact):
    '''
    print ("connection successful")
    print(donorID)
    print(type(donorID))
    print(name)
    print(type(name))
    print(gender)
    print(type(gender))
    print(address)
    print(type(address))
    print(age)
    print(type(age))
    print(contactno)
    print(type(contactno))
    #age=int(age)
    #contactno=int(contactno)
    '''
    if age<18:
        tkinter.messagebox.showinfo("Message","Age should be above 18 to donate blood")
        #print("Age should be above 18 to donate blood")
    else:
        insert = "INSERT INTO donors(donorID,name,gender,age,bloodgroup,address,contact) VALUES('{}','{}','{}',{},'{}','{}',{})".format(donorID,name,gender,age,bloodgroup,address,contact)
        cursor.execute(insert)
        db.commit()
        tkinter.messagebox.showinfo("Message","Record Saved")
    
#	    db.rollback()

'''
def UpdateDonor():
    insert = "INSERT INTO donors(donorID,name,gender,age,address,contactno) VALUES('{}','{}','{}',{},'{}',{})".format(donorID,name,gender,age,address,contactno)
    cursor.execute(insert)
    db.commit()
    tkinter.messagebox.showinfo("Message","Record Updated")
    

'''
def donorprofiledisplay(dID):
    select="select * from donors where donorID={}".format(dID)
    cursor.execute(select)
    rows=cursor.fetchone()
    #print(rows)
    treev=ttk.Treeview(root,selectmode="browse")
    treev.pack(side="right")
    treev["columns"]=("1","2","3","4","5","6","7")
    treev['show']='headings'
    treev.heading("1",text="DonorID")
    treev.heading("2",text="Name")
    treev.heading("3",text="Gender")
    treev.heading("4",text="Age")
    treev.heading("5",text="Blood Group")
    treev.heading("6",text="Address")
    treev.heading("7",text="Contact")
    treev.insert("",'end',text="1,2,3,4,5,6,7,",values=(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5],row[6]))
    


    root.mainloop()
    
def insertBloodinfo():
    insert = "INSERT INTO details(donorID,bloodgroup,unit) VALUES('{}','{}',{})".format(donorID,bloodgroup,unit)
    cursor.execute(insert)
    db.commit()
    tkinter.messagebox.showinfo("Message","Record Saved")
    

    
def insertBlood(bloodID):
	insert= "INSERT INTO blood(bloodID) VALUES('{}')".format(bloodID)
		
	try:
		cursor.execute(insert)
		db.commit()
	except:
		db.rollback()
		
def retrieve(bg):
	request="select * from donors inner join blood using(id) where bloodgroup='"+bg+"'"
	
	try:
		cursor.execute(request)		
		rows=cursor.fetchall()		
		db.commit()
		print(len(rows))
		return rows
	except:
		db.rollback() 

def sel():
   selection = "You selected the option " + v.get()
   #print(selection)
  

def donordetails():
	global v
	root=Toplevel()
	root.title("BLOOD BANK")
	root.geometry("1024x768")
	root.configure(background ='#FF8F8F')
	l=Label(root,text="DonorID:",bg='white',font="Helvetica 12").place(x=40,y=40)
	l1=Label(root,text="Name:",bg='white',font="Helvetica 12").place(x=40,y=80)
	l2=Label(root,text="Gender:",bg='white',font="Helvetica 12").place(x=40,y=120)
	l3=Label(root,text="Age:",bg='white',font="Helvetica 12").place(x=40,y=160)
	l6=Label(root,text="Blood Group:",bg='white',font="Helvetica 12").place(x=40,y=200)
	l4=Label(root,text="Address:",bg='white',font="Helvetica 12").place(x=40,y=240)
	l5=Label(root,text="Contact:",bg='white',font="Helvetica 12").place(x=40,y=280)
	f= StringVar(root)
	f.set("Select Gender")
	g= OptionMenu(root,f,"Male","Female","Other").place(x=120,y=120)
	menu= StringVar(root)
	menu.set("Select Blood Group")
	drop= OptionMenu(root,menu,"A+", "A-","B+","B-","AB+","AB-","O+","O-").place(x=160,y=200)
	e=Entry(root)
	e.place(x=120,y=40)
	e1=Entry(root)
	e1.place(x=120,y=80)
	#e2=Entry(root)
	#e2.place(x=120,y=120)
	'''
	v= IntVar(root)
	r1=Radiobutton(root,text="Male",variable=v,value=1,command=sel).place(x=120,y=120)
	r2=Radiobutton(root,text="Female",variable=v,value=2,command=sel).place(x=200,y=120)
	r3=Radiobutton(root,text="Other",variable=v,value=3,command=sel).place(x=280,y=120)
	'''
	e3=Entry(root)
	e3.place(x=100,y=160)
	#e6=Entry(root)
	#e6.place(x=160,y=200)
	e4=Entry(root)
	e4.place(x=120,y=240)
	e5=Entry(root)
	e5.place(x=120,y=280)
	
	'''
	r1.pack(anchor=v)
	r2.pack(anchor=v)
	r3.pack(anchor=v)
	'''
	b2=Button(root,text="Back",command=lambda : stop(root)).place(x=120,y=340)
	print(e.get())
	
	b1=Button(root,text="Submit",command=lambda : insertDonor(e.get(),e1.get(),menu.get(),int(e3.get()),f.get(),e4.get(),int(e5.get()))).place(x=40,y=340)

	root.mainloop()

def donorprofileupdate():
    root=Toplevel()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background ='#FF8F8F')
    l=Label(root,text="DonorID:",bg='white',font="Helvetica 12").place(x=40,y=40)
    e=Entry(root)
    e.place(x=120,y=40)

    '''
    l1=Label(root,text="Name:",bg='white',font="Helvetica 12").place(x=40,y=150)
    l2=Label(root,text="Gender:",bg='white',font="Helvetica 12").place(x=40,y=200)
    l3=Label(root,text="Age:",bg='white',font="Helvetica 12").place(x=40,y=250)
    l4=Label(root,text="Address:",bg='white',font="Helvetica 12").place(x=40,y=300)
    l5=Label(root,text="Contact:",bg='white',font="Helvetica 12").place(x=40,y=350)
    e=Entry(root)
    e.place(x=120,y=40)
    e1=Entry(root)
    e1.place(x=120,y=150)
    e2=Entry(root)
    e2.place(x=120,y=200)
    e3=Entry(root)
    e3.place(x=120,y=250)
    e4=Entry(root)
    e4.place(x=120,y=300)
    e5=Entry(root)
    e5.place(x=120,y=350)
    '''
    b1=Button(root,text="Submit",command=lambda : donorprofiledisplay(e.get())).place(x=100,y=90)
    '''
    b2=Button(root,text="Submit",command=lambda : donorprofileupdate(e.get(),e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),e7.get(),e8.get())).place(x=80,y=400)
    '''
    root.mainloop()
def bloodcollection():
    root=Tk()
    root.title("BLOOD BANK")
    root.geometry("1024x768")
    root.configure(background ='#FF8F8F')
    l=Label(root,text="DonorID:",bg='white',font="Helvetica 12").place(x=40,y=40)
    menu= StringVar(root)
    menu.set("Select Blood Group")
    drop= OptionMenu(root,menu,"A+", "A-","B+","B-","AB+","AB-","O+","O-").place(x=160,y=200)
    b1=Button(root,text="Submit",command=lambda : bloodcollection).place(x=100,y=90)

    
def blooddetails():
	root=Tk()
	root.title("BLOOD BANK")
	root.geometry("1024x768")
	root.configure(background ='#FF8F8F')
	#l=Label(root,,text="Blood Group:",font="Helvetica 12").place(x=40,y=40,w=250,h=20)
	l1=Label(root,text="Blood Group:",font="Helvetica 12").place(x=40,y=80,w=250,h=20)
	#l2=Label(root,text="PLatetelet count (in 100 thousands):",font="Helvetica 12").place(x=40,y=80,w=250,h=20)
	#l3=Label(root,text="RBC count (in millions):",font="Helvetica 12").place(x=40,y=120,w=250,h=20)
	#l4=Label(root,text="Date Of Entry count:").place(x=40,y=160,w=250,h=20)
	menu= StringVar(root)
	menu.set("Select Blood Group")
	drop= OptionMenu(root,menu,"A+", "A-","B+","B-","AB+","AB-","O+","O-").place(x=300,y=80)
	#drop.pack()
	#e=Entry(root)
	#e.place(x=40,y=120)
	'''
	e1=Entry(root)
	e1.place(x=350,y=40)
	e2=Entry(root)
	e2.place(x=350,y=80)
	e3=Entry(root)
	e3.place(x=350,y=120)
	e4=Entry(root)
	e4.place(x=350,y=160)
	#b2=Button(root,text="Back",command=lambda : stop(root)).place(x=200,y=200)
	#b1=Button(root,text="Submit",command=lambda : insertBlood(e1.get(),e2.get(),e3.get(),e4.get())).place(x=40,y=200)
	
	#panel = Label(root, image = img,bg="#F6B88D").place(x=200,y=200,w=400,h=400)
	'''
	b1=Button(root,text="Submit",command=lambda : insertBlood()).place(x=40,y=120)
	root.mainloop()	
	
	
def grid1(bg):
    #global bg
    root=Tk()
    root.title("LIST OF MATCHING DONORS")
    root.geometry("750x500")
    root.configure(background='#0C43F0')
    rows=retrieve(bg)
    x=0
    for row in rows:
	    l1=Label(root,text=row[0],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=0,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l2=Label(root,text=row[1],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=1,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l3=Label(root,text=row[2],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=2,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l4=Label(root,text=row[3],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=3,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l5=Label(root,text=row[4],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=4,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l6=Label(root,text=row[5],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=5,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l7=Label(root,text=row[6],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=6,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l8=Label(root,text=row[7],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=7,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l9=Label(root,text=row[8],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=8,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    l10=Label(root,text=row[9],bg="#1EDEF2",font = "Verdana 15 bold").grid(row=x,column=9,sticky='E',padx=5,pady=5,ipadx=5,ipady=5)
	    x=x+1
    root.mainloop()
    tkinter.messagebox.showinfo("Message","Record Saved")

def requestblood():
	root=Tk()
	root.title("BLOOD BANK")
	root.geometry("1024x720")
	root.configure(background='#FF8F8F')
	l=Label(root,text="Hospital Name:").place(x=50,y=50)
	l1=Label(root,text="Blood Group:").place(x=50,y=100)
	l2=Label(root,text="Units(in litres):").place(x=50,y=160)
	menu= StringVar(root)
	menu.set("Select Blood Group")
	drop= OptionMenu(root,menu,"A+", "A-","B+","B-","AB+","AB-","O+","O-").place(x=140,y=100)
	e=Entry(root)
	e.place(x=150,y=50)
	e2=Entry(root)
	e2.place(x=150,y=160)
	b2=Button(root,text="Back",command=lambda : stop(root)).place(x=150,y=200)
	b=Button(root,text="Submit",command=lambda : grid1(e.get(),e2.get())).place(x=50,y=200)
	root.mainloop()

def stop(root):
	root.destroy()


root.mainloop()
db.commit()
