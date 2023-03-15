import pygame
from network import Network
from player import Player

width = 500
height = 500
win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Client")

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True
    n = Network()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rum = False
                pygame.quit()
        
        p.move()
        redrawWindow(win, p, p2)

main()
