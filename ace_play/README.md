# ACE PLAY
This project aims to create a Python-based multiplayer card game using client-server architecture. It manages card distribution, rule enforcement, and winner determination with a unique scoring system. A Tkinter-based GUI displays player hands and scores, while socket programming ensures real-time gameplay. A MySQL database stores player info and game results. The system is scalable for future updates, including AI opponents and new game modes

# HOW TO RUN
To run the game, one pc must run server.py first. The server computer should have the 'ace_play' mysql database with it's respective tables.
Tables structure are as follow:
-> card_images (id INT AUTO_INCREMENT PRIMARY KEY, card_rank VARCHAR(10), suit VARCHAR(10), image_path VARCHAR(255))
-> users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(30), email VARCHAR(50), password VARCHAR(50))
The server will then ask for the number of players to start the game.

According to the number of clients requested, each client computer should run main_window.py. Then the player may either login or sign up to start the game.

# About the game
We accept at most 5 players to start the game.

There are 52 cards in the deck. A to K of Spade, Heart, Diamond and Club.

Rules of the game,

- Every player got 2 cards and has the right to draw one extra card.

- The value of the card ranks A=1, 2=2, 3=3, 4=4, 5=5, 6=6, 7=7, 8=8, 9=9, 10=10, J=10, Q=10 and K=10.

- The value of the card depends on the combination of the cards together. If the score is higher than 10, you must ignore the 2nd digit. For example, 15= 5, 14=4, 10=0, 20=0, 33=3.

- To win the game, you must get the higher score. In case the score is equal in value, then the hand who gets less card is the winner.

- If the score and number of cards are equal, the value of the card decides the winner. The orders are A, K, Q, J, 10,….2. If the value is the same, look at the suits of the highest value of the card. The orders is Spade, Heart, Diamond and Club.

=> For example: Deck (5,5,7) VS deck (3,4), deck (3,4) is the winner.

=> For example: Deck (Q,6) VS deck (2,4), deck (Q,6) is the winner.

=> For example: Deck (Heart of 7, Club of 2) VS deck (Diamond of 7, Spade of 2), the first deck is the winner.