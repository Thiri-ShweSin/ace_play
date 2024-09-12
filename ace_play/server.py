import socket
import threading
import time
from game import Game
from player import Player
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error

clients = []
game = Game()

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

def handle(client):
    connection = connect_db()
    cursor = connection.cursor()
    try:
        username = client.recv(1024).decode('utf-8')
        player = Player(username)
        game.players.append(player)

        while True:
            request = client.recv(1024).decode("utf-8")
            if request == "deal_cards":
                for i in range(2):
                    player.draw(game.deck)

                # Prepare the card details to send to the client
                card_details = f"{username}>>>"
                for card in player.hand:
                    cursor.execute("SELECT image_path FROM card_images WHERE card_rank=%s AND suit=%s", (card.value, card.suit))
                    image_path = cursor.fetchone()[0]
                    card_details += f"{image_path}-"

                client.send(card_details.encode('utf-8'))
                time.sleep(1)
                client.send("One more card?(y/n)".encode('utf-8'))

                req = client.recv(1024).decode('utf-8')
                if req.lower() == 'y':
                    player.draw(game.deck)
                    new_card = player.hand[-1]
                    cursor.execute("SELECT image_path FROM card_images WHERE card_rank=%s AND suit=%s", (new_card.value, new_card.suit))
                    new_image_path = cursor.fetchone()[0]
                    card_details += f"{new_image_path}"  # Append with a newline

                    new_card_details = f"Your new card is: {new_image_path}"
                    client.send(new_card_details.encode('utf-8'))
                card_details += "\n"
                # Broadcast the updated card details
                barrier.wait()
                time.sleep(1)
                broadcast(card_details, client)
                break
    except Exception as e:
        print(f"Handle Error: {e}")
    finally:
        if client == clients[-1]:
            game.playerMaxCard()
            winner_announcement = game.findWinner()
            print(winner_announcement)
            time.sleep(1)
            broadcastAll(winner_announcement)
            closing = client.recv(1024).decode('utf-8')
            if closing == "closing":
                client.close()
            cursor.close()
            connection.close()

def broadcast(msg,client_socket):
        for client in clients:
            if client != client_socket:
                try:
                    client.send(msg.encode("utf-8"))
                    time.sleep(1)
                except Exception as e:
                    print(f"Error: {e}")

def broadcastAll(msg):
    for client in clients:
        try:
            client.send(msg.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")

def play():
    global playerCount
    playerCount = int(input("How many players (up to 5) to start a game?"))
    if playerCount < 0 or playerCount > 5:
        print("We accept at most 5 players. Please try again.")
        play()

def run_server():
    try:
        # Create socket object
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to a public host, and a port
        server.bind(('0.0.0.0', 8000))
        # Become a server socket, listen for connections
        server.listen()
        print("Server is listening")

        play()
        global barrier
        barrier = threading.Barrier(playerCount)
        while True:
            client, addr = server.accept() # Accept connection
            clients.append(client)  #Upon accepting a new connection, the client socket is added to the clients list.
            print(f"Connection from {addr} has been established.")

            if len(clients)!= playerCount:
                client.send("Waiting for the other clients...".encode('utf-8'))
            else:
                broadcastAll("Start")
            # Each client connection is handled by a separate thread, which calls the handle function for that specific client.
            thread = threading.Thread(target=handle, args=(client,))    
            thread.start()

    except Exception as e:
        print(f"Err: {e}")
    finally:
        server.close()

if __name__ == "__main__":
    run_server()