# %%
from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


root = Tk()

root.wm_iconbitmap('NotepadIcon.ico')  

def dark():
    text['bg']='gray25'
    text['insertbackground']='white'
    text['fg']='snow2'
    
def light():
    text['bg']='white'
    text['insertbackground']='black'
    text['fg']='black'
    
    
def create():
    global file
    root.title("Untitled - Notepad")
    text.delete(0.0,'end')
    file = None
    
def openfile():
    global file
    file = askopenfilename(defaultextension =".txt", filetype = [("All Files", "*.*"),('Text Doxuments',"*.txt")])
    
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        text.delete(0.0, 'end')
        f = open(file, 'r')
        text.insert(0.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension = '.txt', filetypes = [('Alll Files',"*.*"),('Text Documents','*.txt')])
    
        if file == "":
            file = None

        else:
            f = open(file, "w")
            f.write(text.get(0.0,'end'))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
            
    else:
        f = open(file, 'w')
        f.write(text.get(0.0,'end'))
        f.close()

def about():
    tmsg.showinfo('About', " Welcome to Swarn's Notepad")
    
def exit():
    root.destroy()
    
def cut():
    text.event_generate(("<<Cut>>"))
    
def copy():
    text.event_generate(("<<Copy>>"))
    
def paste():
    text.event_generate(("<<Paste>>"))
    
def bold():
    string = text['font']
    if 'bold' in string:
        string = string.replace('bold','').strip()
    else:
        string += ' bold'
    text['font'] = string

def italic():
    string = text['font']
    if 'italic' in string:
        string = string.replace('italic','').strip()
    else:
        string += ' italic'
    text['font'] = string
    print(string)
    

def size():
    
    def changesize():
        if textsize.get() < 0 or textsize.get() > 100:
            tmsg.showinfo('Warning','Enter a valid size (0 - 100)')
        else:
            string = []
            string = text['font'].split(' ')
            newstring = ''
            for i in string:
                if i.isnumeric():
                    newstring += str(textsize.get())+' '
                else:
                    newstring += i +' '
            newstring = newstring.strip()
            text['font'] = newstring
        frame.destroy()
    
    textsize = IntVar()
    frame = Frame(text, bg = 'gray')
    frame.pack(pady=40)
    entry = Entry(frame, textvariable = textsize)
    entry.pack()
    b1 = Button(frame, text='OK', command = changesize)
    b1.pack()
            
    
root.geometry('800x600')

file = None

if file == None:
    root.title('Untitled - Notepad')

# Adding Scrollbar & Text Box
scrollbar = Scrollbar(root)
scrollbar.pack(side = 'right',fill='y')


text = Text(root, bg='gray25', insertbackground='white', fg='snow2',yscrollcommand = scrollbar.set, font =('Times',24,'bold','italic'))  #'Times 24 bold italic'
text.pack(fill='both', expand='true')

scrollbar.config(command=text.yview)

mainmenu = Menu(root)

filemenu = Menu(mainmenu, tearoff = 0)
filemenu.add_command(label = "New", command = create)
filemenu.add_command(label = "Open", command = openfile)
filemenu.add_command(label = "Save", command = save)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit)
mainmenu.add_cascade(label = 'File', menu = filemenu)

editmenu = Menu(mainmenu, tearoff=0)
editmenu.add_command(label = 'Cut', command = cut)
editmenu.add_command(label = 'Copy', command = copy)
editmenu.add_command(label = 'Paste', command = paste)
mainmenu.add_cascade(label='Edit', menu = editmenu)

fontmenu = Menu(editmenu, tearoff = 0)
fontmenu.add_command(label = 'Bold', command = bold)
fontmenu.add_command(label = 'Italic', command = italic)
fontmenu.add_command(label = 'Size', command = size)

editmenu.add_cascade(label = "Font", menu = fontmenu)

thememenu = Menu(mainmenu, tearoff=0)
thememenu.add_command(label = 'Light', command = light)
thememenu.add_command(label = 'Dark', command = dark)
mainmenu.add_cascade(label='Theme', menu = thememenu)


mainmenu.add_command(label='About', command = about)

root.config(menu = mainmenu)



root.mainloop()

# %%
