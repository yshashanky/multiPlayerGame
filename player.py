import pygame

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.val = 1

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