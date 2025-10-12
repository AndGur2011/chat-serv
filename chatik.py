from customtkinter import *
window = CTk() #создание окна
window.title("Чатик 1.0") #изменение названия
window.geometry("1080x500") #изменение размера
window.configure(fg_color ="purple") #изменение цвета заднего фона .configure может изменять все и как угодно
count = 0
def click():
    global count
    count += 10
    #print(count)
    label_click.configure(text= str(count))

btn = CTkButton(window, width=90,height=90,text="Тык",hover_color="red", command=click,font = ("Arial", 30 , "bold") ) #создание кнопки
btn.place(x = 0,y=100)
btn.pack() #прикрепление кнопки с окну
label_click = CTkLabel(window , width = 140, height=100 , bg_color="lightgreen", text="0", font = ("Arial", 30 , "bold"))
label_click.pack(pady = 50 , padx = 14)














window.mainloop()
