from tkinter import*
import tkinter.messagebox as Msg
def B2K():

    chBath=Bath.get()
    if Bath.get()=='':
        Msg.showinfo("info","Enter bath please!!!!!",icon='warning')
        txt1.focus_set()
    elif Rate.get():
        Msg.showinfo("info", "Enter bath please!!!!!", icon='warning')
        txt2.focus_set()

    elif chBath.isalpha():
        Msg.showinfo("info", "Enter bath is number only!!!!", icon='warning')
        txt1.focus_set()

    else:
        b=int(Bath.get())
        r=int(Rate.get())
        k=b*r
        Kip.set(f'{k:,}Kip')


def AllClear():
    Bath.set('')
    Rate.set('')
    Kip.set('')
    txt1.focus()



root = Tk()
root.title('Exchange')
root.geometry('500x500')
Bath=StringVar()
Rate=StringVar()
Kip=StringVar()





lb1=Label(root,font=('time new roman',16),text='BATH TO KIP')
lb1.place(x=200,y=50)

lb2=Label(root,font=('time new roman',16),text='ENTER BATH :')
lb2.place(x=50,y=100)
txt1=Entry(root,font=('Times New Roman', 16),textvariable=Bath)
txt1.place (x=200, y=100)


lb3=Label(root,font=('Time new roman',16),text='ENTER RATE:')
lb3.place(x=50,y=150)
txt2=Entry(root,font=('Times New Roman', 16),textvariable=Rate)
txt2.place (x=200,y=150)

btn1=Button(root,font=('Times New Roman',16),width=10,text='EXCHANGE',command=B2K)
btn1.place(x=100,y=200)
btn2=Button(root,font=('Times New Roman',16),width=10,text='Clear',command=AllClear)
btn2.place(x=300,y=200)

lb4=Label(root,font=('Time new roman',16),text='TOTAL:')
lb4.place(x=50,y=250)
txt3=Entry(root,font=('Times New Roman', 16),textvariable=Kip)
txt3.place (x=150,y=250)


root.mainloop()