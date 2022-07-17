from tkinter import *

root = Tk()
root.title("PAPAN SKOR")
root.geometry("650x250")
root.configure(bg="#ffffff")

var1 = StringVar()
team1 = Entry(root, width=8, borderwidth=0)
var1.set("TEAM 1")
team1['textvariable'] = var1
team1['font'] = 'NORMAL, 109'
team1['justify'] = 'center'
team1['fg'] = 'white'
team1['bg'] = '#81b1ef'
team1.grid(row=0, column=0, columnspan=2, padx=15, pady=15)

babak1 = Entry(root, width=17, borderwidth=0)
babak1['font'] = 'NORMAL, 51'
babak1['justify'] = 'center'
babak1['fg'] = 'white'
babak1['bg'] = '#81b1ef'
babak1.grid(row=1, column=0, columnspan=2, padx=15, pady=15)

score1 = Entry(root, width=3, borderwidth=0)
score1['bg'] = '#81b1ef'
score1['font'] = 'NORMAL, 290'
score1['justify'] = 'center'
score1['fg'] = 'white'
score1.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

var2 = StringVar()
team2 = Entry(root, width=8, borderwidth=0)
var2.set("TEAM 2")
team2['textvariable'] = var2
team2['font'] = 'NORMAL, 109'
team2['justify'] = 'center'
team2['fg'] = 'white'
team2['bg'] = '#cc5279'
team2.grid(row=0, column=2, columnspan=2, padx=15, pady=15)

babak2 = Entry(root, width=17, borderwidth=0)
babak2['font'] = 'NORMAL, 51'
babak2['justify'] = 'center'
babak2['fg'] = 'white'
babak2['bg'] = '#cc5279'
babak2.grid(row=1, column=2, columnspan=2, padx=15, pady=15)

score2 = Entry(root, width=3, borderwidth=0)
score2['bg'] = '#cc5279'
score2['font'] = 'NORMAL, 290'
score2['justify'] = 'center'
score2['fg'] = 'white'
score2.grid(row=2, column=2, columnspan=2, padx=30, pady=15)

def start(strt):
    score1.delete(0, END)
    score1.insert(0, strt)
    score2.delete(0, END)
    score2.insert(0, strt)
    babak1.insert(0, strt)
    babak2.insert(0, strt)
    global s_awal
    s_awal = strt

def end(e):
    score1.delete(0, END)
    score1.insert(0, e)
    score2.delete(0, END)
    score2.insert(0, e)
    global s_end
    s_end = e

def end2(e):
    babak1.delete(0, END)
    babak1.insert(0, e)
    babak2.delete(0, END)
    babak2.insert(0, e)
    global s_end
    s_end = e

def plus(pls):
    a = score1.get()
    score1.delete(0, END)
    b = int(a)
    score1.insert(0, pls + b)

def plus2(pls):
    a = score2.get()
    score2.delete(0, END)
    b = int(a)
    score2.insert(0, pls + b)

def minus(mns):
    a = score1.get()
    score1.delete(0, END)
    b =int(a)
    score1.insert(0, b - mns)

def minus2(mns):
    a = score2.get()
    score2.delete(0, END)
    b =int(a)
    score2.insert(0, b - mns)

def babakplus(bbkpls):
    a = babak1.get()
    babak1.delete(0, END)
    b = int(a)
    babak1.insert(0, bbkpls + b)

def babakplus2(bbkpls):
    a = babak2.get()
    babak2.delete(0, END)
    b = int(a)
    babak2.insert(0, bbkpls + b)

def babakminus(bbkmns):
    a = babak1.get()
    babak1.delete(0, END)
    b =int(a)
    babak1.insert(0, b - bbkmns)

def babakminus2(bbkmns):
    a = babak2.get()
    babak2.delete(0, END)
    b =int(a)
    babak2.insert(0, b - bbkmns)

def btn(x, y, font, text, width, height, bgcolor, fgcolor, cmd):

    def on_enter(e):
        myBtn['background'] = bgcolor
        myBtn['foreground'] = fgcolor

    def on_leave(e):
        myBtn['background'] = fgcolor
        myBtn['foreground'] = bgcolor

    myBtn = Button(root, width=width, height=height)
    myBtn['border'] = 0
    myBtn['font'] = font
    myBtn['text'] = text
    myBtn['fg'] = bgcolor
    myBtn['bg'] = fgcolor
    myBtn['activeforeground'] = fgcolor
    myBtn['activebackground'] = bgcolor
    myBtn['command'] = cmd
    myBtn.bind('<Enter>', on_enter)
    myBtn.bind('<Leave>', on_leave)
    myBtn.place(x=x, y=y)

btn(664, 15, 'NORMAL, 5', "Start", '10', '13', '#ffffff', '#141414', cmd=lambda:start(0))
btn(664, 102, 'NORMAL, 5',"End", '10', '11', '#ffffff', '#141414', cmd=lambda:end(0))
btn(664, 210, 'NORMAL, 5',"Reset", '10', '11', '#ffffff', '#141414', cmd=lambda:end2(0))
btn(568, 210, 'NORMAL, 11',"+", '10', '4', '#81b1ef', '#141414', cmd=lambda:babakplus(1))
btn(1261, 210, 'NORMAL, 11',"+", '10', '4', '#cc5279', '#141414', cmd=lambda:babakplus2(1))
btn(15, 210, 'NORMAL, 11',"-", '10', '4', '#81b1ef', '#141414', cmd=lambda:babakminus(1))
btn(709, 210, 'NORMAL, 11',"-", '10', '4', '#cc5279', '#141414', cmd=lambda:babakminus2(1))
btn(617, 480, 'NORMAL, 5',">", '10', '15', '#81b1ef', '#141414', cmd=lambda:plus(1))
btn(1311, 480, 'NORMAL, 5',">", '10', '15', '#cc5279', '#141414', cmd=lambda:plus2(1))
btn(16, 480, 'NORMAL, 5',"<", '10', '15', '#81b1ef', '#141414', cmd=lambda:minus(1))
btn(710, 480, 'NORMAL, 5',"<", '10', '15', '#cc5279', '#141414', cmd=lambda:minus2(1))

root.attributes('-fullscreen', True)
root.mainloop()