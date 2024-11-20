import customtkinter
import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk

class Main_Page:
    def __init__(self, master):
        self.master = master
        master.title("E-Scooter Rental System")
        master.geometry("950x500+300+200")
        master.resizable(False, False)
        master.config(bg="blue")

        self.balance = 0
        self.timer_running = False
        self.start_time = 0
        self.total_time = 0  
        self.deduction_rate_per_second = 0.031
        self.deducted_amount = 0  

        self.sections = {
            "Matina Gate": ["Scooter 1", "Scooter 2", "Scooter 3", "Scooter 4"],
            "BE building": ["Scooter 5", "Scooter 6", "Scooter 7", "Scooter 8"],
            "GET building": ["Scooter 9", "Scooter 10", "Scooter 11", "Scooter 12"],
            "DPT building": ["Scooter 13", "Scooter 14", "Scooter 15", "Scooter 16"],
            "MAA gate": ["Scooter 17", "Scooter 18", "Scooter 19", "Scooter 20"]
        }

        self.label = customtkinter.CTkLabel(master, text="Choose a station and e-scooter:", font=("Microsoft YaHei UI light", 11))
        self.label.place(x=30, y=23)

        self.section_var = tk.StringVar(value="Matina Gate")
        self.section_menu = customtkinter.CTkOptionMenu(master, variable=self.section_var, values=list(self.sections.keys()), command=self.update_scooter_menu)
        self.section_menu.place(x=30, y=63)

        self.scooter_var = tk.StringVar(value=self.sections["Matina Gate"][0])
        self.scooter_menu = customtkinter.CTkOptionMenu(master, variable=self.scooter_var, values=self.sections["Matina Gate"])
        self.scooter_menu.place(x=30, y=103)

        self.balance_label = customtkinter.CTkLabel(master, text="Balance: 0 pesos", font=("Microsoft YaHei UI light", 20), bg_color="gray", fg_color="black", width=300)
        self.balance_label.place(x=600, y=0)

        self.timer_label = customtkinter.CTkLabel(master, text="Timer: 0 minutes 0 seconds", font=("Microsoft YaHei UI light", 30))
        self.timer_label.place(x=350, y=100)

        # Buttons
        self.button_rent = customtkinter.CTkButton(master, text="Rent Scooter", command=self.rent_scooter, width=150)
        self.button_rent.place(x=750, y=240)

        self.button_return = customtkinter.CTkButton(master, text="Return Scooter", command=self.return_scooter, width=150)
        self.button_return.place(x=750, y=280)

        self.button_pause = customtkinter.CTkButton(master, text="Pause Rental", command=self.pause_rental, width=150)
        self.button_pause.place(x=750, y=320)

        self.button_resume = customtkinter.CTkButton(master, text="Resume Rental", command=self.resume_rental, width=150)
        self.button_resume.place(x=750, y=360)

        def Location():
            master.destroy()
            import Location_page

        self.button_show_location = customtkinter.CTkButton(master, text="Show Location", command=Location, width=150)
        self.button_show_location.place(x=750, y=400)

        self.button_logout = customtkinter.CTkButton(master, text="Logout", fg_color="#ff5c5c", command=self.logout, width=150)
        self.button_logout.place(x=750, y=440)

        self.button_add_balance = customtkinter.CTkButton(master, text="Add 100 Pesos to Balance", command=self.add_balance)
        self.button_add_balance.place(x=750, y=50)

        self.update_timer()

    def update_scooter_menu(self, *args):
        section = self.section_var.get()
        scooter_options = self.sections[section]
        self.scooter_menu.set(scooter_options[0])
        self.scooter_menu.configure(values=scooter_options)

    def rent_scooter(self):
        if self.balance < 1:
            messagebox.showerror("Error", "Insufficient balance to rent a scooter.")
            return
        
        self.timer_running = True
        self.start_time = time.time()
        self.total_time = 0  
        self.deducted_amount = 0  
        messagebox.showinfo("Rental Started", f"You have started renting {self.scooter_var.get()} from {self.section_var.get()}.")

    def return_scooter(self):
        if not self.timer_running:
            messagebox.showerror("Error", "You are not currently renting a scooter.")
            return
        
        self.timer_running = False
        messagebox.showinfo("Scooter Returned", f"You have returned {self.scooter_var.get()}. Remaining balance: {self.balance:.2f} pesos.")
        self.update_balance()

    def add_balance(self):
        self.balance += 100
        self.update_balance()
        messagebox.showinfo("Balance Updated", "You have added 100 pesos to your balance.")

    def pause_rental(self):
        if not self.timer_running:
            messagebox.showerror("Error", "Rental is not currently active.")
            return
        
        self.timer_running = False
        messagebox.showinfo("Rental Paused", "Your rental has been paused.")

    def resume_rental(self):
        if self.timer_running:
            messagebox.showerror("Error", "Rental is already active.")
            return
        
        self.timer_running = True
        self.start_time = time.time() - self.total_time  
        messagebox.showinfo("Rental Resumed", "Your rental has been resumed.")

    def update_balance(self):
        self.balance_label.configure(text=f"Balance: {self.balance:.2f} pesos")

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.total_time = elapsed_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            self.timer_label.configure(text=f"Timer: {minutes} minutes {seconds} seconds")
            
            deduction = self.total_time * self.deduction_rate_per_second - self.deducted_amount

            if self.balance - deduction >= 0:
                self.balance -= deduction
                self.deducted_amount += deduction
                self.update_balance()
            else:
                self.balance = 0
                self.update_balance()
                self.timer_running = False
                messagebox.showwarning("Warning", "Your balance has been exhausted. Rental stopped.")
        
        self.master.after(1000, self.update_timer)

    def logout(self):
        if messagebox.askokcancel("Logout", "Are you sure you want to logout?"):
            self.master.quit()
            self.master.destroy()


if __name__ == "__main__":
    root = customtkinter.CTk()
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = Main_Page(root)
    root.mainloop()
