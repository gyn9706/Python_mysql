from tkinter import *
from tkinter import messagebox

def func_open():
    messagebox.showinfo("메뉴선택","열기 메뉴를 선택함")

def func_exit():
    window.quit()
    window.destroy()

window=Tk()

mainMenu=Menu(window)
window.config(menu=mainMenu) # 윈도우 창에 등록 //config: 구성하다
#mainMenu.pack()

fileMenu=Menu(mainMenu)
mainMenu.add_cascade(label="파일",menu=fileMenu) # 상위메뉴와 하위메뉴 연결
fileMenu.add_command(label="열기",command=func_open) #기본 메뉴 항목 생성
fileMenu.add_separator() #구분선
fileMenu.add_command(label="종료",command=func_exit)

window.mainloop()