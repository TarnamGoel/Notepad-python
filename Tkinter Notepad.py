# -*- coding: utf-8 -*-
"""
Created on Sun May 23 22:26:55 2021

@author: jagra
"""

from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename,asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled-Notepad")
    file=None#To reset file
    TextArea.delete(1.0,END)#It deletes the written text from 1st line 0th character to end
    
def openFile():
    global file
    file=askopenfilename(defaultextension=".txt",filetypes=[("All files","*.*"),("Text Documents","*.txt")])
    #in file types in all files we said that we can open any file but if it is text file then open file which have .txt extension
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"-Notepad")
        TextArea.delete(1.0,END)
        f=open(file,"r")
        TextArea.insert(1.0,f.read())
        f.close()
        #here we deleted previous written text and then added the text of the file that we opened

def saveFile():
    global file
    if file==None:
        file=asksaveasfilename(initialfile="Untitled.txt",defaultextension=".txt",
                               filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            file=None
        else:
            #Save as a new file
            f=open(file,"w")
            f.write(TextArea.get(1.0,END))
            f.close()
            
            root.title(os.path.basename(file)+"-Notepad")
    else:
        f=open(file,"w")
        f.write(TextArea.get(1.0,END))
        f.close()
        

def quitApp():
    root.destroy()

def cut():
    TextArea.event_generate(("<<Cut>>"))#cut is present in this function of tkinter

def copy():
    TextArea.event_generate(("<<Copy>>"))#copy is present in this function of tkinter

def paste():
    TextArea.event_generate(("<<Paste>>"))

def about():
    tmsg.showinfo("Notepad","Notepad by Tarnam #Coder")

if __name__=='__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled-Notepad")
    root.geometry("655x455")
    
    #Text Area
    TextArea=Text(root,font="lucida 13")
    file=None
    TextArea.pack(expand=True,fill=BOTH)
    
    #Creating menu bar
    MenuBar=Menu(root)
    FileMenu=Menu(MenuBar,tearoff=0)
    
    #Adding commands
    FileMenu.add_command(label="New",command=newFile)
    FileMenu.add_command(label="Open",command=openFile)
    FileMenu.add_command(label="Save",command=saveFile)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit",command=quitApp)
    
    MenuBar.add_cascade(label="File",menu=FileMenu)
    
    #Creating edit menu bar
    EditMenu=Menu(MenuBar,tearoff=0)
    
    #Adding commands
    EditMenu.add_command(label="Cut",command=cut)
    EditMenu.add_command(label="Copy",command=copy)
    EditMenu.add_command(label="Paste",command=paste)
    
    MenuBar.add_cascade(label="Edit",menu=EditMenu)
    
    #Creating help menu
    HelpMenu=Menu(MenuBar,tearoff=0)
    
    #Adding commands
    HelpMenu.add_command(label="About Notepad",command=about)
    
    MenuBar.add_cascade(label="Help",menu=HelpMenu)
    
    root.config(menu=MenuBar)
    
    #Adding scroll bar
    Scroll=Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)
    
    root.mainloop()