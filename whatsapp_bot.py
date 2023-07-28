from tkinter import *
from tkinter import ttk
ttk.Label
root = Tk()
root.geometry('400x500')
root.title('Whatsapp Bot')
import pywhatkit

e1=Entry(root)
e2=Entry(root)
e1.insert(0, "+91")
e3=Entry(root)
e4=Entry(root)


l1=Label(root,text='Enter phone Number')
l2=Label(root,text='Enter your message')
l3=Label(root,text='Enter hour in which message has to be sent (24 hour)')
l4=Label(root,text='Enter minute in which message has to be sent')


l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()

def prgrm():
    pywhatkit.sendwhatmsg(e1.get(),e2.get(),int(e3.get()),int(e4.get()))


Button(root,text='Submit',command=prgrm).pack()


root.mainloop()
