from tkinter import *
from tkinter import messagebox
import customtkinter
import re

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Sign up")
root.geometry("925x500+300+200")
root.config(bg="#fff")
root.resizable(False, False)

def BackB():
    root.destroy()
    import Front_page
    
def enter_pass():
    username = UserN.get()
    phone = PhoneN.get()
    password = PassWo.get()
    confirm_password = PassWRe.get()

    if username == "":
        messagebox.showerror("Invalid", "Username cannot be empty")
    elif not re.match(r"^[0-9]{11}$", phone):
        messagebox.showerror("Invalid", "Enter a valid 11-digit phone number")
    elif password == "":
        messagebox.showerror("Invalid", "Password cannot be empty")
    elif confirm_password == "":
        messagebox.showerror("Invalid", "Please re-enter the password")
    elif password != confirm_password:
        messagebox.showerror("Invalid", "Passwords do not match")
    else:
        messagebox.showinfo("Success", "You have successfully signed up!")
        root.destroy()
        import Main_Page 
        rental_root = Tk()
        app = Main_Page.Main_Page(rental_root)
        rental_root.mainloop()

img = PhotoImage(file="Pictures/um.png")
Label(root, image=img, bg="white").place(x=0, y=0)

frame = Frame(root, width=450, height=500, bg="light blue", border=5)
frame.place(x=50, y=0)

label = Label(frame, text="Sign Up", fg="black",bg="lightblue",font=("Century Gothic", 40, "bold",))
label.place(x=120, y=10)

UserNL = Label(frame, text="Username:", fg="black", bg="light blue", font=("Century Gothic", 11))
UserNL.place(x=58, y=115)
UserN = Entry(frame, width=30, fg="black", border=0, bg="light blue", font=("Century Gothic", 11))
UserN.place(x=140, y=117)
Frame(frame, width=260, height=2, bg="black").place(x=140, y=145)

PhoneNu = Label(frame, text="Phone Number:", fg="black", bg="light blue", font=("Century Gothic", 11))
PhoneNu.place(x=27, y=155)
PhoneN = Entry(frame, width=30, fg="black", border=0, bg="light blue", font=("Century Gothic", 11))
PhoneN.place(x=140, y=157)
Frame(frame, width=260, height=2, bg="black").place(x=140, y=185)

PassW = Label(frame, text="Password:", fg="black", bg="light blue", font=("Century Gothic", 11))
PassW.place(x=67, y=195)
PassWo = Entry(frame, width=30, fg="black", border=0, bg="light blue", font=("Century Gothic", 11), show="*")
PassWo.place(x=140, y=197)
Frame(frame, width=260, height=2, bg="black").place(x=140, y=225)

PassWR = Label(frame, text="Re-enter Password:", fg="black", bg="light blue", font=("Century Gothic", 11))
PassWR.place(x=9, y=235)
PassWRe = Entry(frame, width=30, fg="black", border=0, bg="light blue", font=("Century Gothic", 11), show="*")
PassWRe.place(x=140, y=237)
Frame(frame, width=260, height=2, bg="black").place(x=140, y=265)

nextB = Button(frame, width=7, pady=7, text="Sign up", border=0, bg="light blue", cursor="hand2", fg="black",
            font=("Century Gothic", 12, "bold"), command=enter_pass)
nextB.place(x=350, y=450)

BackB = Button(frame, width=8, pady=7, text="Back", border=0, bg="light blue", cursor="hand2", fg="black",
            font=("Century Gothic", 12, "bold"), command=BackB)
BackB.place(x=270, y=450)

root.mainloop()
