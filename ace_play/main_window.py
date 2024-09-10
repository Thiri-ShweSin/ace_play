from tkinter import *
from tkinter import messagebox
from signup_window import open_signup_window  # Import the function from the other file
from gamerules_window import open_gamerules
from menu import game_menu
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host='172.20.0.185',
            database='ace_play',
            user='remote_user',
            password='mypassword123'
        )
        return connection
    except Error as e:
        messagebox.showerror("Database Error", f"Error connecting to MySQL: {e}")
        return None

def main_window():
    # Main Window
    root = Tk()
    root.title('Login')

    width = 400
    height = 400
    x = (root.winfo_screenwidth()//2)-(width//2)
    y = (root.winfo_screenheight()//2)-(height//2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    root.configure(bg='#fff')
    root.resizable(False, False)

    # SignUp Frame
    frame = Frame(root, width=250, height=250, bg='#fff', padx=50, pady=50)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    heading = Label(frame, text='Sign in', fg='#333', bg='#fff', font=('Microsoft YaHei UI Light', 18, 'bold'))
    heading.pack()

    def on_enter(e):
        e.widget.delete(0, 'end')

    def on_leave(e):
        if e.widget.get() == '':
            e.widget.insert(0, e.widget.placeholder)

    email = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    email.placeholder = 'Email'
    email.insert(0, email.placeholder)
    email.bind('<FocusIn>', on_enter)
    email.bind('<FocusOut>', on_leave)
    email.pack(pady=(50, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    password = Entry(frame, width=35, border=0, fg='#333', font=('Microsoft YaHei UI Light', 10))
    password.placeholder = 'Password'
    password.insert(0, password.placeholder)
    password.bind('<FocusIn>', on_enter)
    password.bind('<FocusOut>', on_leave)
    password.pack(pady=(30, 0))
    Frame(frame, width=250, height=1, bg='#333').pack()

    def sign_in():
        connection = connect_db()
        if connection:
            mail = email.get()
            pwd = password.get()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM users WHERE email=%s AND password=%s", (mail, pwd))
            result = cursor.fetchone()
            if result:
                messagebox.showinfo("Success", "Login successful!")
                root.destroy()
                game_menu(mail)
            else:
                messagebox.showerror("Error", "Invalid credentials")
            cursor.close()
            connection.close()

    Button(frame, width=35, border=0, pady=10, text='Sign in', fg='#fff', bg='#333', command=sign_in).pack(pady=20)

    def on_sign_up_click(event):
        root.withdraw()  # Hide the login window
        open_signup_window(root)  # Pass the root window to reopen later

    text_label = Label(frame, bg='#fff', font=('Microsoft YaHei UI Light', 8))
    text_label.pack()

    # Creating a Text widget to handle rich text
    text_widget = Text(text_label, bg='#fff', borderwidth=0, height=1, width=35, wrap=WORD, font=('Microsoft YaHei UI Light', 8))
    text_widget.pack()
    text_widget.insert(INSERT, "Don't have an account? ")
    text_widget.insert(INSERT, "Sign Up", ('link'))
    text_widget.tag_configure('link', foreground='#007bff', font=('Microsoft YaHei UI Light', 8, 'bold'))
    text_widget.config(cursor='hand2')
    text_widget.bind('<Button-1>', on_sign_up_click)
    text_widget.config(state=DISABLED)  # Make the Text widget read-only

    root.mainloop()

if __name__ == "__main__":
    main_window()