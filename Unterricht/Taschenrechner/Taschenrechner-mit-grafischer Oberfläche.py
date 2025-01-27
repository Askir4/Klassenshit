
import tkinter as tk
from tkinter import font
import webbrowser
#Hier wird das Fenster definiert
root = tk.Tk()
root.geometry("500x500")
root.configure(background='black')


font_cool = font.Font(size=20, family="Terminal")

def addChar(char):
 eingabe.insert(len(eingabe.get()), char)

def clear_entry():
 eingabe.delete(0,len(eingabe.get()) )

def show_result():
    result= eval(eingabe.get())
    eingabe.delete(0, tk.END)
    eingabe.insert(0, str(result))

def git_link():
  webbrowser.open("https://github.com/Askir4/Klassenshit") 


#Hier wird das Eingabefenster erstellt
eingabe = tk.Entry(root, font=font_cool, borderwidth=20,bg="grey")
eingabe.grid(row=0, column=0, columnspan=4)

#Hier werden die Buttons definiert
button1 = tk.Button(root, text="1", font=font_cool, command=lambda: addChar('1'), bg="grey")
button2 = tk.Button(root, text="2", font=font_cool, command=lambda: addChar('2'), bg="grey")
button3=  tk.Button(root, text="3", font=font_cool, command=lambda: addChar('3'), bg="grey")
button4=  tk.Button(root, text="4", font=font_cool, command=lambda: addChar('4'), bg="grey")
button5=  tk.Button(root, text="5", font=font_cool, command=lambda: addChar('5'), bg="grey")
button6=  tk.Button(root, text="6", font=font_cool, command=lambda: addChar('6'), bg="grey")
button7=  tk.Button(root, text="7", font=font_cool, command=lambda: addChar('7'), bg="grey")
button8=  tk.Button(root, text="8", font=font_cool, command=lambda: addChar('8'), bg="grey")

button9=  tk.Button(root, text="9", font=font_cool, command=lambda: addChar('9'), bg="grey")
button0=  tk.Button(root, text="0", font=font_cool, command=lambda: addChar('0'), bg="grey")

button_plus = tk.Button(root, text="+", font=font_cool, command=lambda: addChar('+'), bg="grey")
button_minus = tk.Button(root, text="-", font=font_cool, command=lambda: addChar('-'), bg="grey")
button_geteilt = tk.Button(root, text="/", font=font_cool, command=lambda: addChar('/'), bg="grey")
button_mal = tk.Button(root, text="*", font=font_cool, command=lambda: addChar('*'), bg="grey")
button_ist_gleich = tk.Button(root, text="=", font=font_cool, command=show_result, bg="grey")
button_kommastelle = tk.Button(root, text=".", font=font_cool, command=lambda: addChar("."), bg="grey" )
button_clear = tk.Button(root, text="Nuke Them", font=font_cool, command=clear_entry, bg="grey")
butto_repo = tk.Button(root, text="Repo", font=font_cool, command=git_link, bg="grey")

#Hier werden die Buttons in das oben erstellte Fenster "eingebaut"
button7.grid(row=1, column=0, sticky="nswe")
button8.grid(row=1, column=1, sticky="nswe")
button9.grid(row=1, column=2, sticky="nswe")
button_clear.grid(row=1, column=3, sticky="nswe")
button4.grid(row=2, column=0, sticky="nswe")
button5.grid(row=2, column=1, sticky="nswe")
button6.grid(row=2, column=2, sticky="nswe")
button_minus.grid(row=2, column=3, sticky="nswe")
button1.grid(row=3, column=0, sticky="nswe")
button2.grid(row=3, column=1, sticky="nswe")
button3.grid(row=3, column=2, sticky="nswe")
button_plus.grid(row=3, column=3, sticky="nswe")
button_mal.grid(row=4, column=0, sticky="nswe")
button0.grid(row=4, column=1, sticky="nswe")
button_geteilt.grid(row=4, column=2, sticky="nswe")
button_ist_gleich.grid(row=4, column=3, sticky="nswe")
button_kommastelle.grid(row=5, column=2, sticky="nswe")
butto_repo.grid(row=5, column=0, sticky="nswe")

for column in range (4):
  root.columnconfigure(column,weight=1)


for row in range (4):
  root.rowconfigure(row,weight=1 )


root.mainloop()
