import tkinter as tk
import random
root = tk.Tk()
root.geometry("600x600")
root.resizable(False, False)
root.title("8 puzzle")
#tạo ra bảng trạng thái của game
list_trang_thai = [1,2,3,4,5,6,7,8,""]
#trộn trại thái
random.shuffle(list_trang_thai)
buttoms = []
def swap(i):
    #Cần vị trí vô trống
    index_empty = list_trang_thai.index("")
    if (i-1==index_empty and i%3!=0) or \
        (i+1==index_empty and i%3!=2) or \
        (i-3==index_empty and i-3>=0) or \
        (i+3==index_empty and i+3<9):
        list_trang_thai[i],list_trang_thai[index_empty]=list_trang_thai[index_empty],list_trang_thai[i]
    for j in range(9):
        buttoms[j]["text"]=list_trang_thai[j]
def mau_sac():
    for i in range(9):
        if list_trang_thai[i]=="":
            buttoms[i].config(text="", bg="white")
        else:
            buttoms[i].config(text=list_trang_thai[i], bg="lightblue")
def kq(i):
    swap(i)
    mau_sac()

for i in range(9):
    btn = tk.Button(root, text=list_trang_thai[i], width=6, height=3, font=("Arial",20,"bold"),command = lambda i=i: kq(i))

    btn.grid(row=(i//3),column=(i%3))
    buttoms.append(btn)

mau_sac()
root.mainloop()

