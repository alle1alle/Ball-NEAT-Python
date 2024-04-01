import pygame

class Ball:
    def __init__(self, x, y, radius, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed_x
        self.speed_y = speed_y
        
    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        
    def bounce_off_walls(self, window_width):
        if self.x <= 0 or self.x >= window_width:
            self.speed_x *= -1
        elif self.y <= 0:
            self.speed_y *= -1    

    def bounce_off_bar(self, bar_x, bar_width, bar_y):
        if self.y + self.radius >= bar_y and self.x >= bar_x and self.x <= bar_x + bar_width:
            if self.y - self.speed_y <= bar_y:  # Check if the ball is above the top edge of the paddle
                self.speed_y *= -1  # Reverse the vertical direction of the ball
                return True  # Indicate that the ball bounced off the bar
        return False  # Indicate that the ball did not bounce off the bar

    def draw(self, window, color):
        pygame.draw.circle(window, color, (self.x, self.y), self.radius)
   
        

    







