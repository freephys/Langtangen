#!/usr/bin/env python
from Tkinter import *
import math

root = Tk()              # root (main) window
top = Frame(root)        # create frame
top.pack(side='top')     # pack frame in main window

hwtext = Label(top, text='Hello, World! The sine of')
hwtext.pack(side='top')

r = StringVar() # variable to be attached to r_entry
r.set('1.2')    # default value
r_entry = Entry(top, width=6, textvariable=r)
r_entry.pack(side='top')

s = StringVar() # variable to be attached to s_label
def comp_s(event):
    global s
    s.set('%g' % math.sin(float(r.get()))) # construct string

r_entry.bind('<Return>', comp_s)

compute = Label(top, text=' equals ')
compute.pack(side='top')

s_label = Label(top, textvariable=s, width=18)
s_label.pack(side='top')

import tkMessageBox
def quit(event):
    if tkMessageBox.askokcancel('Quit','Do you really want to quit?'):
        root.destroy()

root.bind('<q>', quit)

root.mainloop()
