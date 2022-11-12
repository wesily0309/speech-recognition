import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
'''
# 圖形化正在測試階段
root = tk.Tk()
root.title('oxxo.studio')
root.geometry('200x200')

def show():
    global file_path#全局變數
    file_path = filedialog.askopenfilename()   # 選擇檔案後回傳檔案路徑與名稱
    print(file_path)               # 印出路徑

# Button 設定 command 參數，點擊按鈕時執行 show 函式
btn = tk.Button(root,
                text='開啟檔案',
                font=('Arial',20,'bold'),
                command=show
              )
btn.pack()

root.mainloop()
'''


file=input("輸入檔案路徑:")
import speech_recognition as sr
r = sr.Recognizer()                        #預設辨識英文
with sr.WavFile(file) as source:    #讀取wav檔
    audio = r.record(source)
try:
    print("Transcription: " + r.recognize_google(audio,language="zh-TW"))
                                           #使用Google的服務
except LookupError:
    print("Could not understand audio")