from tkinter import *
from textblob import TextBlob
import textblob
def correcttheword():
    imput = word1.get()
    obj=TextBlob(imput)
    cw=obj.correct()
    word2.delete(0,END)
    word2.insert(10,cw)
def clearall():
    word2.delete(0,END)
    word1.delete(0,END)
if __name__ == "__main__":
    root=Tk()
    root.configure(background='lightgreen')
    root.geometry("500x300")
    root.title('Spelling Checker')
    header=Label(root,text='Welcome To The Spelling Checker App',fg='black',bg='white')
    header.grid(row=0,column=1)
    L1=Label(root,text="Input Word: ", fg="black", bg="white")
    L1.grid(row=1,column=1,pady=10)
    word1=Entry()
    word1.grid(row=1,column=2)
    L2=Label(root,text="Corrected Word: ", fg="black", bg="white")
    L2.grid(row=3,column=1,pady=10)
    word2=Entry()
    word2.grid(row=3,column=2)
    button1=Button(root,text='Correct',bg='white',fg='black',command=correcttheword)
    button1.grid(row=2, column=2, pady=10)
    button2=Button(root,text='Clear All',bg='white',fg='black',command=clearall)
    button2.grid(row=4, column=2, pady=10)
    root.mainloop()