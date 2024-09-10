from tkinter import *
import threading
import subprocess
from client import open_client

def start_client(email):
    rules_window.destroy()
    # Run open_client in a separate thread to avoid blocking the UI
    threading.Thread(target=open_client, args=(email,)).start()

def open_gamerules(email):
    global rules_window
    rules_window = Tk()
    rules_window.title('Game Rules')
    rules_window.state('zoomed')
    rules_window.configure(bg='#35654d')

    label = Label(rules_window, text='Game Rules', bg='#35654d', fg='#fff', font=('Microsoft YaHei UI Light', 18, 'bold'))
    label.pack(pady=(20))

    txt = ("We accept at most 5 players to start the game.\n\n"
           "There are 52 cards in the deck. A to K of Spade, Heart, Diamond, and Club.\n\n"
           "Every player gets 2 cards and has the right to draw one extra card.\n\n"
           "The value of the card ranks A=1, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=10, J=10, Q=10, and K=10.\n\n"
           "The value of the card depends on the combination of the cards together.\n\n"
           "If the score is higher than 10, you must ignore the 2nd digit. For example, 15=5, 14=4, 10=0, 20=0, 33=3.\n\n"
           "To win the game, you must get the higher score.\n\n"
           "In case the score is equal in value, then the hand with fewer cards is the winner.\n\n"
           "If the score and number of cards are equal, the value of the card decides the winner.\n\n"
           "The orders are A, K, Q, J, 10,…2.\n\n"
           "If the value is the same, look at the suits of the highest value of the card. The order is Spade, Heart, Diamond, and Club.\n\n"
           "For example: Deck (5,5,7) VS deck (3,4), deck (3,4) is the winner.\n\n"
           "For example: Deck (Q,6) VS deck (2,4), deck (Q,6) is the winner.\n\n"
           "For example: Deck (Heart of 7, Club of 2) VS deck (Diamond of 7, Spade of 2), the first deck is the winner.")

    # Create a frame to contain the text and scrollbar
    frame = Frame(rules_window, bg='#35654d')
    frame.pack(pady=(10, 20), padx=20, fill=BOTH, expand=True)

    # Create a scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Create a text widget with scrollbar
    rules_text = Text(frame, wrap=WORD, bg='#35654d', fg='#fff', font=('Microsoft YaHei UI Light', 10), yscrollcommand=scrollbar.set)
    rules_text.insert(INSERT, txt)
    rules_text.config(state=DISABLED)  # Make the text widget read-only
    rules_text.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar.config(command=rules_text.yview)

    # OK button
    Button(rules_window, border=1, text='OK', padx=10, bg='#fff', fg='#35654d', font=('Microsoft YaHei UI Light', 12), command=lambda: start_client(email)).pack(pady=20)

    rules_window.mainloop()
