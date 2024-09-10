import socket
import threading
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from mysql.connector import Error

# Function to connect to the database
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

def display_img(path, player_frame):
    if path:
        # Display the new card image side by side in the current player's frame
        img = Image.open(path)
        img = img.resize((100, 150))
        photo = ImageTk.PhotoImage(img)
        label = Label(player_frame, image=photo, bg='#35654d')
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack(side=LEFT, padx=5)

def display_cards(message):
    # Split the message to get username and card paths
    parts = message.split('>>>')
    username = parts[0].strip()
    card_paths = parts[1].strip().split('-')

    # Create a new frame for this player's cards
    global player_frame
    player_frame = Frame(canvas, bg='#35654d', padx=10, pady=5)
    # player_frame.pack(anchor='w')
    canvas.create_window((0, canvas.bbox("all")[3]), window=player_frame, anchor="nw")

    # Add the username as a label above the cards
    Label(player_frame, text=username, fg='#fff', bg='#35654d', font=('Microsoft YaHei UI Light', 10, 'bold')).pack(anchor='w')

    # Display each card image in the player's frame
    for path in card_paths:
        display_img(path, player_frame)

    # Update scroll region to include new content
    canvas.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

# Function to receive messages from the server
def receiving(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
             
            if "Waiting" in message:
                messagebox.showinfo("Waiting", "Waiting for the others to start the game...")

            elif message == "Start":
                # Send a request to deal cards
                client.send("deal_cards".encode('utf-8'))

            elif "\n" in message:
                msg = message.split("\n")
                if len(msg)>1:
                    for i in msg:
                        if ">>>" in i:
                            display_cards(i)
                
            elif ">>>" in message:
                display_cards(message)

            elif "One more card?(y/n)" in message:
                send_answer()

            elif "Your new card is" in message:
                # Handle displaying the new card
                card_path = message.split(':')[1].strip()
                display_img(card_path, player_frame)

            elif "Winner is" in message:
                Label(window, text=message, bg='#35654d', fg='white', font=('Microsoft YaHei UI Light', 12, 'bold')).pack()
                print("Server closed the connection.")
                client.send("closing".encode('utf-8'))
                break
            else:
                Label(window, text=message, bg='#35654d', fg='white').pack()

        except Exception as e:
            Label(window, text=f"[ERROR] {e}", bg='#35654d', fg='red').pack()
            break

def send_answer():
    # Display a message box with OK and Cancel buttons
    user_response = messagebox.askokcancel("Confirm", "Would you like to draw one more card?")

    if user_response:  # If the user clicked OK
        ans = "y"
    else:  # If the user clicked Cancel
        ans = "n"

    client.send(ans.encode('utf-8'))

# Function to start the client and connect to the server
def open_client(email):
    global client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('172.20.0.185', 8000))

    global window
    window = Tk()
    window.title('Client')
    window.state('zoomed')
    window.configure(bg='#35654d')

    # Create a Frame to hold the Canvas and Scrollbars
    main_frame = Frame(window)
    main_frame.pack(fill=BOTH, expand=True)

    # Create a Canvas widget
    global canvas
    canvas = Canvas(main_frame, bg='#35654d')
    canvas.pack(side=LEFT, fill=BOTH, expand=True)

    # Create a Scrollbar
    scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    # Link the Scrollbar with the Canvas
    canvas.config(yscrollcommand=scrollbar.set)

    # Create a Frame inside the Canvas
    canvas_frame = Frame(canvas, bg='#35654d')
    canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

    # Update scroll region to include the Canvas content
    def on_canvas_configure(event):
        canvas.config(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_canvas_configure)
    # Fetch the username from the database
    connection = connect_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM users WHERE email=%s", (email,))
        result = cursor.fetchone()
        username = result[0] if result else "Unknown"
        Label(window, text=username, fg='#fff', bg='#35654d', font=('Microsoft YaHei UI Light', 10, 'bold')).pack()
        cursor.close()
        connection.close()

    # Send the username to the server
    client.send(username.encode('utf-8'))

    # Start a thread to receive messages from the server
    receive_thread = threading.Thread(target=receiving, args=(client,))
    receive_thread.start()

    window.mainloop()