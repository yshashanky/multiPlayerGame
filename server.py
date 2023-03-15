import socket
from _thread import *
import sys

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

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

pos = [(0,0), (100,100)]

def threader_client(conn, player):
    global currentPlayer

    conn.send(str.encode(make_pos(pos[player])))
    reply = ""
    while True:
        try:
            data = read_pos(conn.recv(2048).decode("utf-8"))
            pos[player] = data

            if not data:
                print("Disconnected")
                currentPlayer -= 1
                break
            else:
                if player == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]

                print(f"Received: {reply}")
                print(f"Sending: {reply}")
            
            conn.sendall(str.encode(make_pos(reply)))

        except:
            break
    
    print("Lost connection")
    currentPlayer -= 1
    conn.close()

while True:
    conn, addr = s.accept()
    print(f"Connected to: {addr}")

    start_new_thread(threader_client, (conn, currentPlayer ))
    currentPlayer +=1