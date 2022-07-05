import tkinter as tk
import tkinter.messagebox as  tkm

#リアルタイム処理
def count_up():                
    global tmr, jid
    tmr += 1
    label["text"] = tmr
    jid = root.after(1000, count_up)

#ボタンクリック、イベント
# def button_click(event):                   
#     btn = event.widget
#     txt = btn["text"]
#     tkm.showinfo(txt,f"{txt}キーが押されました") 

#キー入力
def key_down(event):
    global jid                    
    if jid != None:
        root.after_cancel(jid)
        jid = None
        return
    key = event.keysym
    tkm.showinfo("キー押下",f"{key}キーが押されました")
    jid = root.after(1000,count_up)

if __name__ == '__main__':  
    root = tk.Tk()
    label = tk.Label(root,
                     font=("Times New Roman", 80),
                     text="你好"

                     )
    label.pack()

    #tori = tk.PhotoImage(file="fig/5.png")

#変数  
    tmr = 0
    jid = None

    # button = tk.Button(root, text="押すな", command=button_click)
    # button.bind("<1>", button_click)
    # button.pack()

    root.bind("<KeyPress>",key_down)
    root.mainloop()