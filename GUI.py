def clear():
    entryTxt.set("")

def Go():
    if choiceOCR.get() == "TesseractOCRTra":
        print("TesseractOCRTra")
        text = Tchange(entryTxt.get(), "chi_tra")
        PrintText.insert(tk.INSERT, text)
        PrintText.insert(tk.END, "\n")
    elif choiceOCR.get() == "TesseractOCRSim":
        print("TesseractOCRSim")
        text = Tchange(entryTxt.get(), "chi_sim")
        PrintText.insert(tk.INSERT, text)
        PrintText.insert(tk.END, "\n")
    elif choiceOCR.get() == "GoogleOCR":
        print("GoogleOCR")
        main(entryTxt.get())
        text = read("./out.txt")
        PrintText.insert(tk.INSERT, text)
        PrintText.insert(tk.END, "\n")

import tkinter as tk
from PictureToTxt import Tchange
from GoogleOCR import main
from File_control import read

gui = tk.Tk()
gui.title("Sheng")

choiceOCR = tk.StringVar()
choice1 = tk.Radiobutton(gui, text = "TesseractOCR 陳家靖", value = "TesseractOCRTra", variable = choiceOCR)
choice2 = tk.Radiobutton(gui, text = "TesseractOCR 陈家靖", value = "TesseractOCRSim", variable = choiceOCR)
choice3 = tk.Radiobutton(gui, text = "GoogleOCR", value = "GoogleOCR", variable = choiceOCR)

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
