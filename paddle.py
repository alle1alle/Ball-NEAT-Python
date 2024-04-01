import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, keys, window_width):
        # Check if left arrow is pressed and move paddle left
        if keys[pygame.K_LEFT]:
            self.x -= 0.5
        # Check and move the right one
        if keys[pygame.K_RIGHT]:
            self.x += 0.5    
        
        self.x = max(0, min(self.x, window_width - self.width))

    def move_right(self):
        self.x += 0.5

    def move_left(self):
        self.x -= 0.5

    def draw(self, window, color):
        pygame.draw.rect(window, color, (self.x, self.y, self.width, self.height))




