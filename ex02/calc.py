from calendar import c
import tkinter as tk
import tkinter.messagebox as tkm
import math
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
    
    elif txt == "C":
        entry.delete(0, tk.END) 
    
    elif txt == "Del":
        n = len(entry.get())-1
        entry.delete(n,tk.END)
    
    elif txt == "sqrt(x)":
        keisan = entry.get() 
        result = math.sqrt(int(keisan)) 
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)

    elif txt == "X^2":
        num = entry.get()
        result=int(num)*int(num)
        entry.delete(0, tk.END)   
        entry.insert(tk.END, result)

    elif txt == "+/-":
         num = entry.get()
         num1 = int(num)*-1
         entry.delete(0, tk.END)
         entry.insert(tk.END, num1)
    elif txt == "1/x":
         num = entry.get()
         num1 = 1/int(num)
         entry.delete(0, tk.END)
         entry.insert(tk.END, num1)
    elif txt == "%":
         num = entry.get()
         num1 = int(num)/100
         entry.delete(0, tk.END)
         entry.insert(tk.END, num1)
    else:
        entry.insert(tk.END, txt)
    

if __name__ == "__main__":
    root = tk.Tk()
    root.title("電卓")

    entry = tk.Entry(root, justify="right", width = 18, font=("Times New Roman",40))
    entry.grid(row = 0, column= 0, columnspan=4)

    r, c = 40, 0
    for i,num in enumerate(["Del","%","C","Del","1/x","X^2","sqrt(x)","/",7,8,9,"*",4,5,6,"-",1,2,3,"+","+/-",0,",","="]):
        button = tk.Button(root,
                    width= 5, 
                    height=2, 
                    font=("Times New Roman", 30),
                    text=f"{num}"
                    )
        button.grid(row=r, column=c)
        c += 1
        if (i+1) % 4 == 0:
            r += 1
            c = 0  
        button.bind("<1>", button_click)
        
        if num == "=":
           button["bg"] = "PaleVioletRed1"

    root.mainloop()
