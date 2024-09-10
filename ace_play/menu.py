import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
from gamerules_window import open_gamerules
import socket
import subprocess
import time

def open_shan(email):
    window.destroy()
    open_gamerules(email)

def open_blackJack():
    messagebox.showinfo("BlackJack", "The game BlackJack is not available now.")

def wrap_text(text, font, max_width, draw):
    lines = []
    words = text.split(' ')
    current_line = ""

    for word in words:
        test_line = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test_line, font=font)
        width = bbox[2] - bbox[0]
        if width <= max_width:
            current_line = test_line
        else:
            if current_line:  # Add non-empty line
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def game_menu(email):
    global window
    window = tk.Tk()
    window.title("Game Menu")
    window.state('zoomed')

    # Load and set the background image
    bg_image = Image.open("./cards/bg2.jpg")
    bg_image = bg_image.resize((window.winfo_screenwidth(), window.winfo_screenheight()))
    darkened_bg_image = Image.new('RGB', bg_image.size, (0, 0, 0))
    bg_image = Image.blend(bg_image, darkened_bg_image, alpha=0.5)
    bg_photo = ImageTk.PhotoImage(bg_image)

    canvas = tk.Canvas(window, width=window.winfo_screenwidth(), height=window.winfo_screenheight())
    canvas.pack(fill="both", expand=True)
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")

    # Create a transparent text image
    text_image = Image.new("RGBA", (window.winfo_screenwidth(), window.winfo_screenheight()), (0, 0, 0, 0))
    draw = ImageDraw.Draw(text_image)

    # Define fonts
    title_font = ImageFont.truetype("arial.ttf", 50)
    description_font = ImageFont.truetype("arial.ttf", 18)

    title_text = "Ace Play"
    description_text = ("Welcome to Ace Play, the ultimate gaming platform where strategy meets fun! "
                         "Whether you're a seasoned card shark or just looking to unwind with a quick game, "
                         "Ace Play offers a diverse collection of card games designed to challenge your skills "
                         "and entertain you for hours. With a sleek interface, seamless multiplayer options, "
                         "and exciting game modes, Ace Play is your go-to destination for an immersive and enjoyable "
                         "gaming experience. Get ready to shuffle the deck, deal the cards, and play your way to victory!")

    # Draw title text
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_position = ((text_image.width - (title_bbox[2] - title_bbox[0])) // 2, 50)
    draw.text(title_position, title_text, font=title_font, fill=(255, 255, 255, 255))

    # Wrap and draw description text
    max_description_width = window.winfo_screenwidth() - 350
    description_lines = wrap_text(description_text, description_font, max_description_width, draw)
    
    description_y = title_position[1] + (title_bbox[3] - title_bbox[1]) + 50
    for line in description_lines:
        bbox = draw.textbbox((0, 0), line, font=description_font)
        line_width = bbox[2] - bbox[0]
        line_position = ((text_image.width - line_width) // 2, description_y)
        draw.text(line_position, line, font=description_font, fill=(255, 255, 255, 200))
        description_y += (bbox[3] - bbox[1]) + 5

    text_photo = ImageTk.PhotoImage(text_image)
    canvas.create_image(window.winfo_screenwidth() // 2, window.winfo_screenheight() // 2, image=text_photo, anchor="center")

    # Create a canvas for buttons with a background color similar to the main canvas
    button_canvas = tk.Canvas(canvas, bg='#240606', highlightthickness=0, width=500, height=150)
    button_canvas.place(relx=0.5, rely=0.65, anchor='center')

    # Load and resize images for buttons
    shan = Image.open("./cards/A8.jpg").resize((300, 200))
    shan_photo = ImageTk.PhotoImage(shan)

    # Poker button with image
    poker_button = tk.Button(button_canvas, text="Shan Koe Mee", image=shan_photo, compound="top", command=lambda: open_shan(email), bg='#000', fg='white', font=('Arial', 14))
    poker_button.image = shan_photo  # Keep a reference to avoid garbage collection
    poker_button.pack(side='left', padx=(0,50))

    blackJack = Image.open("./cards/blackjack.png").resize((300,200))
    blackJack_photo = ImageTk.PhotoImage(blackJack)

    # Second button with image
    tt_button = tk.Button(button_canvas, text="Blackjack", image=blackJack_photo, compound="top", command=open_blackJack, bg='#000', fg='white', font=('Arial', 14))
    tt_button.image = blackJack_photo  # Keep a reference to avoid garbage collection
    tt_button.pack(side='left', padx=(50,0))

    window.mainloop()