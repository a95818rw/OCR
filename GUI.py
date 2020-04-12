def clear():
    entryTxt.set("")

def Go():
    if choiceOCR.get() == "TEng":
        text = Tchange(entryTxt.get())
        PrintText.insert(tk.INSERT, text)
        PrintText.insert(tk.END, "\n")
    elif choiceOCR.get() == "GEng":
        print("GEhg")
    elif choiceOCR.get() == "GChi":
        print("Gchi")

import tkinter as tk
from PictureToTxt import Tchange
gui = tk.Tk()
gui.title("Sheng")

choiceOCR = tk.StringVar()
choice1 = tk.Radiobutton(gui, text = "TesseractOCR English", value = "TEng", variable = choiceOCR)
choice2 = tk.Radiobutton(gui, text = "GoogleOCR English", value = "GEng", variable = choiceOCR)
choice3 = tk.Radiobutton(gui, text = "GoogleOCR Chinese", value = "GChi", variable = choiceOCR)

frame1 = tk.Frame(gui)
label = tk.Label(frame1, text = "Picture Address:")
entryTxt = tk.StringVar()
entry = tk.Entry(frame1, textvariable = entryTxt)
label.grid(row = 0, column = 0)
entry.grid(row = 0, column = 1)

frame2 = tk.Frame(gui)
button1 = tk.Button(frame2, text = "clear", command = clear)
button2 = tk.Button(frame2, text = "GO", command = Go)
button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)

PrintText = tk.Text(gui)

frame1.pack()
choice1.pack()
choice2.pack()
choice3.pack()
frame2.pack()
PrintText.pack()
gui.mainloop()