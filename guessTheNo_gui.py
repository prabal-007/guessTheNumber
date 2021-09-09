from tkinter import *
from PIL import Image, ImageTk
import time
import random
import tkinter.messagebox as tmsg

def start():
    root.destroy()
    root1=Tk()
    root1.iconbitmap('icon.ico')
    def exi():
        value = tmsg.askquestion('Exit','Exit, are you sure?')
        if value =='yes':
            root1.destroy()
    def mainlogic():
        global nog
        if nog >= 1:
                # Winner
            if e1.get() == answer:
                mes1ver.set(lis[0])
                mes2ver.set(lis[1])
                mes1 = Label(root1, textvariable=mes1ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                mes2 = Label(root1, textvariable=mes2ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                sco = 5-nog+1
                mes3ver.set(f'{lis[2]} : {sco}')
                mes3 = Label(root1, textvariable=mes3ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                    # break
                
            # Try Again
            else:
                mes1ver.set(lis[3])
                mes1 = Label(root1, textvariable=mes1ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                if e1.get() > answer:
                    mes2ver.set(lis[4])
                    mes2 = Label(root1, textvariable=mes2ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                    print("Tip: try a smaller number.")
                else:
                    mes2ver.set(lis[5])
                    mes2 = Label(root1, textvariable=mes2ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                    print("Tip: Try a larger number. ")
                nog -= 1
                mes3ver.set(f'{lis[6]} : {nog}')
                mes3 = Label(root1, textvariable=mes3ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
        # if GAME OVER
                if nog == 0:
                    mes1ver.set(lis[7])
                    mes2ver.set(lis[8])
                    mes3ver.set(f'the number was {answer}')
                    mes1 = Label(root1, textvariable=mes1ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                    mes2 = Label(root1, textvariable=mes2ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
                    mes3 = Label(root1, textvariable=mes3ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')

    root1.geometry('600x525')
    root1.maxsize(600,525)
    root1.configure(background='yellow')
    Label(root1, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root1.title('guessTheNO.')
    answer = str(random.randint(lvar.get(), uvar.get()))
    print(answer)
    lim = Label(root1, text=f'Upper Limit = {uvar.get()}\t\tLower Limit = {lvar.get()}', font='arial 12 bold',bg='olive', padx='5', pady='5')
    lim.pack(padx='10', pady='20')
    trynum = IntVar()
    e1 = Entry(root1, textvariable=trynum, font='arial 60 bold')
    e1.pack(padx='240', pady='20')
    trybutton = Button(root1, text='Enter', bg='green', font='arial 22 bold',activebackground='lime', command=mainlogic)
    trybutton.pack(pady='10')
    mes1ver = StringVar()
    mes1ver.set(lis[10])
    mes1ver.get()
    mes2ver = StringVar()
    mes2ver.set(lis[11])
    mes2ver.get()
    mes3ver = StringVar()
    mes3ver.set(lis[12])
    mes3ver.get()
    mes1 = Label(root1, textvariable=mes1ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
    mes2 = Label(root1, textvariable=mes2ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
    mes3 = Label(root1, textvariable=mes3ver, font='arial 15 bold', padx='5', pady='5').pack(padx='5', pady='5')
    frm=Frame(root1, bg='goldenrod')
    Button(frm, text='Quit',bg='red', font='arial 15 bold', relief=SUNKEN,activebackground='maroon', command=exi).pack(side=LEFT, padx='20', pady='10')
    Button(frm, text='HELP',bg='grey',  font='arial 15 bold', relief=SUNKEN,activebackground='silver', command=hel).pack(side=LEFT, padx='20', pady='10')
    Button(frm, text='Restart', bg='orange', font='arial 15 bold',activebackground='olive', command=exi).pack(side=RIGHT, padx='20', pady='10')
    Button(frm, text='ABOUT',bg='grey', font='arial 15 bold', relief=SUNKEN,activebackground='silver', command=about).pack(side=RIGHT, padx='20', pady='10')
    frm.pack(side=BOTTOM, fil=X)

    root1.mainloop()

def hel():
    # root.destroy()
    root2=Tk()
    root2.geometry('500x500')
    root2.configure(background='yellow')
    Label(root2, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root2.title('guessTheNO.- Help')
    head=Label(root2, text='HELP', font='arial 18 bold')
    head.pack(pady='20')
    cont=Label(root2, text='1. Enter integer values only.\n2. The range of number should not exceed 999.\n', font='arial 12 bold')
    cont.pack(pady='20')
    root2.mainloop()

def about():
    # root.destroy()
    root3=Tk()
    root3.geometry('500x500')
    Label(root3, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    root3.configure(background='yellow')
    root3.title('guessTheNO.- About')
    head=Label(root3, text='About', font='arial 18 bold')
    head.pack(pady='20')
    cont=Label(root3, text='Name - Guess the number\n\nVersion - strgtn0.1\n\nDeveloper - Prabal Gupta\n\ngithub - prabal-007', font='arial 12 bold')
    cont.pack(pady='20')
    root3.mainloop()

def exi():
    value = tmsg.askquestion('Exit','Exit, are you sure?')
    if value =='yes':
        root.destroy()
# def numimages():
#     img1 = Image.open('2.png')
#     pho1 = ImageTk.PhotoImage(img1)

#     lab1 = Label(image=pho1).place(x=50, y=200)

if __name__ == "__main__":
    # lowerLimit= 10
    # upperLimit = 20
    nog = 5
    # answer = str(random.randint(lowerLimit, upperLimit))
    # print(answer)
    lis = ['WINNER','Congratulation..You WON','number of gusses taken : ','Please try again',
    'Tip: try a smaller number','Tip: Try a larger number','Number of guesses left out of 5 : ','GAME OVER',
    'You loss','Better luck next time','Welcome',"Let's Play",'Best of luck']
    
    root = Tk()
    root.title('GuessTheNumber')
    # root.iconbitmap('icon.ico')
    root.geometry('500x500')
    root.configure(background = 'yellow')
    Label(root, text='by Prabal Gupta', anchor='e', fg='white', bg='black').pack(side=BOTTOM, fil=X)
    
    # img1 = Image.open('2.png')
    # pho1 = ImageTk.PhotoImage(img1)
    # lab1 = Label(image=pho1).place(x=50, y=200)

    Label(root, text='  Guess The No.  ', font='Algerian 20 bold', fg='white', bg='red', padx='10', relief=SUNKEN, borderwidth='10').pack(pady='25')
    frm1=Frame(root)
    Label(frm1, text='upperlimit', bg='orange', font='arial 12').pack(pady='4')
    uvar = IntVar()
    upperLimit = Scale(frm1, from_ = 0 , to = 100,variable=uvar, troughcolor='orange', resolution=2,sliderlength='5', width='10', 
    activebackground='red', orient= VERTICAL, tickinterval='50', bd='2', length='200', borderwidth='5')
    upperLimit.set('20')
    upperLimit.pack()
    frm1.pack(side=LEFT)
    frm2=Frame(root)
    Label(frm2, text='lowerlimit', bg='orange', font='arial 12').pack(pady='4')
    lvar = IntVar()
    lowerLimit = Scale(frm2, from_ = 0 , to = 100, variable=lvar, troughcolor='orange', resolution=2,sliderlength='5', width='10', 
    activebackground='red', orient= VERTICAL, tickinterval='50', bd='2', length='200', borderwidth='5')
    lowerLimit.set('10')
    lowerLimit.pack()
    frm2.pack(side=RIGHT)
    start = Button(root, text='START',bg='teal', font='arial 18 bold',activebackground='aqua', command=start)
    start.pack(padx='10', pady='10')
    Help = Button(root, text='HELP',bg='teal', font='arial 18 bold', relief=SUNKEN, padx='8',activebackground='aqua', command=hel)
    Help.pack(padx='10', pady='10')
    about = Button(root, text='ABOUT',bg='teal', font='arial 18 bold', relief=SUNKEN,activebackground='aqua', command=about)
    about.pack(padx='10', pady='10')
    exi = Button(root, text='EXIT',bg='teal',  font='arial 18 bold', relief=SUNKEN, padx='13',activebackground='aqua', command=exi)
    exi.pack(padx='10', pady='10')    

    root.mainloop()
