import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import os


##############################################+=============================================================
root = tk.Tk()
root.configure(background="grey")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("700x650+200+100")
root.title("login")

username = tk.StringVar()
password = tk.StringVar()
        
# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
try:
    if os.path.exists('log.jpg'):
        image2 = Image.open('log.jpg')
        # Fixed: Replace Image.ANTIALIAS with Image.LANCZOS
        image2 = image2.resize((w,h), Image.LANCZOS)
        
        background_image = ImageTk.PhotoImage(image2)
        background_label = tk.Label(root, image=background_image)
        background_label.image = background_image
        background_label.place(x=0, y=0)
    else:
        print("Background image 'log.jpg' not found. Using default background.")
except Exception as e:
    print(f"Error loading background image: {e}")

def registration():
    try:
        from subprocess import call
        call(["python","register.py"])
        root.destroy()
    except Exception as e:
        ms.showerror("Error", f"Could not open registration: {e}")

def login():
    try:
        # Establish Connection
        with sqlite3.connect('evaluation.db') as db:
            c = db.cursor()

            # Find user If there is any take proper action
            cursor = db.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                              "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
            db.commit()
            
            find_entry = ('SELECT * FROM registration WHERE username = ? and password = ?')
            c.execute(find_entry, [(username.get()), (password.get())])
            result = c.fetchall()

            if result:
                msg = ""
                print(msg)
                ms.showinfo("Message", "LogIn successfully")
                root.destroy()

                from subprocess import call
                call(['python','expression_Analysis.py'])
            else:
                ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
                
    except sqlite3.Error as e:
        ms.showerror("Database Error", f"Database error: {e}")
    except Exception as e:
        ms.showerror("Error", f"An error occurred: {e}")

# Load images with error handling
def load_image(filepath, default_size=(100, 100)):
    try:
        if os.path.exists(filepath):
            img = Image.open(filepath)
            img = img.resize(default_size, Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        else:
            print(f"Image file '{filepath}' not found.")
            return None
    except Exception as e:
        print(f"Error loading image '{filepath}': {e}")
        return None

# Load icons with fallback handling
bg1_icon = load_image("C:/Users/balaj/Downloads/Movie-Recommendation-system/b.jpg", (600, 550))
bg_icon = load_image("C:/Users/balaj/Downloads/Movie-Recommendation-system/L.jpg")
user_icon = load_image("C:/Users/balaj/Downloads/Movie-Recommendation-system/l1.png", (30, 30))
pass_icon = load_image("C:/Users/balaj/Downloads/Movie-Recommendation-system/p1.jpg", (30, 30))

# Create UI elements with error handling for missing images
if bg1_icon:
    bg_lbl = tk.Label(root, image=bg1_icon, width=600, height=550)
    bg_lbl.place(x=50, y=40)
else:
    # Fallback: create a colored rectangle if image not found
    bg_lbl = tk.Label(root, bg="lightblue", width=75, height=35)
    bg_lbl.place(x=50, y=40)

title = tk.Label(root, text="Login Here", font=("Algerian", 30, "bold", "italic"), 
                bd=5, bg="black", fg="white")
title.place(x=220, y=100, width=250)

Login_frame = tk.Frame(root, bg="white")
Login_frame.place(x=80, y=220)

if bg_icon:
    logolbl = tk.Label(Login_frame, image=bg_icon, bd=0).grid(row=0, columnspan=2, pady=20)
else:
    logolbl = tk.Label(Login_frame, text="LOGIN", font=("Arial", 16, "bold"), 
                      bg="white").grid(row=0, columnspan=2, pady=20)

# Username field
if user_icon:
    lbluser = tk.Label(Login_frame, text="Username", image=user_icon, compound=LEFT, 
                      font=("Times new roman", 20, "bold"), bg="white").grid(row=1, column=0, padx=20, pady=10)
else:
    lbluser = tk.Label(Login_frame, text="Username", font=("Times new roman", 20, "bold"), 
                      bg="white").grid(row=1, column=0, padx=20, pady=10)

txtuser = tk.Entry(Login_frame, bd=5, textvariable=username, font=("", 15))
txtuser.grid(row=1, column=1, padx=20)

# Password field
if pass_icon:
    lblpass = tk.Label(Login_frame, text="Password", image=pass_icon, compound=LEFT, 
                      font=("Times new roman", 20, "bold"), bg="white").grid(row=2, column=0, padx=50, pady=10)
else:
    lblpass = tk.Label(Login_frame, text="Password", font=("Times new roman", 20, "bold"), 
                      bg="white").grid(row=2, column=0, padx=50, pady=10)

txtpass = tk.Entry(Login_frame, bd=5, textvariable=password, show="*", font=("", 15))
txtpass.grid(row=2, column=1, padx=20)

# Buttons
btn_log = tk.Button(Login_frame, text="Login", command=login, width=15, 
                   font=("Times new roman", 14, "bold"), bg="blue", fg="white")
btn_log.grid(row=3, column=1, pady=10)

btn_reg = tk.Button(Login_frame, text="Create Account", command=registration, width=15, 
                   font=("Times new roman", 14, "bold"), bg="brown", fg="white")
btn_reg.grid(row=3, column=0, pady=10)

def window():
    root.destroy()

if __name__ == "__main__":
    root.mainloop()