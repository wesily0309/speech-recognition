import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
from tkinter import*


root = tk.Tk()
root.title('oxxo.studio')
root.geometry('500x500')

lb=tk.Label(text="")

def show():
    global file_path#全局變數
    file_path = filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    print(file_path)
    host()               # 印出路徑
############################
def host():
    r = sr.Recognizer()                  
    with sr.WavFile(file_path) as source:    #讀取wav檔
        audio = r.record(source) 
    try:                                                               #設定中文
        print("Transcription: " + r.recognize_google(audio,language="zh-TW"))
                                                #使用Google的服務
    except LookupError:
        print("Could not understand audio")
#############################

# Button 設定 command 參數，點擊按鈕時執行 show 函式
lb=tk.Label(text="選擇wav檔案",font=('Arial',30,'bold'))
lb.pack()

btn = tk.Button(root,text='匯入wav音檔',font=('Arial',20,'bold'),command=show)
btn.pack()
#選擇wav檔案


lb2=tk.Label(text='匯入後等待一段時間',font=('Arial',10,'bold'))
lb2.pack()

lb3=tk.Label(text='到提示字元視窗複製結果',font=('Arial',10,'bold'))
lb3.pack()



root.mainloop()


    #file=input("輸入檔案路徑:")
    #print("轉換中...")
'''
r = sr.Recognizer()                  
with sr.WavFile(file_path) as source:    #讀取wav檔
    audio = r.record(source)
try:                                                               #設定中文
    print("Transcription: " + r.recognize_google(audio,language="zh-TW"))
                                            #使用Google的服務
except LookupError:
    print("Could not understand audio")
'''
