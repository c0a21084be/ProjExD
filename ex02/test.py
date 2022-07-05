print("hello world")

from distutils.dir_util import create_tree
import tkinter as tk
from venv import create
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showwarning(txt, 
                     f"[{txt}]you clicked on this button.")
    # tkm.showwarning("Error", 
    #                  "This is an error message\nYou clicked the button that doesn't open the image."
    #                  )
root = tk.Tk()
root.title("おためしか")
root.geometry("500x200")

lable = tk.Label(root,
                 text="らべるを書いてみたい件", 
                 font=("Ricty Dimirished",20)
                 )
lable.pack()

button = tk.Button(root, text="押すな", command=button_click)
button.bind("<1>",button_click)
button.pack()

# create_image(x,y,image=PhotoUmage)
# create_line(x, y, fill=color, outline=color, width=?)
# create_rectangle(x,y,fill=color, outline=color, width=?)
# create_oval(x, y, fill=color, outline=color, width=?)
# create_polygon(x, y, fill=color, outline=color, width=?)

entry = tk.Entry(width=30)
entry.insert(tk.END,"fugapiyo")
entry.pack()


    

root.mainloop()
