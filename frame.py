from customtkinter import *
from PIL import Image
import socket
window = CTk()
window.title("Чатик 1.6")
window.geometry("1080x700")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1028))
def send():
    sms = enter.get()
    client.send(sms.encode())
    enter.delete(0, END)
    print(sms)
    textbox.configure(state="normal")
    textbox.insert(END, sms + "\n")
    textbox.configure(state = "disabled")



bg_image = Image.open("background.jfif")  # открываем файл фона
bg_photo = CTkImage(light_image=bg_image, size=(1080, 700))  # создаем CTkImage для фона

bg_label = CTkLabel(window, text="", image=bg_photo)  # создаем label с фоном
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

chat_frame = CTkFrame(window, fg_color="#00716a", corner_radius=15, width=700, height=350,)  # рамка для чата
chat_frame.place(x=190, y=40)
chat_frame.pack_propagate(False)

textbox = CTkTextbox(chat_frame, fg_color="#FFFFFF",state = "disabled", width = 650, height = 300)
textbox.pack(pady = 20)

enter = CTkEntry(window, width=850, height=50, placeholder_text="Введіть текст...", corner_radius=10, font=("Arial", 16))  # поле ввода
enter.place(x=100, y=420)

send_icon = Image.open("pixil-frame-0.png")  # иконка для кнопки (закомментирована)
send_icon = CTkImage(light_image=send_icon, size=(40, 40))

btn = CTkButton(window, text="Send", image=send_icon,
                 compound="left",
                font=("Arial", 20, "bold"), width=120, height=50,
                fg_color="#6A0DAD", hover_color="#9b30ff", corner_radius=10, command=send)  # кнопка отправки
btn.place(x=960, y=420)

window.mainloop()
