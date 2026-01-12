'''
import tkinter as tk
win = tk.Tk()
win = tk.mainloop()
'''
def vocabulary():
    import tkinter as tk
    dic = {}

    try:
        with open("vocabulary.txt","r",encoding="utf-8") as file:
            for data in file:
                eng, chi = data.strip().split("\t")
                dic[eng] = chi
    except FileNotFoundError:
        pass # 如果檔案不存在就跳過

    
    while True:
        English = input("請輸入英文:")
        if English == "1":
            break
        
        chinese = input("請輸入中文:")
        if chinese == "1":
            break

        i = English
        if i not in dic:
            dic[i] = chinese
        else:
            print("已存在") 
            continue # 當已存在就跳過
        
        

        
    with open("vocabulary.txt","w",encoding="utf-8") as file:
        for k,v in dic.items():
            file.write(f"{k}\t{v}\n") # write不能用sep ， v具有換行的效果
            
        
    
vocabulary()

# 單字查詢
def inquire():
    import pandas as pd
    from colorama import init,Fore,Style
    init(autoreset=True)
    print("--- Vocabulary Inquire ---")
    while True:
        file = pd.read_csv("vocabulary.txt",sep="\t",header=None,names=["En","Ch"])
        word = input("請輸入英文單字:")

        if word == "1":
            print(Fore.RED + "--- Finish ---")
            


        if word in file['En'].values:
            answer = file.loc[file["En"] == word ,"Ch"].values[0]
            print(f"Answer : {answer}" + "\n")
        else:
            print(Fore.BLUE + "!!! 此單字未建立" + "\n")

        word2 = input("請輸入中文單字:")
        if word2 == "1":
            print(Fore.RED + "--- Finish ---")
            break

        if word2 in file['Ch'].values:
            answer = file.loc[file["Ch"] == word2 ,"En"].values[0]
            print(f"Answer : {answer}" + "\n")
        else:
            print(Fore.BLUE + "!!! 此單字未建立" + "\n")



# inquire()


# 單字測試
def test():
    import random 
    import pandas as pd
    from colorama import init, Fore, Style
    init(autoreset=True)
    print("--- Vocabulary Test ---")
    file = pd.read_csv("vocabulary.txt",sep="\t",header=None,names=["En","Ch"])
    while True:
        
        row = file.sample(1).iloc[0]
        english = row["En"]
        chinese = row["Ch"]

        mode = random.choice(["En","Ch"])

        if mode == "En":
            print(english)
            user = input("中文(1為跳出):")
            if user == "1":
                break
            if user == chinese:
                print(Fore.GREEN + "--- Your answer is Right. ---" + "\n")
            else:
                print(Fore.RED + "--- Your answer is Error. ---" + "\n") # colorama.fore只支援8種顏色
        else:
            print(chinese)
            user = input("英文(1為跳出):")

            if user == "1":
                break

            if user == english:
                print(Fore.GREEN+ "--- Your answer is Right. ---" + "\n")
            else:
                print(Fore.RED + "--- Your answer is Error. ---" + "\n")

# test()
