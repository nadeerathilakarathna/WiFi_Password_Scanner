import tkinter as tk
import os
import time
from tkinter import *
import os.path


def show():
    print("Selected value :", optionVar.get())
    A=optionVar.get()
    def UserCMD():
        if ((os.path.exists('Data\SYS.vbs'))==False):
            fy=open("Data\SYS.vbs","w")
            fy.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "Data\SYS.cmd" & Chr(34), 0\nSet WshShell = Nothing')
            fy.close()
        
        f=open("Data\SYS.cmd","w")
        f.write("netsh wlan show profiles \""+A+"\" Key=clear >>Data\SYS.txt")
        time.sleep(1.5)
        f.close()
        command="Data\SYS.vbs"
        os.system(command)
        time.sleep(1.5)

        f.close()


        os.remove('Data\SYS.cmd')
          
        f=open("Data\SYS.txt","r")
        user=0
        X=f.readlines()
        T2=[]
        B=0
        C=0
        Z=-1
        Y=-1

        P=(X[Z])
      
        while(P[4:18]!='Authentication'):
            Z=Z-1
            P=(X[Z])
        
        P=(P[29:-1])


        if (P=='Open'):
            Pass="No Password"

        if (P!='Open'):
            Pass=(X[Y])
            try:
                while (Pass[4:15]!='Key Content'):
                    Y=Y-1
                    Pass=(X[Y])
            except:
                f.close()
                admin()
                
            Pass=(Pass[29:-1])

        T2.append(P)
        T2.append(Pass)

        f.close()

        os.remove('Data\SYS.txt')

        print (T2)
        e1.delete(0,END)
        e1.insert(0,optionVar.get())
        e2.delete(0,END)
        e2.insert(0,P)
        e3.delete(0,END)
        e3.insert(0,Pass)

    UserCMD()


#admin error=========================================================================
#==============================================================================

def admin():
    os.remove('Data\SYS.txt')
    admin = tk.Tk()
    
    admin.title("")
    admin.geometry("+{}+{}".format(positionRight-65, positionDown-50))
    def a(x=0):
        admin.destroy()
    admin.configure(bg='#171e24')
    admin.bind('<Return>',a)
    admin.iconbitmap('Data\icon.ico')
    admin.focus_force()

    eL12=Label(admin,text="")
    eL12.config(width=44, font=('Helvetica', 8),)
    eL12.grid(row = 0, column = 0, sticky = S, pady = 2)
    eL12.configure(bg='#171e24')

    eL11=Label(admin,text="Administrative Privileges Required.")
    eL11.config( font=('Helvetica', 15),fg='red')
    eL11.grid(row = 1, column = 0, sticky = S, pady = 8)
    eL11.configure(bg='#171e24')

    eL13=Label(admin,text='Administrator privileges are required for this software to work properly.\nRestart the software into the "Run as administrator" mode.')
    eL13.config(width=55, font=('Helvetica', 11),fg='#FFFFFF')
    eL13.grid(row = 2, column = 0, sticky = S, pady = 10)
    eL13.configure(bg='#171e24')
   
    E2B1 = Button(admin, text="OK", command=admin.destroy,)
    E2B1.config(width=15, font=('Helvetica', 11),fg="#FFFFFF",bg='#2e2e2e',activebackground="#404040")
    E2B1.grid(row = 3, column = 0, sticky = S, pady =20,)

    admin.mainloop()




#Error=========================================================================
#==============================================================================

def error():
    error = tk.Tk()
    error.title("")
    error.resizable(0,0)
    error.geometry("+{}+{}".format(positionRight, positionDown))
    def a(x=0):
        error.destroy()
    error.configure(bg='#171e24')
    error.bind('<Return>',a)
    error.iconbitmap('Data\icon.ico')
    error.focus_force()

    eL2=Label(error,text="")
    eL2.config(width=44, font=('Helvetica', 12),)
    eL2.grid(row = 0, column = 0, sticky = S, pady = 2)
    eL2.configure(bg='#171e24')

    eL1=Label(error,text="There is no data about the routers used\non this computer.")
    eL1.config( font=('Helvetica', 12),fg='#FFFFFF')
    eL1.grid(row = 1, column = 0, sticky = S, pady = 10)
    eL1.configure(bg='#171e24')

    EB1 = Button(error, text="OK", command=error.destroy,)
    EB1.config(width=15, font=('Helvetica', 11),fg="#FFFFFF",bg='#2e2e2e',activebackground="#404040")
    EB1.grid(row = 2, column = 0, sticky = S, pady =10,)

    error.mainloop()


#Coding=============================================================================
#======================================================================================

def UserCMD():
    if ((os.path.exists('Data\system.vbs'))==False):
        fx=open("Data\system.vbs","w")
        fx.write('Set WshShell = CreateObject("WScript.Shell")\nWshShell.Run chr(34) & "Data\system.cmd" & Chr(34), 0\nSet WshShell = Nothing')
        fx.close()

    f=open("Data\system.cmd","w")
    f.write("netsh wlan show profiles >>Data\system.txt")
    f.close()
    time.sleep(1)
    


def ReadUser():
    UserCMD()
    command="Data\system.vbs"
    os.system(command)
    time.sleep(2)
    
    f=open("Data\system.txt","r")
    f2=open("Data\system.txt","r")
    user=0
    A=f.readlines()
    U=[]
    B=0
    C=0
    V='X'

    while (B!="    All User Profile"):
        B=f2.readline(20)
        C=C+1
        if (C==1000):
            break

    while (B!="\n"):
        if (C==1000):
            break
        
        user=(A[C-5])
        if(user[0:5]=='-----'):
            user=(A[C-4])
            V='W10'
        user=user[27:-1]
        if(user==''):
            break
        U.append(user)
        B=f2.readline()
        C=C+1
        if (V=='W10'):
            V='OK'
            C=C+1

    f.close()
    f2.close()

    os.remove('Data\system.cmd')
    os.remove('Data\system.txt')

    if(len(U)==0):
        error()
    elif(len(U)!=0):
        btnShow.config(state=NORMAL)
        option.config(state=NORMAL)
        U=tuple(U)
        
        option.children['menu'].delete(0,'end')
        optionVar.set(U[0])    
        
        for x in U:
            option.children['menu'].add_command(label=x,command=lambda a=x: optionVar.set(a))

global T


#Interface=============================================================================
#======================================================================================

T=['...',]
T=(tuple(T))

# Top level window 
window = Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()

positionRight = int(window.winfo_screenwidth()/2 - windowWidth/2)
PR =positionRight-250
positionDown = int(window.winfo_screenheight()/2 - windowHeight/2)
PD=positionDown-150

window.title("Wifi Inspector")
window.geometry('670x400')
window.geometry("+{}+{}".format(PR, PD))

window.configure(bg='#171e24')
window.iconbitmap('Data\icon.ico')
window.resizable(0,0)

# Option menu variable
optionVar = StringVar()
optionVar.set(T[0])


# Create a option menu
option = OptionMenu(window, optionVar,*T)
option.grid(row = 6, column = 1, sticky = W, pady =2 )
option.configure(bg='#2e2e2e',state='disabled',width=15,fg='#CCCCCC',activebackground="#404040")
option['menu'].config(font=('Helvetica',(12)),bg='#404040',fg='black',activebackground="black")

Lable1=Label(window,text="Router Name:")
Lable1.config(width=15, font=('Helvetica', 12),fg="#FFFFFF")
Lable1.grid(row = 6, column = 0, sticky = E, pady = 0)
Lable1.configure(bg='#171e24')

Lable3=Label(window,text="")
Lable3.grid(row = 10, column = 0, sticky = E,columnspan=2)
Lable3.configure(bg='#171e24')

b1=Button(window,text="Scan Routers", command=ReadUser)
b1.config(width=15,height=4, font=('Helvetica', 12),fg="#FFFFFF",bg='#2e2e2e',activebackground="#404040")
b1.grid(row=1,column=0,columnspan=2,rowspan=5,sticky = N,pady = 20)

L1=Label(window,text="Username \t:")
L1.config(width=16, font=('Helvetica', 10),fg="#FFFFFF")
L1.grid(row = 2, column = 3, sticky = E, pady =10)
L1.configure(bg='#171e24')

L2=Label(window,text="Authentication \t:")
L2.config(width=16, font=('Helvetica', 10),fg="#FFFFFF")
L2.grid(row = 3, column = 3, sticky = E, pady =10)
L2.configure(bg='#171e24')

L3=Label(window,text="Password \t:")
L3.config(width=16, font=('Helvetica', 10),fg="#FFFFFF")
L3.grid(row = 4, column = 3, sticky = E, pady =10)
L3.configure(bg='#171e24')

username=StringVar()
e1=Entry(window,textvariable=username)
e1.config(width=20, font=('Helvetica', 11))
e1.grid(row = 2, column = 4, sticky = W, pady = 2)
e1.configure(bg='#1c2a35',fg='#FFFFFF')

auth=StringVar()
e2=Entry(window,textvariable=auth)
e2.config(width=20, font=('Helvetica', 11),)
e2.grid(row = 3, column = 4, sticky = W, pady = 2)
e2.configure(bg='#1c2a35',fg='#FFFFFF')

passw=StringVar()
e3=Entry(window,textvariable=passw)
e3.config(width=20, font=('Helvetica', 11))
e3.grid(row = 4, column = 4, sticky = W, pady = 2)
e3.configure(bg='#1c2a35',fg='#FFFFFF')

Lable1=Label(window,text="")
Lable1.config(width=12, font=('Helvetica', 12))
Lable1.grid(row = 5, column = 0, sticky = E, pady = 10)
Lable1.configure(bg='#171e24')



# Create button with command
btnShow = Button(window, text="Find Password", command=show)
btnShow.config(width=15,height=1, font=('Helvetica', 11),state='disabled',activebackground="#404040",fg='#FFFFFF',bg='#2e2e2e')
btnShow.grid(row = 7, column = 0, sticky = S, pady = 20,columnspan=2)

logo = PhotoImage(file="Data\head.png",)
line = PhotoImage(file="Data\line.png",)
LD = PhotoImage(file="Data\LD.png",)

Lable10=Label(window,image=logo)
Lable10.config( font=('Helvetica', 12))
Lable10.grid(row = 0, column = 0, sticky = S, pady = 10, columnspan=1100)
Lable10.configure(bg='#171e24')

LableL=Label(window,image=line)
LableL.config( font=('Helvetica', 12))
LableL.grid(row = 1, column = 3, sticky = N+W, pady = 0, rowspan=9)
LableL.configure(bg='#171e24')

LableLD=Label(window,image=LD)
LableLD.config( font=('Helvetica', 12))
LableLD.grid(row = 10, column = 0, sticky = E, pady = 0, columnspan=3)
LableLD.configure(bg='#171e24')

LableLD2=Label(window,image=LD)
LableLD2.config( font=('Helvetica', 12))
LableLD2.grid(row = 10, column = 3, sticky = E, pady = 0, columnspan=3)
LableLD2.configure(bg='#171e24')

Lable1=Label(window,text="Developed by: Nadeera Thilakarathna")
Lable1.config(width=40, font=('Helvetica', 10))
Lable1.grid(row =9, column = 0, sticky = E+N, pady = 500,columnspan=10)
Lable1.configure(bg='#171e24',fg='#FFFFFF')

Lable1=Label(window,text="Developed by: Nadeera Thilakarathna")
Lable1.config(width=28, font=('Helvetica', 10))
Lable1.grid(row =7, column = 0, sticky = E+S, pady = 0,columnspan=6)
Lable1.configure(bg='#171e24',fg='#FFFFFF')

Lable1=Label(window,text='100')
Lable1.config(width=1, font=('Helvetica', 10))
Lable1.grid(row =100, column = 2, sticky = E, pady = 100,columnspan=1)
Lable1.configure(bg='#171e24',fg='#FFFFFF')

positionRight = positionRight-100
window.mainloop()











