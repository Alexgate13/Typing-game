from tkinter import *
import random

Sentenses = ["Forest door hidden, waiting.", "City shadows whisper secrets.", "Lone figure on stormy cliff.", "Eyes meet in market crowd.", "Old lighthouse glows eerie light.", "Girl holds key to reality.", "Riverton freezes at midnight.", "Rain, unexpected visitor arrives."]

score = 0
timer = 120

screen = Tk()
screen.geometry('350x200')
screen.title('My first window')
screen.configure(background="black")

def startgame(event):
    nextSentens()
    if timer == 120:
        countdown()


def countdown():
    global timer
    if timer > 0:
        timer -= 1
        lbl8.configure(text="Time:" + str(timer))
        lbl8.after(1000, countdown)



def nextSentens():
    global score
    if timer > 0:
        if e.get() == Sentenses[0]:
            score += 1
        lbl7.configure(text="Score:" + str(score))
        e.delete(0, END)
        random.shuffle(Sentenses)
        print(Sentenses)
        lbl5.configure(text=Sentenses[0])


lbl1 = Label(screen, text="Type in these fast as you can the setenses", background="black", foreground="white")
lbl1.grid(row=0, column=1)

lbl2 = Label(screen, text="  ", background="black")
lbl2.grid(row=1, column=1)

lbl3 = Label(screen, text="Pres <Enter> to begin", background="black", foreground="white")
lbl3.grid(row=2, column=1)

lbl4 = Label(screen, text="  ", background="black")
lbl4.grid(row=3, column=1)

lbl5 = Label(screen, text="......", font=("Tahoma", 10), background="black", foreground="white")
lbl5.grid(row=4, column=1)

lbl6 = Label(screen, text="  ", background="black")
lbl6.grid(row=5, column=1)


lbl7 = Label(screen, text="score:0", background="black", foreground="white")
lbl7.grid(row=4, column=3)

lbl8 = Label(screen, text="Time left:120", background="black", foreground="white")
lbl8.grid(row=2, column=3)


lbl9 = Label(screen, text="    ", background="black")
lbl9.grid(row=2, column=2)

lbl9 = Label(screen, text="    ", background="black")
lbl9.grid(row=4, column=2)

e = Entry(screen)
e.grid(row=6, column=1)
e.focus_set()
screen.bind('<Return>', startgame)





screen.mainloop()