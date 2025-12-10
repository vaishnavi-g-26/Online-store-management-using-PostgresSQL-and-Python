# app.py
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from database import get_connection
import customtkinter

def authenticate(username, password):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
    except Exception as e:
        print("DB Error:", e)
        return None

def login():
    username = username_entry.get()
    password = password_entry.get()
    user = authenticate(username, password)
    if user:
        messagebox.showinfo("Login Successful", f"Welcome, {username}")
        show_orders(username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def show_orders(username):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT o.orders_id, p.p_name, o.shipping_date, o.total_amount, o.status
            FROM orders o
            JOIN products p ON o.p_id = p.product_id
            WHERE o.customer_name = %s
        """, (username,))
        orders = cursor.fetchall()
        conn.close()

        order_window = tk.Toplevel(root)
        order_window.title("Orders")

        if not orders:
            tk.Label(order_window, text="No orders found.").pack()
        else:
            tree = ttk.Treeview(order_window, columns=("Order ID", "Product Name", "Shipping Date", "Price", "Status"), show="headings")
            tree.heading("Order ID", text="Order ID")
            tree.heading("Product Name", text="Product Name")
            tree.heading("Shipping Date", text="Shipping Date")
            tree.heading("Price", text="Price")
            tree.heading("Status", text="Status")
            for order in orders:
                tree.insert("", "end", values=order)
            tree.pack(fill="both", expand=True)
    except Exception as e:
        print("Error fetching orders:", e)

# GUI setup
customtkinter.set_appearance_mode('dark')
root = customtkinter.CTk()
root.geometry('600x440')
root.title("Login Demo")

frame = customtkinter.CTkFrame(master=root, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor="center")

l2 = customtkinter.CTkLabel(master=frame, text='Log into your Account', font=('Century Gothic', 20))
l2.place(x=50, y=45)

username_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
username_entry.place(x=50, y=110)

password_entry = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show='*')
password_entry.place(x=50, y=170)

login_button = customtkinter.CTkButton(master=frame, width=220, text="Login", command=login, corner_radius=6)
login_button.place(x=50, y=240)

root.mainloop()
