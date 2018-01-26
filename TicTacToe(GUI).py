from tkinter import *
import tkinter.messagebox

master=Tk()

master.title('TicTacToe')

global player, P1, P2, empty, num1, num2, num3, num4, num5, num6, num7, num8, num9

player = True
P1 = 'x'
P2 = 'o'
empty = ' '

num1 = True
num2 = True
num3 = True
num4 = True
num5 = True
num6 = True
num7 = True
num8 = True
num9 = True

back = empty

def check():
    #horizontal
    if button1['text'] == 'x' and button2['text'] == 'x' and button3['text'] == 'x':
            return '\nPlayer1 Is the Winner'
    elif button4['text'] == 'x' and button5['text'] == 'x' and button6['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    elif button7['text'] == 'x' and button8['text'] == 'x' and button9['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    #vertical
    elif button1['text'] == 'x' and button4['text'] == 'x' and button7['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    elif button2['text'] == 'x' and button5['text'] == 'x' and button8['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    elif button3['text'] == 'x' and button6['text'] == 'x' and button9['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    #diagonal
    elif button1['text'] == 'x' and button5['text'] == 'x' and button9['text'] == 'x':
        return '\nPlayer1 Is the Winner'
    elif button3['text'] == 'x' and button5['text'] == 'x' and button7['text'] == 'x':
        return '\nPlayer1 Is the Winner'

        # player2
    elif button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    elif button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    elif button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    #vertical
    elif button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    elif button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    elif button3['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    #diagonal
    elif button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o':
        return '\nPlayer2 Is the Winner'
    elif button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o':
        return '\nPlayer2 Is the Winner'

def change1():
    check()
    if check() == None:
        if num1 == True:
            if player == True:
                button1.configure(text=P1, bg="blue")
                global player, back
                player = False
                back = P1
            elif player == False:
                button1.configure(text=P2, bg="deep pink")
                global player, back
                player = True
                back = P1
            global num1
            num1 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change2():
    check()
    if check() == None:
        if num2 == True:
            if player == True:
                button2.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button2.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num2
            num2 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change3():
    check()
    if check() == None:
        if num3 == True:
            if player == True:
                button3.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button3.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num3
            num3 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change4():
    check()
    if check() == None:
        if num4 == True:
            if player == True:
                button4.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button4.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num4
            num4 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change5():
    check()
    if check() == None:
        if num5 == True:
            if player == True:
                button5.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button5.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num5
            num5 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change6():
    check()
    if check() == None:
        if num6 == True:
            if player == True:
                button6.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button6.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num6
            num6 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change7():
    check()
    if check() == None:
        if num7 == True:
            if player == True:
                button7.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button7.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num7
            num7 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change8():
    check()
    if check() == None:
        if num8 == True:
            if player == True:
                button8.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button8.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num8
            num8 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))
def change9():
    check()
    if check() == None:
        if num9 == True:
            if player == True:
                button9.configure(text=P1, bg="blue")
                global player
                player = False
            elif player == False:
                button9.configure(text=P2, bg="deep pink")
                global player
                player = True
            global num9
            num9 = False
        else:
            print('Position Taken')
    else:
        tkinter.messagebox.showinfo("WInner Of TicTacToe", "{}".format(check()))

button1=Button(master,text=back, font='Arial 32', width=3,foreground="white", command=change1)
button1.grid(row=1,column=1)

button2=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change2)
button2.grid(row=1,column=2)

button3=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change3)
button3.grid(row=1,column=3)

button4=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change4)
button4.grid(row=2,column=1)

button5=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change5)
button5.grid(row=2,column=2)

button6=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change6)
button6.grid(row=2,column=3)

button7=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change7)
button7.grid(row=3,column=1)

button8=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change8)
button8.grid(row=3,column=2)

button9=Button(master, text=" ", font='Arial 32', width=3,foreground="white", command=change9)
button9.grid(row=3,column=3)

master.mainloop()             