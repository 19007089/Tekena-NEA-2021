from tkinter import*
root = Tk()
root.geometry('500x500')
root.title("Registraion Form")
label_0 = Label(root, text = "Registration form",width = 20,font =("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text = "UserName", width=20,font=("bold",10))
label_1.place(x=80,y=130)

name = Entry(root)
name.get()  
name.place(x=240,y=130)

label_2 = Label(root, text = "Email", width = 20, font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240, y = 180)

label_3 = Label(root, text= "Gender", width = 20, font=("bold", 10))
label_3.place(x=70, y=230)
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
spots.append((spot1.get()))


label_1 = Label(root, text = "spot2", width=20,font=("bold",10))
label_1.place(x=80,y=130)
spot2 = Entry(root)
spots.append(spot2.get()) 
spots.place(x=240,y=130)

label_2 = Label(root, text = "spots3", width = 20, font=("bold", 10))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.place(x=240, y = 180)

label_3 = Label(root, text= "Gender", width = 20, font=("bold", 10))
label_3.place(x=70, y=230)
var = IntVar()
Radiobutton(root, text = "Male",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root,text = "Female",padx = 20, variable=var, value=2).place(x=290, y=230)

label_4 = Label(root, text ="country", width = 20, font = ("bold", 10))
list1 = ['Canada', 'India', 'UK', 'USA', 'Iceland', 'south Africa'] ;
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
