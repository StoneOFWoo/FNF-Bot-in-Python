import customtkinter
import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename

import json
import os

def openFile():
    filepath = askopenfilename(title="Choose your config file",filetypes=(("JSON File", "*.json"),))

    with open('source/user/user_saves.json', 'r+') as openfile:
        json_object = json.load(openfile)
        json_object['lastConfig'] = filepath

        openfile.seek(0)
        json.dump(json_object, openfile)
        openfile.truncate()

def startBot():
    os.system('python source/script.py')
        


# CREATE WINDOW
customtkinter.set_appearance_mode('system')
customtkinter.set_default_color_theme('dark-blue')


app = customtkinter.CTk()
app.geometry('400x400')

# BUTTON
select = customtkinter.CTkButton(master=app, text="Open Config File", command=openFile)
select.place(relx= 0.5, rely=0.4, anchor=tkinter.CENTER)

start = customtkinter.CTkButton(master=app, text="Start", command=startBot)
start.place(relx= 0.5, rely=0.55, anchor=tkinter.CENTER)

# TEXT
bigtext = customtkinter.CTkLabel(master=app, text="FNF BOT", font=('Roboto bold', 45))
bigtext.pack(padx= 0, pady=70)



app.mainloop()
