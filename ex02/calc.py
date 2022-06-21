from calendar import c
import tkinter as tk
import tkinter.messagebox as tkm

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    # tkm.showwarning("確認", 
    #                  f"you clicked on {txt} button.")
    if txt == "=":
        keisan = entry.get() 
        result = eval(keisan) 
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    else:
        entry.insert(tk.END, txt)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")
    root.geometry("295x570")

    entry = tk.Entry(root, justify="right", width = 10, font=("Times New Roman",40))
    entry.grid(row = 0, column= 0, columnspan=3)

    r, c = 40, 0
    for i,num in enumerate([i for i in range(9,-1,-1)]+["+","="]):
        button = tk.Button(root,
                    width= 4, 
                    height=2, 
                    font=("Times New Roman", 30),
                    text=f"{num}"
                    )
        button.grid(row=r, column=c)
        c += 1
        if (i+1) % 3 == 0:
            r += 1
            c = 0  
        button.bind("<1>", button_click)
        

    root.mainloop()
