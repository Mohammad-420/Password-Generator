#!/usr/bin/python3.7.5
__author__ = "Mohammad Askari"

import random
import string
from tkinter import *

generate = ""


def generator():
    global generate
    generate = ""
    password = lower.get() + upper.get() + number.get()
    for i in range(int(length.get())):
        generate += random.choice(password)
    show.set(generate)


if __name__ == "__main__":
    gui = Tk()
    gui.title('pass generator')
    gui.geometry('310x60+750+500')

    length = StringVar()
    show = StringVar()
    lower = StringVar()
    upper = StringVar()
    number = StringVar()

    lower_ = string.ascii_lowercase
    upper_ = string.ascii_uppercase
    number_ = string.digits

    chkbtnlow = Checkbutton(gui, text="Lower", width=7, variable=lower, onvalue=lower_, offvalue="").grid(row=0,
                                                                                                              column=1)
    chkbtnup = Checkbutton(gui, text="Upper", width=7, variable=upper, onvalue=upper_, offvalue="").grid(row=0,
                                                                                                             column=2)
    chkbtnnum = Checkbutton(gui, text="Number", width=7, variable=number, onvalue=number_, offvalue="").grid(row=0,
                                                                                                                 column=3)
    spinbox = Spinbox(gui, from_=4, to=15, textvariable=length, width=7).grid(row=0, column=0)
    btn = Button(gui, text="generate", command=generator).grid(row=1, column=0)
    entr = Entry(gui, textvariable=show, width=27).grid(row=1, column=1, columnspan=3)

    gui.mainloop()
