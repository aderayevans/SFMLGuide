# -*- coding: utf8 -*-
import tkinter as tk
from tkinter import filedialog
import os


class MainWindow(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        tk.Frame.__init__(self)
        self.label = tk.Label(self, text="Link to your project main file: "
                              , font=("Times New Roman", 13))
        self.label.grid(column=0, row=0)
        self.link_text = tk.Entry(self, width=50)  #
        self.link_text.grid(column=0, row=1)
        self.file_button = tk.Button(self, text="Browse", command=self.browse)
        self.file_button.grid(column=1, row=1)
        self.compile_button = tk.Button(self, text="Compile", command=self.compile)
        self.compile_button.grid(column=1, row=2)
        self.default_val = tk.IntVar()
        self.default_check = tk.Checkbutton(self, text="CurrentDirectory (main.cpp)"
                                         , variable=self.default_val, onvalue=1
                                         , offvalue=0, height=1, width=20)
        self.default_check.grid(column=0, row=2)
        self.label['background']=background_color
        self.compile_button['background']=background_color
        self.default_check['background']=background_color

    def set_link(self, text):
        self.link_text.delete(0, tk.END)
        self.link_text.insert(tk.INSERT, text)

    def get_link(self):
        while True:
            try:
                if self.link_text.get() == '':
                    raise ValueError('Value Error')
                linktext = self.link_text.get()
                break
            except ValueError:
                ErrorMessage('13', 0)
                raise
        return linktext

    def check_file(self):
        if self.file_val.get() == 0:
            self.set_cipher(hashing(self.parent.get_func(), self.get_plain().encode()))
        else:
            while True:
                try:
                    with open(self.get_link(), 'rb') as fo:
                        content = fo.read()
                    break
                except FileNotFoundError:
                    ErrorMessage('14', 0)
                    raise
            self.set_cipher(hashing(self.parent.get_func(), content))

    def compile(self):
        if self.default_val.get() == 0:
            link = self.get_link()
        else:
            link = os.getcwd() + '/main.cpp'
        head, tail = os.path.splitext(link)
        outputfile = head + '.o'
        exe_file = head + '.exe'
        command01 = 'g++ -c ' + link + ' -o ' + outputfile + ' -I D:/Programs/SFML/include -g -m64 -Wall && g++ ' + outputfile + ' -o ' + exe_file + ' -L D://Programs//SFML//lib -lsfml-audio -lsfml-graphics -lsfml-system -lsfml-network -lsfml-window'
        command02 = 'g++ -c ' + link + ' -o ' + outputfile + ' -I D://Programs//SFML//include -O3 -m64 && g++ ' + outputfile + ' -o ' + exe_file + ' -L D://Programs//SFML//lib -lsfml-audio -lsfml-graphics -lsfml-system -lsfml-network -lsfml-window -mwindows'
        command03 = 'START "path" ' + exe_file
	
        os.system(command01)
        os.system(command02)
        os.system(command03)

    def browse(self):
        self.set_link(browse_file())
        

def browse_file():
    return tk.filedialog.askopenfilename(initialdir="D:/",
                                         title="Open", filetypes=(("All files", "*.*"),
                                                                ("C++ files", "*.cpp"))
                                         )


def main():
    root.title("My compiler")
    root.geometry('500x100')
    root['background']=background_color
    main = MainWindow(root)
    main.pack()
    main['background']=background_color
    root.mainloop()


if __name__ == '__main__':
    global background_color
    global root
    background_color = '#cedbd2'
    root = tk.Tk()
    main()
