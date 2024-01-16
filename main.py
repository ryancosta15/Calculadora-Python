import tkinter as tk
from tkinter import *
#tela
window = tk.Tk() #construindo tela
window.title("calculadora")
window.geometry = (1000,1000) #tamanho da tela como tupla


base = tk.Frame(window, width = 1000,height = 1000, pady=5)
base.grid(row = 0,column = 0)
base.config(bg="#3c3c3c")

current = 0
font_current = ("Verdana",10,"bold")

#label
label = tk.Label(base,width=20, height=2)
label.config(bg = "darkgreen")
label.config(text = current)
label.grid(row = 0,column = 0)
label.config(font = font_current)

#pad
pad = tk.Frame(base, width=300, height=300,pady=5, padx=10)
pad.config(bg = "#515151")
pad.grid(row=1, column=0)


# selecting number
def selectnumber(number):
    if label["text"] == 0:
        label.config(text = number)
        x = number
    else:
        y = str(label["text"]) + str(number)
        label.config(text=y)
        x = int(y)
    return x


#botões
btn7 = tk.Button(pad, text = "7",command = lambda: selectnumber(7),padx=10,pady=5)
btn7.grid(row=0, column=0)
btn8 = tk.Button(pad, text = "8",command = lambda: selectnumber(8),padx=10,pady=5)
btn8.grid(row=0, column=1)
btn9 = tk.Button(pad, text = "9",command = lambda: selectnumber(9),padx=10,pady=5)
btn9.grid(row=0, column=2)

btn4 = tk.Button(pad, text = "4",command = lambda: selectnumber(4),padx=10,pady=5)
btn4.grid(row=1, column=0)
btn5 = tk.Button(pad, text = "5",command = lambda: selectnumber(5),padx=10,pady=5)
btn5.grid(row=1, column=1)
btn6 = tk.Button(pad, text = "6",command = lambda: selectnumber(6),padx=10,pady=5)
btn6.grid(row=1, column=2)

btn1 = tk.Button(pad, text = "1",command = lambda: selectnumber(1),padx=10,pady=5)
btn1.grid(row=2, column=0)
btn2 = tk.Button(pad, text = "2",command = lambda: selectnumber(2),padx=10,pady=5)
btn2.grid(row=2, column=1)
btn3 = tk.Button(pad, text = "3",command = lambda: selectnumber(3),padx=10,pady=5)
btn3.grid(row=2, column=2)



window.mainloop() #deixa a interface de tela