from tkinter import *
from tkinter import messagebox
import customtkinter
from PIL import ImageTk,Image
import Main_Page

root = customtkinter.CTk()
root.title("Login Page")
root.geometry("925x500+300+200")
root.resizable(False, False)

customtkinter.set_appearance_mode("System") 
customtkinter.set_default_color_theme("blue")  


def signing():
    username = user.get()
    password = UserP.get()
    if username == "admin" and password == "1234":
        sign_up_button.pack()
        root.destroy()
        rental_root = customtkinter.CTk()  
        app = Main_Page.Main_Page(rental_root)
        rental_root.mainloop() 
        
    elif username != 'admin' and password != "1234":
        messagebox.showerror("INVALID", "Invalid username and password")
        
    elif username != "admin":
        messagebox.showerror("INVALID", "Invalid username")
        
    elif password != "1234":
        messagebox.showerror("INVALID", "Invalid password")

img = ImageTk.PhotoImage(file="Pictures/Pogi_Logo.png")  
Label(root, image=img, bg="white").place(x=-100, y=-195)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text="Sign in", fg="#57a1f8", bg="white", font=("Microsoft YaHei UI light", 23, "bold"))
heading.place(x=110, y=5)

def on_enter(e):
    user.delete(0, "end")

def on_leave(e):
    name = user.get()
    if name == "":
        user.insert(0, "Username")

user = Entry(frame, width=30, fg="black", border=0, bg="white", font=("Microsoft YaHei UI light", 11))
user.place(x=30, y=80)
user.insert(0, "Username")
user.bind("<FocusIn>", on_enter)
user.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e):
    UserP.delete(0, "end")

def on_leave(e):
    Pass = UserP.get()
    if Pass == "":
        UserP.insert(0, "Password")
        

UserP = Entry(frame, width=30, fg="black", border=0, bg="white", show="*", font=("Microsoft YaHei UI light", 11))
UserP.place(x=30, y=150)
UserP.insert(0, "Password")
UserP.bind("<FocusIn>", on_enter)
UserP.bind("<FocusOut>", on_leave)

Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text="Sign in", bg="#57a1f8", fg="white", border=0, command=signing).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg="black", bg="white", font=("Microsoft YaHei UI Light", 9))
label.place(x=75, y=270)

def sign_up():
    root.destroy()
    import Sign_upP

sign_up_button = Button(frame, width=6, text="Sign up", border=0, bg="white", cursor="hand2", fg="#57a1f8", command=sign_up)
sign_up_button.place(x=215, y=270),

print("LOL")

root.mainloop()
