import tkinter as tk
import tkinter.messagebox as ttk


if __name__ ==  '__main__':
    root = tk.Tk()
    root.title("迷宫")
    canvas = tk.Canvas(root, 
                       width = 1500, 
                       height = 900, 
                       bg = "black",
                       )
    canvas.pack()
    tori = tk.PhotoImage(file="fig/5.png")
    cx = 300
    cy = 400
    canvas.create_image(cx, cy, image=tori, tag="tori")
    
    root.mainloop()