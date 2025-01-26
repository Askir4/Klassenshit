
import tkinter as tk
from tkinter import font


#Hier wird das Fenster definiert
root = tk.Tk()
root.geometry("250x150")
root.title="Taschenrechner"
root.configure(background='black')

#Hier wird das Standardfont festgelegt
font_cool = font.Font(size=20, family="Terminal")

#Hier werden die nötigen Befehle 
def delete(): 
 eingabe.delete(0,len(eingabe.get()) )

def show_result():
    result= eval(eingabe.get())
    eingabe.delete(0, tk.END)
    eingabe.insert(0, str(result))

#Hie werden die nötigen Buttons definiert
button_clear = tk.Button(root, text="clear",bg="grey", font=font_cool, command=delete)
button_ist_gleich = tk.Button(root, text="solve",bg="grey", font=font_cool, command=show_result)

#Hier wird das Eingabefenster definiert
eingabe = tk.Entry(root, font=font_cool, borderwidth=22, bg="grey")
eingabe.grid(row=0, column=0, columnspan=15)

button_clear.grid(row=1, column=0, sticky="nswe")
button_ist_gleich.grid(row=1, column=3, sticky="nswe")

#Damit es beim ändern der Fenstergröße nicht wie ein Paul (insider Discord) reagiert
for column in range (4):
  root.columnconfigure(column,weight=1)


for row in range (1):
  root.rowconfigure(row,weight=1 )




root.mainloop()
    