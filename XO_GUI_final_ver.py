from tkinter import *
from tkinter.messagebox import *
from tkinter import messagebox
import random
import copy

xo = { 0: {0: 0, 1: 1, 2: 2},1: {0: 3, 1: 4, 2: 5},2: {0: 6, 1: 7, 2: 8} }

top = Tk()
top.title('Before playing')
top.geometry('430x270')

#TK1: welcome message
wlcmL = Label(top,text='WELCOME. \nFill the following to continue,\n',font=('Helvatical bold',10)).grid(row=0, column=0)

#TK2: readio Buttons
def dopvb(): ##prepare pvb match
    text2.delete(1.0,END)
    text2.insert(END,'AI')
    text2.config(state = DISABLED)
    ezRB.config(state=NORMAL)
    hardRB.config(state=NORMAL)
def dopvp(): ##prepare pvp match
    text2.config(state = NORMAL)
    text2.delete(1.0,END)
    ezRB.config(state=DISABLED)
    hardRB.config(state=DISABLED)
v=IntVar()
v.set(1) #pvp or pvb?
pvpRB = Radiobutton(top,text='PVP',variable=v, value =1,command = lambda: dopvp()).grid(row=1, column=0)
pvbRB = Radiobutton(top,text='PVB ',variable=v, value =0,command = lambda: dopvb()).grid(row=1, column=1) 

e=IntVar()
e.set(1) #easy/hard mode
ezRB = Radiobutton(top,text='Easy',state=DISABLED,variable=e, value =1)
ezRB.grid(row=2, column=0)
hardRB = Radiobutton(top,text='Hard',state=DISABLED,variable=e, value =0)
hardRB.grid(row=2, column=1)

l=StringVar()
l.set('x') #select x or o
letter1RB = Radiobutton(top,text='Player1 has x',variable=l, value ='x').grid(row=5, column=0)
letter2RB = Radiobutton(top,text='Player1 has o',variable=l, value ='o').grid(row=5, column=1)

f=IntVar()
f.set(1) #who plays first?
p1FirstRB = Radiobutton(top,text='Player1 first   ',variable=f, value =1).grid(row=6, column=0)
p1SecRB =   Radiobutton(top,text='Player2 first   ',variable=f, value =0).grid(row=6, column=1)

#TK3: text boxes the thier LABELS
label1 = Label(top, text='Player1 name ').grid(row=3, column=0)
text1 = Text(top, width=25,height=1)
text1.grid(row=3, column=1)
label2 = Label(top, text='Player2 name ').grid(row=4, column=0)
text2 = Text(top, width=25,height=1)
text2.grid(row=4, column=1)

#TK3: buttons
def readyToPlay(): ##for play button
    global name1
    global name2
    global pvp
    global p1First
    global letter1
    global letter2
    global turn
    global ezMode

    name1=str(text1.get(1.0,"end-1c"))
    name2=str(text2.get(1.0,"end-1c"))
    pvp = int(v.get())
    ezMode = int(e.get())
    p1First = int(f.get())
    turn = p1First
    letter1= l.get()
    if letter1 == 'o':
        letter2= 'x'
    else:
        letter2= 'o'

    if not (name1.strip() and name2.strip()):
        messagebox.showwarning("Warning", "Not valid names!")
    else:
        playPage()
cancelB = Button(top,text="Cancel", width=20,height=4, command= lambda: exit() ).grid(row=7, column=0)
playB =   Button(top,text="Play", width=35 ,height=4, command= lambda: readyToPlay()).grid(row=7, column=1)

def playPage(): ## play page
    play = Toplevel(top)
    play.title('X O game')
    play.geometry('580x850')

    #TK4: play buttons 
    size = 30
    h=5 #height of buttons
    w=8 #width of buttons
    b0 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b0,0,0))
    b0.grid(row=0, column=0)
    b1 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b1,0,1))
    b1.grid(row=0, column=1)
    b2 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b2,0,2))
    b2.grid(row=0, column=2)

    b3 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b3,1,0))
    b3.grid(row=1, column=0)
    b4 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b4,1,1))
    b4.grid(row=1, column=1)
    b5 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b5,1,2))
    b5.grid(row=1, column=2)

    b6 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b6,2,0))
    b6.grid(row=2, column=0)
    b7 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b7,2,1))
    b7.grid(row=2, column=1)
    b8 = Button(play,text="-",height=h,width=w,font=('Helvatical bold',size),command= lambda:playxo(b8,2,2))
    b8.grid(row=2, column=2)

    buttonList = [b0,b1,b2,b3,b4,b5,b6,b7,b8]

    def disableB(B): ##set of functiions for enabling/disableing
        B['state']=DISABLED
    def enableB(B):
        B['state']=NORMAL
    def disableAllB():
        for i in buttonList:
         i['state']=DISABLED
    def enableAllB():
        for i in buttonList:
         i['state']=NORMAL

    def playxo(B,r,c): ##playing function, a player presses a button
        global turn
        if turn:
            B.config(text=letter1)
            xo[r][c]=letter1
            turn-=1
            if checkWin(letter1,xo):
                theWinnerIs(letter1)
                return 0
        else:
            B.config(text=letter2)
            xo[r][c]=letter2
            turn+=1
            if checkWin(letter2,xo):
                theWinnerIs(letter2)
                return 0

        B['state']=DISABLED
        for i in buttonList:
            if i['state'] == NORMAL:
                if not pvp:
                    AIplay()
                return 0
        theWinnerIs('none')

    def checkWin(s, dict): ## ckeck if x/o wins 
     for r in range(0,3): # check rows
      if dict[r][0] == s and dict[r][1] == s and dict[r][2] == s:
         return 1

     for c in range(0,3): # check colums
      if dict[0][c] == s and dict[1][c] == s and dict[2][c] == s:
         return 1
    
    # check exceptions. They are two: two diagonals
     if dict[1][1] == s and ((dict[0][0] == s and dict[2][2] == s) or (dict[2][0] == s and dict[0][2] == s)):
         return 1

     return 0 # if no win return false

    def theWinnerIs(s): ## detrmain the winner
        disableAllB()
        if s == 'none':
            messagebox.showinfo("DRAW", "No one wins")
        elif letter1 == s:
            messagebox.showinfo(s+" WINS", name1+" wins")
        else:
            messagebox.showinfo(s+" WINS", name2+" wins")

    def on_closePlay(): ## user closes the play page. OR presses cancel
        resetMatrix()
        play.destroy()
    play.protocol("WM_DELETE_WINDOW", on_closePlay)

    def RESTART(): ## restart button
        resetMatrix()
        if not pvp and not p1First:
            AIplay()
    cancelB = Button(play,text="Cancel",font=('Helvatical bold',size),command= lambda: on_closePlay()).grid(row=3, column=0)
    restartB = Button(play,text="Restart",font=('Helvatical bold',size), command= lambda: RESTART()).grid(row=3, column=2)

    def resetMatrix(): ## reset matrix to orignal for more readiability for user
     global turn
     turn = p1First
     counter = -1
     for r in range(0,3):
        for c in range(0,3):
            counter=counter+1
            xo[r][c] = counter
     for i in buttonList:
         i['state']=NORMAL
         i.config(text="-")

    #all the following is regarding the boot/AI
    def AIrandom(): ##random choise by boot
        randomList=[]
        counter = 0
        for r in range(0,3):
            for c in range(0,3):
                if isAvlbl(r, c):
                    randomList.append(counter)
                counter+=1
        return randomList

    def AImove(letter,dic,index):
        write(letter, dic, index)
        buttonList[index].config(text=letter)
        disableB(buttonList[index])

    def AIplay(): ## AI plays
        global turn
        randomList = []
        if not ezMode:
            for x in range(0,9):
                templist = copy.deepcopy(xo)
                write(letter2, templist, x)
                if checkWin(letter2, templist):
                    AImove(letter2,xo,x)
                    turn+=1
                    if checkWin(letter2,xo):
                        theWinnerIs(letter2)
                    return 0

            for x in range(0,9):
                templist = copy.deepcopy(xo)
                write(letter1, templist, x)
                if checkWin(letter1, templist):
                    AImove(letter2,xo,x)
                    turn+=1
                    if checkWin(letter2,xo):
                        theWinnerIs(letter2)
                    return 0

            if not isAvlbl(1,1): # if the middle not avaliable

              if isAvlbl(0,0): # secound eadges
                  randomList.append(0)
              if isAvlbl(2,2):
                  randomList.append(8)
              if isAvlbl(2,0):
                  randomList.append(6)
              if isAvlbl(0,2):
                  randomList.append(2)
              if randomList == []:      # last "whatever"
                randomList = AIrandom()

              AImove(letter2,xo,random.choice(randomList))
              randomList.clear()
            else:
                AImove(letter2,xo,4)
        else: # ez mode 
            randomList = AIrandom()
            AImove(letter2,xo,random.choice(randomList))
            randomList.clear()
        turn+=1
        if checkWin(letter2,xo):
            theWinnerIs(letter2)
        else:
            for i in buttonList:
                if i['state'] == NORMAL:
                    return 0
            disableAllB()
            theWinnerIs('none')

    def isAvlbl(index1, index2): ## is the index avilable?
      if xo[index1][index2] == 'x' or xo[index1][index2] == 'o':
         return 0
      else:
         return 1

    def write(letter,dic,p): ## writing on the matrix x or o with given list for the machien.
        if p <= 2:
            if isAvlbl(0,p):
                dic[0][p] = letter     
        elif p <= 5:
            if isAvlbl(1,p-3):
                dic[1][p-3] = letter
        elif p <= 8:
            if isAvlbl(2,p-6):
                dic[2][p-6] = letter

    if not pvp and not p1First:
        AIplay()
    mainloop()
mainloop()