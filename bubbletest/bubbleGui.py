def clear():
    entryTxt.set("")

def Go():
    print("null")

import tkinter as tk

gui = tk.Tk()
gui.title("Sheng")

frame1 = tk.Frame(gui)
label = tk.Label(frame1, text = "Picture Address:")
entryTxt = tk.StringVar()
entry = tk.Entry(frame1, textvariable = entryTxt)
label.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

frame2 = tk.Frame(gui)
button2 = tk.Button(frame2, text = "GO", command = Go)
button2.grid(row = 0, column = 1)

PrintText = tk.Text(gui)

frame1.pack()
frame2.pack()
PrintText.pack()
gui.mainloop()
