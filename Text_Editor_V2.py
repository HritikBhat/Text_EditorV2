from tkinter import Button, Label, Text, Entry, Tk
import tkinter as tk
from tkinter import ttk as tk1

""" This function is used to save or read a file and use text box as medium to
display content of the file."""
def __commit__(file, com,data=None, obj=None):
    global FILE,LIST
    if file not in LIST:
       LIST.append(file)
    fi_1 = open(file, com)
    if com == 'w':
        FILE = file
        global FONT, SIZE
        list1 = [FONT, SIZE]
        if ".txt" in FILE: 
            for line in list1:
                line = line.replace('\n', '')
                fi_1.write(line+"\n")
        fi_1.write(data.get("1.0", tk.END))                
    elif com == 'r':
        n=2
        data.delete('1.0', tk.END)
        FILE = file
        lines = fi_1.readlines()
        if ".txt" not in FILE :
            n=0
        for i in range(n, len(lines)):
            data.insert(tk.END, lines[i])

        if (data is not None) and (".txt" in FILE) :
            __setf__(lines[0], lines[1], data)
        else:
            __setf__("Arial","20",data)
    if obj is not None:
        obj.destroy()

#This function is to open a file and display through text box.
def __open__(data):
    open_wd = Tk()
    open_wd.geometry('400x150')
    open_wd.title("Open")

    lbl1 = Label(open_wd, text='Path:')
    lbl1.place(x=20, y=20)

    path= tk1.Combobox(open_wd,width=40)
    path['values'] =tuple(LIST)
    path.current()
    path.configure(font='Arial 10')
    path.place(x=60, y=20)

    lbl1 = Label(open_wd, text='Type:')
    lbl1.place(x=20, y=50)

    prtype = tk1.Combobox(open_wd, width=25)
    prtype['values'] = ('.txt', '.py', '.java', '.html')
    prtype.current(0)
    prtype.place(x=60, y=50)

    opbtn = Button(open_wd, text="Open", height=2, width=10, command=lambda: __commit__(path.get()+prtype.get(), "r",data, open_wd))
    opbtn.place(x=190, y=100)

    clbtn = Button(open_wd, text="Cancel", height=2, width=10, command=lambda: open_wd.destroy())
    clbtn.place(x=290, y=100)

#This Function is to save the current content of a file.
def __save__(data, svflg):
    global FILE,LIST
    #svflg is a Flag used to differentiate Save and SaveAs
    if FILE is not None and svflg is True:
        __commit__(FILE, "w",data)
    else:
        sav_wd = Tk()
        sav_wd.geometry('400x150')
        sav_wd.title("Save")

        # Takes addresss from user 
        lbl1 = Label(sav_wd, text='Path:')
        lbl1.place(x=20, y=20)
        path = tk1.Combobox(sav_wd,width=40)
        path['values'] = tuple(LIST)
        path.current()
        path.configure(font='Arial 10')
        path.place(x=60, y=20)

        # Takes extension of file from user
        lbl1 = Label(sav_wd, text='Type:')
        lbl1.place(x=20, y=50)
        prtype = tk1.Combobox(sav_wd, width=25)
        prtype['values'] = ('.txt', '.py', '.java', '.html')
        prtype.current(0)
        prtype.place(x=60, y=50)

        #Save Button to save
        savbtn = Button(sav_wd, text="Save", height=2, width=10, command=lambda: __commit__(path.get()+prtype.get(), "w",data,sav_wd))
        savbtn.place(x=190, y=100)

        clbtn = Button(sav_wd, text="Cancel", height=2, width=10, command=lambda: sav_wd.destroy())
        clbtn.place(x=290, y=100)

#This function sets the requested setting choice by the user.
def __setf__(font, size, data):
    global FONT, SIZE
    FONT = font
    SIZE = size

    if(size=='10' or size.strip()=='10'):
        data.configure(font=(font.strip(), size.strip()), width=100, height=80)
        
    elif(size=='20' or size.strip()=='20'):
        #print(size=='20')
        #print(size.strip()=='20')
        data.configure(font=(font.strip(), size.strip()), width=47, height=20)

    elif(size=='30' or size.strip()=='30'):
        data.configure(font=(font.strip(), size.strip()), width=32, height=15)

    elif(size=='40' or size.strip()=='40'):
        data.configure(font=(font.strip(), size.strip()), width=24, height=20)
        
    # For seeting Font and Size combobox to the user choice
    F.set(FONT)
    S.set(SIZE)
    
#The core window of this program.
def main(): 
    root = Tk()
    root.geometry('750x700')
    root.title("Text Editor")

    #Big Text Box
    data = Text(root, width=100, height=80)
    data.configure(font=(FONT, SIZE))
    data.place(x=40, y=130)

    #For the Font 
    lbl1 = Label(root, text='Font: ')
    lbl1.place(x=90, y=80)
    global S, F
    font = tk1.Combobox(root)
    F = font
    font['values'] = ('Arial', 'Algerian', 'Aharoni', 'Arial Black', 'Calibri', 'Impact')
    font.current(0)
    font.place(x=150, y=80)

    #For the Size
    lbl1 = Label(root, text='Size:')
    lbl1.place(x=370, y=80)
    size = tk1.Combobox(root)
    S = size
    size['values'] = ('10', '20', '30', '40', '50')
    size.current(0)
    size.place(x=440, y=80)

    #For save the changes of Font and Size
    setbtn = Button(root, text="Set", height=1, width=10, command=lambda: __setf__(font.get(), size.get(), data))
    setbtn.place(x=630, y=75)

    #For opening a new file
    openbtn = Button(root, text="Open", height=2, width=10, command=lambda: __open__(data))
    openbtn.place(x=220, y=10)

    #For saving a current file
    savebtn = Button(root, text="Save", height=2, width=10, command=lambda: __save__(data, True))
    savebtn.place(x=350, y=10)

    #For saving a current file under other filename
    saveas_btn = Button(root, text="Save As", height=2, width=10, command=lambda: __save__(data, False))
    saveas_btn.place(x=480, y=10)

    root.mainloop()
        
LIST = []
FILE = None
FONT = 'Arial'
SIZE = '10'
S = None
F = None

main()
