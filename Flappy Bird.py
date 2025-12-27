import pygame
from sys import exit
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Flappy Bird')
clock = pygame.time.Clock()

# Player
player = pygame.Rect(400, 1, 34, 24)
player_vel = 0
gravity = 0.5

# Pipes
pipe_x = 800
pipe_x_2 = 1200
pipe_speed = 4
pipe_width = 50
gap_size = 150
gap_y = 200
gap_y_2 = random.randint(100, 450)

pipe_top = pygame.Rect(pipe_x, 0, pipe_width, gap_y)
pipe_bottom = pygame.Rect(pipe_x, gap_y + gap_size, pipe_width, 600 - (gap_y + gap_size))

pipe_top_2 = pygame.Rect(pipe_x_2, 0, pipe_width, gap_y_2)
pipe_bottom_2 = pygame.Rect(pipe_x_2, gap_y_2 + gap_size, pipe_width, 600 - (gap_y_2 + gap_size))

# Game state
dead = False
score = 0
scored = False
scored_2 = False

font = pygame.font.Font(None, 40)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if dead:
                player.y = 1
                player_vel = 0

                pipe_x = 800
                pipe_x_2 = 1200
                gap_y = random.randint(100, 450)
                gap_y_2 = random.randint(100, 450)

                pipe_top.height = gap_y
                pipe_bottom.y = gap_y + gap_size
                pipe_bottom.height = 600 - (gap_y + gap_size)

                pipe_top_2.height = gap_y_2
                pipe_bottom_2.y = gap_y_2 + gap_size
                pipe_bottom_2.height = 600 - (gap_y_2 + gap_size)

                score = 0
                scored = False
                scored_2 = False
                dead = False
            else:
                player_vel = -10

    if not dead:
        # ---- PIPE RESPAWN ----
        if pipe_x < -pipe_width:
            pipe_x = 800
            gap_y = random.randint(100, 450)

            pipe_top.height = gap_y
            pipe_bottom.y = gap_y + gap_size
            pipe_bottom.height = 600 - (gap_y + gap_size)

            scored = False

        if pipe_x_2 < -pipe_width:
            pipe_x_2 = 800
            gap_y_2 = random.randint(100, 450)

            pipe_top_2.height = gap_y_2
            pipe_bottom_2.y = gap_y_2 + gap_size
            pipe_bottom_2.height = 600 - (gap_y_2 + gap_size)

            scored_2 = False

        # ---- MOVE PIPES ----
        pipe_x -= pipe_speed
        pipe_x_2 -= pipe_speed

        pipe_top.x = pipe_x
        pipe_bottom.x = pipe_x
        pipe_top_2.x = pipe_x_2
        pipe_bottom_2.x = pipe_x_2

        # ---- SCORE ----
        if not scored and pipe_top.centerx < player.centerx:
            score += 1
            scored = True

        if not scored_2 and pipe_top_2.centerx < player.centerx:
            score += 1
            scored_2 = True

        # ---- PLAYER PHYSICS ----
        player_vel += gravity
        player.y += int(player_vel)

        # ---- COLLISIONS ----
        if player.y <= 0 or player.y >= 600 - player.height or player.colliderect(pipe_top) or player.colliderect(pipe_bottom)or player.colliderect(pipe_top_2) or player.colliderect(pipe_bottom_2):
            dead = True

    # ---- DRAW ----
    screen.fill('black')
    pygame.draw.rect(screen, (150, 150, 150), player)
    pygame.draw.rect(screen, 'green', pipe_top)
    pygame.draw.rect(screen, 'green', pipe_bottom)
    pygame.draw.rect(screen, 'green', pipe_top_2)
    pygame.draw.rect(screen, 'green', pipe_bottom_2)

    score_surface = font.render(str(score), True, 'white')
    screen.blit(score_surface, (400, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
exit()