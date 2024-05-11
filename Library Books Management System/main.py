#Tkinter MODULES
from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from tkinter import ttk

#SQL CONNECTION
import mysql.connector as con
import datetime
connector = con.connect(host="localhost",user="root",password="*******",database="library_books_management")


#=============================Add Book=================================
def add_book():
    root_add = Tk()
    root_add.title("Add Book")

    def delete(g,h,i,j,k,l):
        bidEntry.delete(0,g)
        bnameEntry.delete(0,h)
        bauthorEntry.delete(0,i)
        bpriceEntry.delete(0,j)
        bdomainEntry.delete(0,k)
        bdescriptionEntry.delete(0,l)
        

    def enter_book_info():
        bid=bidEntry.get()
        bname=bnameEntry.get()
        bauthor=bauthorEntry.get()
        bprice=bpriceEntry.get()
        bdomain=bdomainEntry.get()
        bdescription=bdescriptionEntry.get()
        date = datetime.date.today()
        
        query = "insert into books values(%s,%s,%s,%s,%s,%s,%s,%s);"

        
            
        if(bid!='' and bname!='' and bauthor!='' and bprice!='' and bdomain!='' and bdescription!=''):
            try:
                if(type(int(bprice))==int):
                    cursor = connector.cursor()
                    cursor.execute(query,(bid,bname,bauthor,bprice,bdomain,bdescription,'available',date))
                    rows_affected=cursor.rowcount
                    connector.commit()
                    if(rows_affected==1):
                        delete(len(bid),len(bname),len(bauthor),len(bprice),len(bdomain),len(bdescription))
                        root_add.destroy()
                        messagebox.showinfo('','Book added successfully!')
                    
                    
            except ValueError:
                root_add.destroy()
                messagebox.showerror('','Price should be a number')
            except:
                root_add.destroy()
                messagebox.showerror('','Book with Id '+bid+' is already present')
                
                    
        else:
            root_add.destroy()
            messagebox.showerror("Addition Failed!","Incomplete details\nTRY AGAIN!")
        
        
    #icon
    root_add.iconbitmap("logo.ico")
    root_add.minsize(1000,600)
    root_add.configure(bg='#ffb3ff')


    frame = Frame(root_add)
    frame.pack(pady=50)
    frame.configure(padx=10,pady=10)

    book_info_frame = LabelFrame(frame,text = "Book Information")
    book_info_frame.grid(row=0,column=0)
    book_info_frame.configure(font=("Verdana",15),fg="#003399",padx=20,pady=20)


    #book id
    bnameId = Label(book_info_frame,text = "Book Id")
    bnameId.grid(row=0,column=0)

    bidEntry = Entry(book_info_frame)
    bidEntry.grid(row=1,column=0)

    #book name
    bnameLabel = Label(book_info_frame,text = "Book Name")
    bnameLabel.grid(row=0,column=1)

    bnameEntry = Entry(book_info_frame)
    bnameEntry.grid(row=1,column=1)

    #book author
    bauthorLabel = Label(book_info_frame,text = "Book Author")
    bauthorLabel.grid(row=0,column=2)

    bauthorEntry = Entry(book_info_frame)
    bauthorEntry.grid(row=1,column=2)


    #book price
    bpriceLabel = Label(book_info_frame,text = "Book Price")
    bpriceLabel.grid(row=3,column=0)

    bpriceEntry = Entry(book_info_frame)
    bpriceEntry.grid(row=4,column=0)

    #book domain
    bdomainLabel = Label(book_info_frame,text = "Book Domain")
    bdomainLabel.grid(row=3,column=1)

    bdomainEntry = Entry(book_info_frame)
    bdomainEntry.grid(row=4,column=1)

    #book description
    bdescriptionLabel = Label(book_info_frame,text = "Book Description")
    bdescriptionLabel.grid(row=3,column=2)

    bdescriptionEntry = Entry(book_info_frame)
    bdescriptionEntry.grid(row=4,column=2)


    for widget in book_info_frame.winfo_children():
        widget.configure(font=('Verdana',15),fg="#003399")
        widget.grid_configure(padx=20,pady=15)

    submitBtn = Button(root_add,text="Submit",command=enter_book_info)
    submitBtn.pack(pady=30)
    submitBtn.configure(font=("Verdana",15),fg="#003399",padx=50)

    def exit_add_book():
        root_add.destroy()

    ExitBtn = Button(root_add,text="Exit",command=exit_add_book)
    ExitBtn.pack(pady=30,padx=50)
    ExitBtn.configure(font=("Verdana",15),fg="#003399",padx=10)


    root_add.mainloop()

#=============================Issue Book=================================

def issue_book():

    root_issue = Tk()
    root_issue.title("Issue Book")

    def delete(g,h,i,j,k,l,m):
        snameEntry.delete(0,g)
        sregNoEntry.delete(0,h)
        bidEntry.delete(0,i)
        syearEntry.delete(0,j)
        ssectionEntry.delete(0,k)
        sbranchEntry.delete(0,l)
        sgmailEntry.delete(0,m)
        

    def issue_book_info():
        sname=snameEntry.get()
        sregNo=sregNoEntry.get()
        bid=bidEntry.get()
        syear=syearEntry.get()
        ssection=ssectionEntry.get()
        sbranch=sbranchEntry.get()
        sgmail=sgmailEntry.get()
        date = datetime.date.today()
        
        query1 = "insert into issued_books values(%s,%s,%s,%s,%s,%s,%s,%s);"
        query2 = "update books set issued=%s where bid=%s"



        cursor = connector.cursor()
        cursor.execute("select issued from books where bid=%s",(bid,))
        status=''
        for i in cursor:
            status = i[0]
        connector.commit()
            
        
        if(sname!='' and sregNo!='' and bid!='' and syear!='' and ssection!='' and sbranch!='' and sgmail!=''):
            if(syear in ['I','II','III','1V']):
                if(status=='available'):
                    cursor = connector.cursor()
                    cursor.execute(query1,(sname,sregNo,bid,syear,ssection,sbranch,sgmail,date))
                    rows_affected=cursor.rowcount
                    connector.commit()
                    if(rows_affected==1):
                        delete(len(sname),len(sregNo),len(bid),len(syear),len(ssection),len(sbranch),len(sgmail))
                        root_issue.destroy()
                        messagebox.showinfo('','Book issued successfully!')

                    cursor = connector.cursor()
                    cursor.execute(query2,('issued',bid))
                    connector.commit()
                        
                    
                else:
                    root_issue.destroy()
                    messagebox.showwarning("Can't Issue","Book with ID "+bid+" is unavailable!")
            else:
                root_issue.destroy()
                messagebox.showwarning("Can't Issue","Enter Valid Year")
                
                
        else:
            root_issue.destroy()
            messagebox.showerror("Can't Issue","Enter all details\nTRY AGAIN!")


        
        
        
    #icon
    root_issue.iconbitmap("logo.ico")
    root_issue.minsize(1000,600)
    root_issue.configure(bg='#ffb3ff')


    frame = Frame(root_issue)
    frame.pack(pady=50)
    frame.configure(padx=10,pady=10)

    book_info_frame = LabelFrame(frame,text = "Issue Book")
    book_info_frame.grid(row=0,column=0)
    book_info_frame.configure(font=("Verdana",15),fg="#003399",padx=20,pady=20)


    #student name
    snameId = Label(book_info_frame,text = "Student Name")
    snameId.grid(row=0,column=0)
    snameId.configure(font=("Verdana",15),fg="#003399")

    snameEntry = Entry(book_info_frame)
    snameEntry.grid(row=1,column=0)

    #reg no
    sregNoLabel = Label(book_info_frame,text = "Reg No")
    sregNoLabel.grid(row=0,column=1)
    sregNoLabel.configure(font=("Verdana",15),fg="#003399")

    sregNoEntry = Entry(book_info_frame)
    sregNoEntry.grid(row=1,column=1)

    #book id
    bidLabel = Label(book_info_frame,text = "Book Id")
    bidLabel.grid(row=0,column=2)
    bidLabel.configure(font=("Verdana",15),fg="#003399")

    bidEntry = Entry(book_info_frame)
    bidEntry.grid(row=1,column=2)


    #year
    syearLabel = Label(book_info_frame,text = "Year")
    syearLabel.grid(row=3,column=0)
    syearLabel.configure(font=("Verdana",15),fg="#003399")

    syearEntry = ttk.Combobox(book_info_frame,values=['I','II','III','IV'])
    syearEntry.grid(row=4,column=0)

    #section
    ssectionLabel = Label(book_info_frame,text = "Section")
    ssectionLabel.grid(row=3,column=1)
    ssectionLabel.configure(font=("Verdana",15),fg="#003399")

    ssectionEntry = ttk.Combobox(book_info_frame,values=['A','B','C','D'])
    ssectionEntry.grid(row=4,column=1)

    #branch
    sbranchLabel = Label(book_info_frame,text = "Branch")
    sbranchLabel.grid(row=3,column=2)
    sbranchLabel.configure(font=("Verdana",15),fg="#003399")


    sbranchEntry = ttk.Combobox(book_info_frame,values=['EEE','ECE','ECM','ME','CE','CSE','AIDS','IT'])
    sbranchEntry.grid(row=4,column=2)


    #gmail
    sgmailId = Label(book_info_frame,text = "Student Gmail")
    sgmailId.grid(row=5,column=1)
    sgmailId.configure(font=("Verdana",15),fg="#003399")

    sgmailEntry = Entry(book_info_frame)
    sgmailEntry.grid(row=6,column=1)
    

    for widget in book_info_frame.winfo_children():
        widget.configure(font=('Verdana',15))
        widget.grid_configure(padx=20,pady=15)

    submitBtn = Button(root_issue,text="Submit",command=issue_book_info)
    submitBtn.pack(pady=30)
    submitBtn.configure(font=("Verdana",15),fg="#003399",padx=50)

    def exit_issue_book():
        root_issue.destroy()

    ExitBtn = Button(root_issue,text="Exit",command=exit_issue_book)
    ExitBtn.pack(pady=30,padx=50)
    ExitBtn.configure(font=("Verdana",15),fg="#003399",padx=10)

    root_issue.mainloop()

    
#=============================Return Book================================

def return_book():

    root_delete = Tk()
    root_delete.title("Return Book")

    def delete(g,h):
        sregNoEntry.delete(0,g)
        bidEntry.delete(0,h)
        

    def return_book_info():
        sregNo=sregNoEntry.get()
        bid=bidEntry.get()
        
        delete(len(sregNo),len(bid))

        if(sregNo!='' and bid!=''):
            #query1 = "delete from issued_books where bid=%s and regno=%s"
            query1 = "select * from issued_books where bid=%s and regno=%s"
            cursor = connector.cursor()
            cursor.execute(query1,(bid,sregNo))
            #rows_affected=cursor.rowcount
            rows_affected=len(cursor.fetchall())
            connector.commit()
            if(rows_affected==1):
                root_delete.destroy()
                messagebox.showinfo('','Book returned successfully!')
            else:
                root_delete.destroy()
                messagebox.showerror('','Book not issued with that details.')

            query2 = "update books set issued=%s where bid=%s"
            cursor = connector.cursor()
            cursor.execute(query2,('available',bid))
            connector.commit()
            
        else:
            root_delete.destroy()
            messagebox.showerror('','Enter all details')
    
        
    #icon
    root_delete.iconbitmap("logo.ico")
    root_delete.minsize(1000,600)
    root_delete.configure(bg='#ffb3ff')


    frame = Frame(root_delete)
    frame.pack(pady=50)
    frame.configure(padx=10,pady=10)

    book_info_frame = LabelFrame(frame,text = "Return Book")
    book_info_frame.grid(row=0,column=0)
    book_info_frame.configure(font=("Verdana",15),fg="#003399",padx=20,pady=20)


    #reg no
    sregNoLabel = Label(book_info_frame,text = "Reg No")
    sregNoLabel.grid(row=0,column=0)

    sregNoEntry = Entry(book_info_frame)
    sregNoEntry.grid(row=1,column=0)

    #book code
    bidLabel = Label(book_info_frame,text = "Book Id")
    bidLabel.grid(row=0,column=1)

    bidEntry = Entry(book_info_frame)
    bidEntry.grid(row=1,column=1)



    for widget in book_info_frame.winfo_children():
        widget.configure(font=('Verdana',15),fg="#003399")
        widget.grid_configure(padx=20,pady=15)

    submitBtn = Button(root_delete,text="Submit",command=return_book_info)
    submitBtn.pack(pady=30)
    submitBtn.configure(font=("Verdana",15),fg="#003399",padx=50)
    

    def exit_add_book():
        root_delete.destroy()

    ExitBtn = Button(root_delete,text="Exit",command=exit_add_book)
    ExitBtn.pack(pady=30,padx=50)
    ExitBtn.configure(font=("Verdana",15),fg="#003399",padx=10)

    root_delete.mainloop()


#=============================Display Books=================================
def display_books():

    root_display = Tk()
    root_display.title("Library Books")
        
    #icon
    root_display.iconbitmap("logo.ico")
    root_display.minsize(1000,600)
    root_display.configure(bg='#ffb3ff')


    frame = Frame(root_display)
    frame.pack(pady=50)
    frame.configure(padx=10,pady=10)

    book_info_frame = LabelFrame(frame,text = "Books")
    book_info_frame.grid(row=0,column=0)
    book_info_frame.configure(font=("Verdana",15),fg="#003399",padx=20,pady=20)



    #Display Library Books Function
    def display_library_books():
        


        root_show = Tk()
        root_show.title("Library Books")
        root_show.geometry("1200x600")


        #icon
        root_show.iconbitmap("logo.ico")
        root_show.minsize(1000,600)
        root_show.configure(bg='#ffb3ff')


        cursor = connector.cursor()
        cursor.execute("select * from books")

        tree=ttk.Treeview(root_show)
        tree['show']='headings'

        #Theme
        theme=ttk.Style(root_show)
        theme.theme_use("default")



        tree["columns"]=('bid','bname','bauthor','bprice','bdomain','bdesc','issued','badded_date')


        #Assinging widths
        tree.column('bid',width=60,minwidth=60,anchor=CENTER)
        tree.column('bname',width=250,minwidth=250,anchor=CENTER)
        tree.column('bauthor',width=120,minwidth=120,anchor=CENTER)
        tree.column('bprice',width=60,minwidth=60,anchor=CENTER)
        tree.column('bdomain',width=100,minwidth=100,anchor=CENTER)
        tree.column('bdesc',width=200,minwidth=200,anchor=CENTER)
        tree.column('issued',width=80,minwidth=80,anchor=CENTER)
        tree.column('badded_date',width=100,minwidth=100,anchor=CENTER)

        #Asssigning heading names
        tree.heading('bid',text="Book ID",anchor=CENTER)
        tree.heading('bname',text="Book Name",anchor=CENTER)
        tree.heading('bauthor',text="Author",anchor=CENTER)
        tree.heading('bprice',text="Price",anchor=CENTER)
        tree.heading('bdomain',text="Domain",anchor=CENTER)
        tree.heading('bdesc',text="Description",anchor=CENTER)
        tree.heading('issued',text="Book Status",anchor=CENTER)
        tree.heading('badded_date',text="Date",anchor=CENTER)


        i=0
        for row in cursor:
            tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            i+=1
        tree.pack()

        #BOOKS COUNT
        cursor = connector.cursor()
        cursor.execute("select * from books")
        books_count=len(cursor.fetchall())



        count=Label(root_show,text="No of Books="+str(books_count))
        count.pack()
        root_show.mainloop()

    
    #Display Issued Books Function
    def display_issued_books():
        


        root_show = Tk()
        root_show.title("Issued Books")
        root_show.geometry("1200x600")


        #icon
        root_show.iconbitmap("logo.ico")
        root_show.minsize(1000,600)
        root_show.configure(bg='#ffb3ff')


        cursor = connector.cursor()
        cursor.execute("select * from issued_books")

        tree=ttk.Treeview(root_show)
        tree['show']='headings'

        #Theme
        theme=ttk.Style(root_show)
        theme.theme_use("default")

        tree["columns"]=('sname','regno','bid','year','section','branch','gmail','date')


        #Assinging widths
        tree.column('sname',width=150,minwidth=150,anchor=CENTER)
        tree.column('regno',width=80,minwidth=80,anchor=CENTER)
        tree.column('bid',width=120,minwidth=120,anchor=CENTER)
        tree.column('year',width=60,minwidth=60,anchor=CENTER)
        tree.column('section',width=100,minwidth=100,anchor=CENTER)
        tree.column('branch',width=80,minwidth=80,anchor=CENTER)
        tree.column('gmail',width=200,minwidth=200,anchor=CENTER)
        tree.column('date',width=100,minwidth=100,anchor=CENTER)

        #Asssigning heading names
        tree.heading('sname',text="Student Name",anchor=CENTER)
        tree.heading('regno',text="Reg No",anchor=CENTER)
        tree.heading('bid',text="Book ID",anchor=CENTER)
        tree.heading('year',text="Year",anchor=CENTER)
        tree.heading('section',text="Section",anchor=CENTER)
        tree.heading('branch',text="Branch",anchor=CENTER)
        tree.heading('gmail',text="Gmail",anchor=CENTER)
        tree.heading('date',text="Date",anchor=CENTER)


        i=0
        for row in cursor:
            tree.insert('',i,text="",values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
            i+=1
        tree.pack()

        #RECORDS COUNT
        cursor = connector.cursor()
        cursor.execute("select * from issued_books")
        records_count=len(cursor.fetchall())

        count=Label(root_show,text="No ofRecords="+str(records_count))
        count.pack()
        root_show.mainloop()






    #Books Available
    avBtn = Button(book_info_frame,text="Library Books",command=display_library_books)
    avBtn.grid(row=0,column=0)
    avBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)

    #issue
    issueBtn = Button(book_info_frame,text="Issued Books",command=display_issued_books)
    issueBtn.grid(row=0,column=1)
    issueBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)

    




    for widget in book_info_frame.winfo_children():
        widget.configure(font=('Verdana',15),fg="#003399")
        widget.grid_configure(padx=30,pady=15)

    def exit_display_books():
        root_display.destroy()
    submitBtn = Button(root_display,text="Exit",command=exit_display_books)
    submitBtn.pack(pady=30)
    submitBtn.configure(font=("Verdana",15),fg="#003399",padx=50)

    root_display.mainloop()
    
#=============================Show Tasks=================================


def show_tasks():

    root_show_tasks = Tk()
    root_show_tasks.title("Tasks")
        
    #icon
    root_show_tasks.iconbitmap("logo.ico")
    root_show_tasks.minsize(1000,600)
    root_show_tasks.configure(bg='#ffb3ff')


    frame = Frame(root_show_tasks)
    frame.pack(pady=50)
    frame.configure(padx=10,pady=10)

    book_info_frame = LabelFrame(frame,text = "Tasks")
    book_info_frame.grid(row=0,column=0)
    book_info_frame.configure(font=("Verdana",15),fg="#003399",padx=20,pady=20)

    #add
    addBtn = Button(book_info_frame,text="Add",command=add_book)
    addBtn.grid(row=0,column=0)
    addBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)


    #issue
    issueBtn = Button(book_info_frame,text="Issue",command=issue_book)
    issueBtn.grid(row=0,column=1)
    issueBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)

    #delete
    deleteBtn = Button(book_info_frame,text="Return",command=return_book)
    deleteBtn.grid(row=0,column=2)
    deleteBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)

    #Display
    showBtn = Button(book_info_frame,text="Display",command=display_books)
    showBtn.grid(row=0,column=3)
    showBtn.configure(font=("Verdana",15),fg="#003399",padx=30,pady=20)




    for widget in book_info_frame.winfo_children():
        widget.configure(font=('Verdana',15),fg="#003399")
        widget.grid_configure(padx=30,pady=15)

    def exit_show_tasks():
        root_show_tasks.destroy()
        
    submitBtn = Button(root_show_tasks,text="Exit",command=exit_show_tasks)
    submitBtn.pack(pady=30)
    submitBtn.configure(font=("Verdana",15),fg="#003399",padx=50)

    root_show_tasks.mainloop()
#================================Login Page=================================

root = Tk()
root.title("Login")

#icon
root.iconbitmap("logo.ico")
root.minsize(1000,600)
root.configure(bg='#ffb3ff')


#credentails verification
def check_credentials():
    userid = login_id.get()
    password = password_id.get()
    a = len(userid)
    b = len(password)
    if(userid=="Luser1" and password=="1234"):
        root.destroy()
        show_tasks()
    else:
        delete(a,b)
        messagebox.showerror("Login Status","Login Failed")

#delete Entries
def delete(m,n):
    login_id.delete(0,m)
    password_id.delete(0,n)
        
img = Image.open("logo.jpg")
resized_img = img.resize((60,60))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root,image=img)
img_label.pack(pady=(30,30))

clg_name = Label(text="Vignan's Institute of Information Technology(A)",fg="#003399",bg='#ffb3ff')
clg_name.configure(font=("Verdana",20))
clg_name.pack(pady=(10,40))

#login ID
login_label = Label(text="Enter Login Id",fg="#003399",bg='#ffb3ff')
login_label.configure(font=("Verdana",10))
login_label.pack(pady=(10,15))

login_id = Entry(width=20)
login_id.configure(font=("Verdana",10))
login_id.pack(ipady=3);

#password 
password_label = Label(text="Enter Password",fg="#003399",bg='#ffb3ff')
password_label.configure(font=("Verdana",10))
password_label.pack(pady=(10,15))

password_id = Entry(width=20)
password_id.configure(font=("Verdana",10))
password_id.pack(pady=(0,30),ipady=3);

#submit
submit_btn = Button(root,text="Submit",command=check_credentials)
submit_btn.pack(ipady=5,ipadx=5)
submit_btn.configure(font=("Verdana",10))


root.mainloop()




