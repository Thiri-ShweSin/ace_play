from tkinter import *
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import re

def is_valid_password(password):
    # Define the pattern to search for special characters
    pattern = r'[!@#$%^&*()\-_+=]'
    
    # Search for the pattern in the password
    if re.search(pattern, password):
        return True  # Contains at least one special character
    return False  # No special characters found

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='ace_play',
            user='root',
            password='09795334737'
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
        return None

def open_signup_window(main_window):
    # Create the Sign Up window
    signup_window = Toplevel(main_window)
    signup_window.title('Sign Up')
    
    # Center the signup window
    signup_width = 400
    signup_height = 400
    x = (signup_window.winfo_screenwidth()//2)-(signup_width//2)
    y = (signup_window.winfo_screenheight()//2)-(signup_height//2)
    signup_window.geometry(f'{signup_width}x{signup_height}+{x}+{y}')
    signup_window.configure(bg='#fff')
    
    # SignUp Frame
    frame = Frame(signup_window, width=250, height=250, bg='#fff')
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    heading = Label(frame, text='Sign Up', fg='#333', bg='#fff', font=('Microsoft YaHei UI Light', 18, 'bold'))
    heading.pack()

    def on_enter(e):
        e.widget.delete(0, 'end')

    def on_leave(e):
        if e.widget.get() == '':
            e.widget.insert(0, e.widget.placeholder)

    user = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    user.placeholder = 'Username'
    user.insert(0, user.placeholder)
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    user.pack(pady=(50, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    email = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    email.placeholder = 'Email'
    email.insert(0, email.placeholder)
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    email.pack(pady=(30, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    password = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    password.placeholder = 'Password'
    password.insert(0, password.placeholder)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)
    password.pack(pady=(30, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    confirm = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    confirm.placeholder = 'Confirm Password'
    confirm.insert(0, confirm.placeholder)
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)
    confirm.pack(pady=(30, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    def check():
        username = user.get()
        mail = email.get()
        pwd = password.get()
        cnf_pwd = confirm.get() 

        if username == user.placeholder or mail == email.placeholder or pwd == password.placeholder or cnf_pwd == confirm.placeholder:
            messagebox.showerror("Error","Please fill all required fields")
        else:
            if '@' not in mail:
                messagebox.showerror("Error", "Please enter a valid mail address")
            elif pwd != cnf_pwd:
                messagebox.showerror("Error", "Passwords do not match!")
            elif not is_valid_password(pwd):
                messagebox.showerror("Error", "Password should contain at least one special character like !, @, #.")
            else:
                connection = connect_db()
                if connection:
                    cursor = connection.cursor()
                    try:
                        cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, mail, pwd))
                        connection.commit()
                        messagebox.showinfo("Signup Success", "Account created successfully!")
                        signup_window.destroy()  # Close the sign-up window
                        main_window.deiconify()  # Show the main window
                    except mysql.connector.Error as e:
                        messagebox.showerror("Signup Error", f"Error: {e}")
                    finally:
                        cursor.close()
                        connection.close()

    Button(frame, width=35, border=0, pady=10, text='Sign Up', fg='#fff', bg='#333', command=check).pack(pady=20)