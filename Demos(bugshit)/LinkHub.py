
import tkinter as tk
from tkinter import font
import webbrowser
#Hier wird das Fenster definiert
root = tk.Tk()
root.geometry("450x450")
root.configure(background='black')

font_cool = font.Font(size=20, family="Terminal")"


def git_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit")


def utm_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit")


def ticket_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit")



def Hutm_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit")



def unifi_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit")


  
  
button_repo = tk.Button(root, text="Repo", font=font_cool, command=git_link, bg="grey")
button_Iutm = tk.Button(root, text="Iutm", font=font_cool, command=utm_link, bg="grey" )
button_Processes = tk.Button(root, text="Tickets", font=font_cool, command=ticket_link, bg="grey")
button_Hutm = tk.Button(root, text="Hutm", font=font_cool, command=utm_link, bg="grey")
button_unifi = tk.Button(root, text="Unifi", font=font_cool, command=unifi_link, bg="grey")



button_repo.grid(row=0, column=0, sticky="nswe")
button_Iutm.grid(row=0, column=1, sticky="nswe")
button_Processes.grid(row=0, column=2, sticky="nswe")
button_unifi.grid(row=2, column=0, sticky="nswe")
button_Hutm.grid(row=2, column=1, sticky="nswe")




for column in range (4):
  root.columnconfigure(column,weight=1)


for row in range (4):
  root.rowconfigure(row,weight=1 )
















root.mainloop()
