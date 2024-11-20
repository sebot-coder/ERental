from tkinter import *
import tkinter as tk
from typing import Self
from tkintermapview import TkinterMapView
import customtkinter

Lo = customtkinter.CTk()
Lo.title("Station Location")
Lo.geometry("950x550")
Lo.resizable(False, False)

gmap_widget = LabelFrame(Lo)
gmap_widget = TkinterMapView(Lo, width=1050 , height=650, corner_radius=0)
gmap_widget.pack(pady=20)
gmap_widget.set_zoom(17)


gmap_widget.set_position(7.066488136498032, 125.5956815649072)
marker_1 = gmap_widget.set_marker(7.065089, 125.598142, text="Matina Gate")
marker_2 = gmap_widget.set_marker(7.065483, 125.596321, text="BE building")
marker_3 = gmap_widget.set_marker(7.067424, 125.596408, text="GET building")
marker_4 = gmap_widget.set_marker(7.068349, 125.595643, text="DPT Building")
marker_5 = gmap_widget.set_marker(7.067512, 125.592169, text="MAA Gate")

marker_1.set_position(7.065089, 125.598142)
marker_2.set_position(7.065483, 125.596321)
marker_3.set_position(7.067424, 125.596408)
marker_4.set_position(7.068349, 125.595643)
marker_5.set_position(7.067512, 125.592169)


def Back():
    Lo.destroy()  
    import Main_Page  
    rental_root = customtkinter.CTk()
    app = Main_Page.Main_Page(rental_root)
    rental_root.mainloop()  

back_button = customtkinter.CTkButton(master=Lo, text="Back",width=100, bg_color="white", fg_color="#57a1f8", cursor="hand2",corner_radius=1, command=Back,font=('Century Gothic',20))
back_button.place(x=800, y=500)



Lo.mainloop()

