import imp
import tkinter as tk
import tkinter.messagebox as ttk
import maze_maker as mm


def key_down(event):
    global key
    key = event.keysym
    #print(f"[{key}]Clicked")

def key_up(event):
    global key
    key = " "

def main_proc():
    global cx,cy,key
    delta = { " ":[0,0],
            "Up":[0,-20],
             "Down":[0,+20], 
             "Left":[-20,0], 
             "Right":[+20,0],
            
    }
    cx,cy = cx + delta[key][0], cy + delta[key][1]
    canvas.coords("tori",cx,cy)
    root.after(100,main_proc)

if __name__ ==  '__main__':
    root = tk.Tk()
    root.title("迷宫")
    canvas = tk.Canvas(root, 
                       width = 1500, 
                       height = 900, 
                       bg = "black",
                       )
    canvas.pack()

    maze_bg = mm.make_maze(15,9) 
    print(maze_bg)
    mm.show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/5.png")
    cx = 300
    cy = 400
    canvas.create_image(cx, cy, image=tori, tag="tori")
    
    key=" "
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)    
    
    main_proc()
    root.mainloop()