import pygame

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
        self.val = 3

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
        
        self.rect = (self.x, self.y, self.width, self.height)
        

def redrawWindow(win, player):
    win.fill((255,255,255))
    player.draw(win)
    pygame.display.update()

def main():
    run = True

    p = Player(50, 50, 100, 100, (180,200,130))

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rum = False
                pygame.quit()
        
        p.move()
        redrawWindow(win, p)

main()
