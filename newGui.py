from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
import PIL
from PIL import Image
from PIL import ImageTk

from app import *

root = Tk()
l = 520
w = 775
root.geometry(str(w) + "x" + str(l))
root.title("PadScraper")
root.resizable(0,0)

def updateLogs(msg):
    logs.configure(state="normal")
    logs.insert("end-1c", msg)
    logs.update()
    logs.see(END)
    logs.configure(state="disabled")

def pasteClipboard():
    link.delete(0, END)
    link.insert(0, root.clipboard_get())
    link.update()

def pbStep(x):
    pbBar['value'] += int(100/x)

def initDownload():
    try:
        logs.delete("1.0", END)
        pbBar['value'] = 0
        story_url = link.get()
        updateLogs("Downloading: " + story_url + "\n")
        writeTxt(initScrape(storyMeta(story_url)[0]))
        pbBar['value'] = 100
        myLabel3.configure(text="Progress: [Download Complete]")
        myLabel3.update()
        updateLogs("PadScraper [Download Complete]\n")
    except Exception as e:
        updateLogs("An error occured: " + e)

#Elements
myLabel = Label(root, text="Story Link: ", anchor="w")
myLabel2 = Label(root, text="Logs/Errors: ", anchor="w")
myLabel3 = Label(root, text="      Progress", anchor="w")
downloadBtn = Button(root, text="Download & Export as TXT", command=initDownload)
pasteBtn = Button(root, text="PASTE", height=0, command=pasteClipboard)
programDesc = Label(root, borderwidth=1, width=40, relief="solid" ,text="PadScraper - WattPad Download Tool\nAuthor: Journel Cabrillos\nEmail: journelcabrillos@protonmail.com")
myImg = ImageTk.PhotoImage(Image.open("wattpad.png"))
imgLogo = Label(root, image=myImg)
link = Entry(root, width=70)
separator = ttk.Separator(root).place(x=0, y=240, relwidth=1)
logs = ScrolledText(root, width=70, height=10, state="disabled")

pbBar = ttk.Progressbar(root, orient=HORIZONTAL, length=500, mode='determinate')

#Grid System
myLabel.grid(row=3, column=0, pady=20, padx=10)
link.grid(row=3, column=1, pady=20)
pasteBtn.grid(row=3, column=2, padx=10)

programDesc.grid(row=2, column=1)
imgLogo.grid(row=1,column=1, padx=20, pady=5)
downloadBtn.grid(row=4, column=1)
myLabel2.grid(row=5, column=1,padx=10,pady=20)
logs.grid(row=6,column=1,sticky=("N", "S", "E", "W"))
pbBar.grid(row=8,column=1, pady=0)
myLabel3.grid(row=7, column=1, pady=5)
root.mainloop()
