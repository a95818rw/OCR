def clear():
    entryTxt.set("")

def Go():
    PrintText.insert(tk.INSERT, text)
    PrintText.insert(tk.END, "\n")

import tkinter as tk
from PictureToTxt import text

gui = tk.Tk()

frame1 = tk.Frame(gui)
label = tk.Label(frame1, text = "Picture Location:")
entryTxt = tk.StringVar()
entry = tk.Entry(frame1, textvariable = entryTxt)
label.grid(row=0, column=0)
entry.grid(row=0, column=1)

frame2 = tk.Frame(gui)
button1 = tk.Button(frame2, text="clear", command=clear)
button2 = tk.Button(frame2, text="GO", command=Go)
button1.grid(row=0, column=0)
button2.grid(row=0, column=1)

PrintText = tk.Text(gui)

frame1.pack()
frame2.pack()
PrintText.pack()
gui.mainloop()