import tkinter as tk
import tkinter.messagebox as ttk
import random

def make_maze(yoko, tate):
    XP = [ 0, 1, 0, -1]
    YP = [-1, 0, 1,  0]

    maze_lst = []
    for y in range(tate):
        maze_lst.append([0]*yoko)
    for x in range(yoko):
        maze_lst[0][x] = 1
        maze_lst[tate-1][x] = 1
    for y in range(1, tate-1):
        maze_lst[y][0] = 1
        maze_lst[y][yoko-1] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            maze_lst[y][x] = 1
    for y in range(2, tate-2, 2):
        for x in range(2, yoko-2, 2):
            if x > 2: rnd = random.randint(0, 2)
            else:     rnd = random.randint(0, 3)
            maze_lst[y+YP[rnd]][x+XP[rnd]] = 1

    return maze_lst
    
def show_maze(canvas, maze_lst):
    color = ["white", "gray"]
    for y in range(len(maze_lst)):
        for x in range(len(maze_lst[y])):
            canvas.create_rectangle(x*100, y*100, x*100+100, y*100+100, 
                                    fill=color[maze_lst[y][x]])

def key_down(event):
    global key
    key = event.keysym
    #print(f"[{key}]Clicked")

def key_up(event):
    global key
    key = " "

def main_proc():
    global cx, cy, key, mx, my
    delta = { " ":[0,0],
            "Up":[0,-1],
             "Down":[0,+1], 
             "Left":[-1,0], 
             "Right":[+1,0],
            
    }

    try:
        if maze_bg[my+delta[key][1]][mx+delta[key][0]]==0:
            my,mx = my+delta[key][1],mx+delta[key][0]
    except:
        pass
    #mx,my = mx + delta[key][0], my + delta[key][1]
    cx = mx*100+50
    cy = my*100+50

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

    maze_bg = make_maze(15,9) 
    # print(maze_bg)
    show_maze(canvas, maze_bg)
    tori = tk.PhotoImage(file="fig/5.png")
    mx = 1
    my = 1
    cx = mx*100+50
    cy = my*100+50
    canvas.create_image(cx, cy, image=tori, tag="tori")
    
    key=" "
    root.bind("<KeyPress>",key_down)
    root.bind("<KeyRelease>",key_up)    
    
    main_proc()
    root.mainloop()