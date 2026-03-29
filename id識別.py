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

# pack() -> - 控制方式：指定方向 side="top", "bottom", "left", "right"。
# grid() -> 用 row 、 column
# place() -> 用 xy 座標


import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk # 使用Pillow套件

# Indentification視窗
# 在定義子視窗時，label、button、entry都要在前面加win，因為這樣才能對應到視窗
# 子視窗 - 建立的按鈕
def window():
    win = tk.Toplevel()
    win.title("Indentification")

    win.geometry("400x300+800+300") # "500x300"
    win.config(background="#323232")
    win.iconbitmap("ixsuq-tkybo-001.ico")

    lb = tk.Label(win,text="請輸入身分證字號",bg="#323232",fg="skyblue",font="微軟正黑體 10")
    lb.grid(row=0,column=1,columnspan=2)


    identity_number = tk.Label(win,text="identity number:",bg="#323232",fg="skyblue")
    identity_number.grid(row=1,column=1)

    en = tk.Entry(win)
    en.grid(row=1,column=3)



    def answer():
        an = en.get().strip() # strip表示去掉空白
        print(an)
        if not an or len(an) != 10: # 如果為空白且不足10個
             return mistake()
        
        if not an[0].isupper() or not an[0].isalpha() or not an[1:].isdigit():
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
    win.bind('<Return>',lambda event:answer())


# 子視窗 - 查詢的按鈕
def window2():
    win = tk.Toplevel()
    win.title("inquiry")

    win.geometry("400x300+800+300") # geometry("寬 x 高 +x座標 +y座標")
    win.config(background="#323232") # config用來修改屬性
    

    # 插入小插圖
    img = Image.open("user.png")
    img = img.resize((50,50)) # 指定寬高
    mag = ImageTk.PhotoImage(img)
   

    lb = tk.Label(win,text="請輸入要查詢的身分證號碼:",bg="#323232",fg="skyblue",font="微軟正黑體 10",image=mag,compound="left")
    lb.image = mag
    lb.grid(row=1,column=1,columnspan=2) # columnspan 為跨欄的意思
      
    id_number = tk.Label(win,text="identity number:",bg="#323232",fg="skyblue")
    id_number.grid(row=2,column=1)

    en = tk.Entry(win) # 輸入框
    en.grid(row=2,column=2)
    
      
    def inquiry():
        user_input = en.get().strip()
        with open("answer.txt","r",encoding = "utf-8") as file:
            data = file.read().splitlines() # 把字串依照「換行符號」切割成一個 list
            
            if user_input in data:
                    messagebox.showinfo("查詢結果:",f"此帳號 '{user_input}' 存在")
            else:
                    messagebox.showinfo("查詢結果:","沒此帳號")    

    bt = tk.Button(win,text="提交",command=inquiry)
    bt.grid(row=3,column=1,columnspan=2)
    win.bind('<Return>',lambda event: inquiry()) # bind 是 Tkinter 用來「綁定事件」的方法，'<Return>' 表示鍵盤上的 Enter 鍵。


# 主頁面
win = tk.Tk()
win.title("首頁")
win.geometry("400x300+800+300")
win.config(background="#323232")

#建立資區域
frame1 =tk.Frame(win,bg="lightyellow")
frame1.pack(fill="x",pady=5)  # fill="x" 填滿x軸 ， pady為垂直間距 ， padx為水平間距

lab1 = tk.Label(frame1,text="建立資料區域",bg="lightyellow")
lab1.pack()


outbutton = tk.Button(frame1,text="建立ID",fg="black",command=window)
outbutton.pack(pady=10) # side預設為top

# 查詢資料區域
frame2 = tk.Frame(win,bg="lightblue")
frame2.pack(fill="x",pady=10)

lab2 = tk.Label(frame2,text="查詢資料區域",bg="lightblue")
lab2.pack() 

outbutton2 = tk.Button(frame2,text="查詢ID",fg="black",command=window2)
outbutton2.pack(pady=5)
win.mainloop()