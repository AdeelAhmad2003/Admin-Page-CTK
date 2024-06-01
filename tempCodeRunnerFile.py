from customtkinter import *
from CTkTable import CTkTable
from PIL import Image
import customtkinter as ctk
from tkinter import ttk
import pyodbc

app = CTk()
app.geometry("1200x670")
app.resizable(0,0)

set_appearance_mode("light")

main_frame = CTkFrame(master=app, fg_color="#2A8C55",  width=1200, height=670, corner_radius=0)
main_frame.pack_propagate(0)
main_frame.pack(fill="y", anchor="w", side="left")

logo_img_data = Image.open("logo.png")
logo_img = CTkImage(dark_image=logo_img_data, light_image=logo_img_data, size=(77.68, 85.42))

label1=CTkLabel(master=main_frame, text="Welcome!!!", image=logo_img,fg_color="transparent", font=("Arial Bold", 25),anchor="w")
label1.pack(pady=(38, 10),anchor="n")

menu_img_data = Image.open("menu.png")
menu_img = CTkImage(dark_image=menu_img_data, light_image=menu_img_data,size=(100,100))

menu=CTkButton(master=main_frame, image=menu_img, text="Menu Management",fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="w")
menu.pack(side='left',anchor="center", ipady=10, pady=(16, 0))

employee_img_data = Image.open("employees.png")
employee_img = CTkImage(dark_image=employee_img_data, light_image=employee_img_data,size=(100,100))
employee=CTkButton(master=main_frame, image=employee_img, text="Employee Management", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="w")
employee.pack(side='left',anchor="center", ipady=10, pady=(16, 0))

inventory_img_data = Image.open("inventory_1.png")
inventory_img = CTkImage(dark_image=inventory_img_data, light_image=inventory_img_data,size=(100,100))
inventory=CTkButton(master=main_frame, image=inventory_img, text="Inventory Management", fg_color="transparent", font=("Arial Bold", 25), hover_color="#207244", anchor="w")
inventory.pack(side='left',anchor="center", ipady=10, pady=(16, 0))
