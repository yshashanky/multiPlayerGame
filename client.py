import pygame
from network import Network

width = 500
height = 500
win = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Client")

clientNumber = 0

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 0.1

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        w, h = pygame.display.get_surface().get_size()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            if self.x <= 0:
                self.x = self.x
            else:
                self.x -= self.val

        if keys[pygame.K_RIGHT]:
            if self.x >= (w-self.width):
                self.x = self.x
            else:
                self.x += self.val
        
        if keys[pygame.K_UP]:
            if self.y <= 0:
                self.y = self.y
            else:
                self.y -= self.val

        if keys[pygame.K_DOWN]:
            if self.y >= (h-self.height):
                self.y = self.y
            else:
                self.y += self.val
        
        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])

def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])

def redrawWindow(win, player, player2):
    win.fill((255,255,255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

def main():
    run = True

    n = Network()
    startPos = read_pos(n.getPos())
    p = Player(startPos[0], startPos[1], 100, 100, (180,200,130))
    p2 = Player(0, 0, 100, 100, (180,200,0))

    while run:
        p2pos = read_pos(n.send(make_pos((p.x, p.y))))
        p2.x = p2pos[0]
        p2.y = p2pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rum = False
                pygame.quit()
        
        p.move()
        redrawWindow(win, p, p2)

main()
