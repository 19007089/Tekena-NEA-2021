from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registraion Form")
label_0 = Label(root, text = "Registration form",width = 20,font =("bold", 20))
label_0.place(x=90,y=53)

MY_ADDRESS = 'my_address@example.comm'
PASSWORD = 'mypassword'
msg = EmailMessage()
msg.set_content('testing python automated email program')
#subject = 'Type_in_your_subject_here'
subject = 'Testing python automated email'
msg['Subject'] = subject
msg['From'] = MY_ADDRESS
msg['To'] = 'recipient_address_here'
s.send_message(msg)
s.quit()

#s = smtplib.SMTP(host='your_host_address_here', port=your_port_here)
s = smtplib.SMTP(host=' smtp.gmail.com', port=587)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)


label_1 = Label(root, text = "UserName", width=20,font=("bold",10))
label_1.place(x=80,y=130)
name = Entry(root)
name.get()  
name.place(x=240,y=130)

label_2 = Label(root, text = "Email", width = 20, font=("bold", 10))
label_2.place(x=80,y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y = 180)

label_3 = Label(root, text= "Gender", width = 20, font=("bold", 10))
label_3.place(x=80, y=230)
var = IntVar()
Radiobutton(root, text = "Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root,text = "Female",padx = 20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text ="country", width = 20, font = ("bold", 10))
list1 = ['Canada', 'India', 'UK', 'USA', 'Iceland', 'south Africa'] ;
c = StringVar()
droplist = OptionMenu(root, c, *list1)
droplist.config(width=15)
c.set('select your country')
droplist.place(x=240,y =280)
Button(root,text = "Submit",width = 20).place(x=180,y=380)    

spots =[]
mast = Tk()
mast.geometry("500x500")
mast.title("Shotdoctor")
label_5 = Label(mast, text=("Hello", name.get(),'\n spot1: '), width = 20, font = ("bold",10))

label_0 = Label(mast, text = "Recording",width = 20,font =("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(mast, text = "spot1", width=20,font=("bold",10))
label_1.place(x=80,y=150)
spot1 = Entry(mast) 
spot1.pack()
spots.append(spot1.get()) 
spot1.place(x=240,y=150)

label_2 = Label(mast, text = "spot2", width = 20, font=("bold", 10))
label_2.place(x=80,y=180)
spot2 = Entry(mast) 
spot2.pack()
spots.append(spot2.get()) 
spot2.place(x=240, y = 180)

label_3 = Label(mast, text= "spot3", width = 20, font=("bold", 10))
label_3.place(x=80, y=210)
spot3 = Entry(mast) 
spot3.pack()
spots.append(spot3.get())
spot3.place(x=240,y=210)

label_4 = Label(mast, text= "spot4", width = 20, font=("bold", 10))
label_4.place(x=80, y=240)
spot4 = Entry(mast) 
spot4.pack()
spots.append(spot4.get())
spot4.place(x=240,y=240)

label_5 = Label(mast, text= "spot5", width = 20, font=("bold", 10))
label_5.place(x=80, y=270)
spot5 = Entry(mast) 
spot5.pack()
spots.append(spot3.get())
spot5.place(x=240,y=270)

for i in range(0,5):
    total = 0
    for i in range(0,4):
        total += int(spots[i])
    avg = total / 5
    percentage = avg * 100

    spot_percentage = []
    for i in range(0,4):
          spot_percentage.append(int(spot[i]) * 20)

team = []
 
Button(mast,text = "Submit",width = 20).place(x=180,y=340)

#from tkinter import *
#from PIL import ImageTk, Image    
#def form(name):
    #root = Tk()
    #root.geometry('600x500')
    #root.title("Form")    
    #photo = PhotoImage('C:/Users/44753/Downloads/kobe.png')
    #l = Label(image = photo)
    #l.pack()
#form()
