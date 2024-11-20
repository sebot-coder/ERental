import tkinter
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("green")  


app = customtkinter.CTk()  
app.geometry("600x440")
app.title('Admin Login')
app.resizable(False,False)

def signing():
    username = User.get()
    password = UserP.get()
    if username == "admin" and password == "1234":
        app.destroy()
        import Amainpage
        
        
    elif username != 'admin' and password != "1234":
        messagebox.showerror("INVALID", "Invalid username and password")
        
    elif username != "admin":
        messagebox.showerror("INVALID", "Invalid username")
        
    elif password != "1234":
        messagebox.showerror("INVALID", "Invalid password")

img1=ImageTk.PhotoImage(Image.open("Pictures/Campus.jpg"))
Pic=customtkinter.CTkLabel(master=app,image=img1)
Pic.pack()

frame=customtkinter.CTkFrame(master=Pic, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

Header=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
Header.place(x=50, y=45)

User=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
User.place(x=50, y=110)

UserP=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
UserP.place(x=50, y=165)

button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=signing, corner_radius=6)
button1.place(x=50, y=240)

app.mainloop()