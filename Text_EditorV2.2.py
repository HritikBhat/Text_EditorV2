import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from tkinter import messagebox
import os
import tkinter.font


class Interface:
    def __init__(self):
        #Window Initialization
        self.filename=None
        self.face=tk.Tk()
        self.face.title("Untitled")
        self.face.geometry("700x700")
        #Menubar
        self.menubar = tk.Menu(self.face)
        #File Option!
        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="Open", command=self.Open, accelerator="Ctrl+O")
        filemenu.add_command(label="Save", command=self.Save, accelerator="Ctrl+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.Quit, accelerator="Ctrl+Q")
        self.menubar.add_cascade(label="File", menu=filemenu)
        #Edit Option!
        editmenu = tk.Menu(self.menubar, tearoff=0)
        editmenu.add_command(label="Font", command=self.Font)
        self.menubar.add_cascade(label="Edit", menu=editmenu)
        self.face.config(menu=self.menubar)
        #Short-Cut Keys For Commands Like Save,Open,Exit.
        self.face.bind_all('<Control-Key-o>', self.Open)
        self.face.bind_all('<Control-Key-s>', self.Save)
        self.face.bind_all('<Control-Key-q>', self.Quit)
        #Frame for Text and Scroll_Bar
        self.frame = tk.Frame(self.face)
        self.frame.pack(fill=tk.BOTH, expand=1)
        #Scroll_Bar
        self.scrollbar = tk.Scrollbar(self.frame,orient=tk.VERTICAL)
        self.scrollbar.pack( side=tk.RIGHT, fill = tk.Y )
        #Text_Box
        self.text = tk.Text(self.frame)
        self.text.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        #Setting scrollbar to textbox
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.text.yview)
        self.face.protocol("WM_DELETE_WINDOW", self.Quit)
        self.face.mainloop()

    def Save(self,event=None):
        def done():
            try:
                f1=open(self.filename, "w")
                f1.write(self.text.get("1.0", tk.END))
                f1.close()
                self.face.title(self.filename)
            except FileNotFoundError:
                pass

        if self.filename is None:   
            self.filename = filedialog.asksaveasfilename(initialdir="C:/Users/Hritik/Desktop/Java_Comp/Bin/Projects/", title="Select file", filetypes=[("all files", "*.*")])
        done()

    def Open(self,event=None):
        def done():
            self.face.title(self.filename)
            f1=open(self.filename, "r")
            list_ln = f1.readlines()
            self.text.delete("1.0", tk.END)
            for line in list_ln:
                self.text.insert(tk.END, line)
            f1.close()
            
        self.filename = filedialog.askopenfilename(initialdir="C:/Users/Hritik/Desktop/Java_Comp/Bin/Projects/", title="Select file", filetypes=[("all files", "*.*")])
        done()

    def Font(self):
        self.font = tk.Toplevel()
        self.font.title("Font")
        self.font.geometry("390x470")
        
        font_lst = list(sorted(tkinter.font.families()))

        font_label=tk.Label(self.font,text="Font:")
        font_label.place(x=10,y=20)
        

    def Quit(self,event=None):
        if self.filename is None and self.text.get("1.0", tk.END) != '\n':
                MsgBox = tk.messagebox.askquestion ('Exit Application', 'Do you want to save changes to Untitled?', icon='warning')
                if MsgBox == 'yes':
                    self.Save()
                else:
                    self.face.destroy()

        else:
            self.face.destroy()
        
it = Interface()

