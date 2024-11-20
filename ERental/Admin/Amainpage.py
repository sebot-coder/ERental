import tkinter
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.title("Admin")
app.geometry("1500x800")

SettingF = customtkinter.CTkFrame(master=app, height=770, width=400, corner_radius=8, border_color="white")
SettingF.place(x=30, y=15)

image_path = "Pictures/Location.png"  

try:
    image = Image.open(image_path)
    resized_image = image.resize((300, 300))
    user_photo = ImageTk.PhotoImage(resized_image)

    img_label = customtkinter.CTkLabel(master=SettingF, image=user_photo, text="") 
    img_label.pack(pady=20) 
    
except FileNotFoundError:
    print(f"Error: File not found at {image_path}")

DataT = customtkinter.CTkFrame(master=app, height=770, width=1130, corner_radius=8, border_color="white")
DataT.place(x=360, y=15)

Frame_but = customtkinter.CTkFrame(master=app, height=415, width=340, corner_radius=8, border_color="white")
Frame_but.place(x=10, y=370)

Log_out_Button = customtkinter.CTkButton(master=Frame_but, text='Logout', fg_color='black', bg_color='white',anchor='center')
Log_out_Button.pack()

Analytic = customtkinter.CTkButton(master=Frame_but, text='Users', fg_color='black', bg_color='white',anchor='center')
Analytic.place(x=10, y=30)
Analytic.pack()

app.mainloop()

