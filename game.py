import pygame
import sys
from ball import Ball
from paddle import Paddle
from pygame.font import Font
import random
import neat
import os
import time

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Font
font = pygame.font.Font(None, 36)

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def draw_score(window, score):
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

def update_display():
    pygame.display.update()

def render_text(window, text, pos, color):
    font_obj = Font(None, 20)
    text_surface = font_obj.render(text, True, color)
    window.blit(text_surface, pos)

def main(genomes, config):
    start_time = time.time()  # Track the start time
    for genome_id, genome in genomes:
        genome.fitness = 0

        net = neat.nn.FeedForwardNetwork.create(genome, config)
        window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Ball Game")
        score = 0

        random_x_speed = random.uniform(-0.25, 0.25)
        ball = Ball(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, 10, random_x_speed, 0.25)
        paddle = Paddle((WINDOW_WIDTH - 150) // 2, WINDOW_HEIGHT - 50, 150, 20)

        while True:
            handle_events()
            keys = pygame.key.get_pressed()
            paddle.move(keys, WINDOW_WIDTH)

            output = net.activate((paddle.x, ball.x, WINDOW_HEIGHT - ball.y))

            if output[0] > 0.5:
                paddle.move_right()
            else:
                paddle.move_left()

            ball.move()
            ball.bounce_off_walls(WINDOW_WIDTH)
            if ball.bounce_off_bar(paddle.x, paddle.width, paddle.y):
                score += 1
                genome.fitness += 1
                

            if ball.y >= WINDOW_HEIGHT:
                score = 0
                break

            # Check elapsed time and end the game if it exceeds 2 minutes (120 seconds)
            if time.time() - start_time > 120:
                break

            window.fill(BLACK)
            paddle.draw(window, WHITE)
            ball.draw(window, RED)
            draw_score(window, score)
            update_display()

def run_neat(config_path, generations):
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)
    p = neat.Population(config)

    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)

    for _ in range(generations):
        p.run(main, 1)  # Run NEAT for one generation

    
    

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run_neat(config_path, 20)






       

 


        

        
        







