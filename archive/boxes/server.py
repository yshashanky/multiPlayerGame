import socket
import pickle
from _thread import *
import sys
from player import Player

server = "192.168.1.42"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

global currentPlayer
currentPlayer = 0

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started...")

players = [Player(0,0,50,50,(255,0,0)), Player(100,100,50,50,(0,0,255))]

def threader_client(conn, player):
    global currentPlayer

    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                currentPlayer -= 1
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print(f"Received: {reply}")
                print(f"Sending: {reply}")
            
            conn.sendall(pickle.dumps(reply))

        except:
            break
    
    print("Lost connection")
    if player == 1:
        currentPlayer -= 1
    if player == 0 and currentPlayer == 1:
        currentPlayer -= 1
    if player == 0 and currentPlayer == 2:
        currentPlayer -= 2
    
    conn.close()

while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threader_client, (conn, currentPlayer ))
    currentPlayer +=1