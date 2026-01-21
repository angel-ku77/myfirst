'''
def id():
    id_list = []
    try:
        with open("identification.txt","r",encoding="utf-8") as file:
            for data in file:
                id_list.append(data.strip())
    except FileNotFoundError: 
        pass

    
    while True: 
        number =input("請輸入身分證:")
        if number == "1":
            break
            
        if number not in id_list:
            id_list.append(number)

        new = '\n'.join(id_list)
        # print(new) # return 只會執行一次

    with open("identification.txt","w",encoding="utf-8") as file:
        file.write(new)

# id()

def identify():
    import streamlit as st
    import pandas as pd
    file = pd.read_csv("identification.txt",header=None,names=["id"])
    dic = {}

    while True:
        
        number = input("請輸入要辨認的號碼:")

        if number == "1":
            break

        if number in file.values:
            if number not in dic:
                print("已領取")
                dic[number] = "已領取"
            else:
                print("重複領取")
                dic[number] = "重複領取"

        else:
            print("不存在")
            dic[number] = "不存在"


    # print(list(dic.items()),sep="")
    
    answer = pd.DataFrame(list(dic.items()),columns=["成員","查核結果"])

    # answer.to_csv("Identification Form.csv",index=False,encoding="utf-8")
    with open("Identification Form.csv","w",encoding="utf-8",newline="") as file:
            answer.to_csv(file,index=False)



identify()

'''
'''
def oi():
    answer = en.get()
    print(answer)
'''


# tk.Toplevel()是子視窗，可以有很多個 
# tk.TK()是主視窗，只能一個 
# 上述皆為規定

# mainloop() 只要在主視窗呼叫一次
# 子視窗會自動跟著主視窗的執行，不需要再呼叫 mainloop()


import tkinter as tk
from tkinter import messagebox

# Indentification視窗
# 在定義子視窗時，label、button、entry都要在前面加win，因為這樣才能對應到視窗
def window():
    win = tk.Toplevel()
    win.title("Indentification")

    win.geometry("400x300+800+300") # "500x300"
    win.config(background="#323232")
    win.iconbitmap("ixsuq-tkybo-001.ico")

    lb = tk.Label(win,text="請輸入身分證字號",bg="#323232",fg="skyblue",font="微軟正黑體 10")
    lb.grid(row=0,column=1,columnspan=2)


    identity_number = tk.Label(win,text="identity number",bg="#323232",fg="skyblue")
    identity_number.grid(row=1,column=1)

    en = tk.Entry(win)
    en.grid(row=1,column=2)



    def answer():
        an = en.get().strip() # strip表示去掉空白
        print(an)
        if not an: # 如果為空白
             return mistake()
        
        with open("answer.txt","a",encoding="utf-8") as file: # a代表追加
                    file.write(an+'\n')


    def mistake():
         messagebox.showerror("錯誤訊息","輸入有誤，請重新輸入")
         '''
         win = tk.Toplevel()
         win.title("錯誤訊息")
         label = tk.Label(win,text="輸入有誤，請重新輸入")
         label.pack(expand=True) # 讓標籤置中
         '''


    bt = tk.Button(win,text="提交",command=answer)
    bt.grid(row=2,column=1,columnspan=2)
    win.bind('<Return>',lambda event: answer())

win = tk.Tk()
win.title("首頁")
win.geometry("400x300+800+300")
win.config(background="#323232")

outbutton = tk.Button(text="建立ID",fg="black",command=window)
outbutton.place(anchor="center",x=200,y=20)

outbutton2 = tk.Button(text="查詢ID",fg="black")
outbutton2.place(anchor="center",x=200,y=65)
win.mainloop()