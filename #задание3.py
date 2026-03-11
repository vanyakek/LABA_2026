#задание3
import pygame
import math
import random
from pygame.draw import *

pygame.init()

FPS = 30
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")

SUN_COLOR = (255, 255, 0)
SKY_TOP = (255, 245, 220)
SKY_BOTTOM = (255, 200, 150)

COLOR_FAR = (255, 220, 200)
COLOR_MID = (255, 180, 50)
COLOR_NEAR = (230, 110, 70)

for y in range(HEIGHT):
    r = SKY_TOP[0] + (SKY_BOTTOM[0] - SKY_TOP[0]) * y // HEIGHT
    g = SKY_TOP[1] + (SKY_BOTTOM[1] - SKY_TOP[1]) * y // HEIGHT
    b = SKY_TOP[2] + (SKY_BOTTOM[2] - SKY_TOP[2]) * y // HEIGHT
    pygame.draw.line(screen, (r, g, b), (0, y), (WIDTH, y))

sun_x = WIDTH // 2
sun_y = 170
sun_radius = 45
circle(screen, SUN_COLOR, (sun_x, sun_y), sun_radius)

def draw_mountain_layer(top_points, color):
    poly = top_points + [(WIDTH, HEIGHT), (0, HEIGHT)]
    polygon(screen, color, poly)

top_far = []
for x in range(0, WIDTH + 1, 10):
    y = 200 + 35 * abs(math.sin(x / 70)) + 15 * math.sin(x / 120)
    top_far.append((x, y))
draw_mountain_layer(top_far, COLOR_FAR)

top_mid = []
for x in range(0, WIDTH + 1, 8):
    y = 270 + 50 * abs(math.sin(x / 60)) + 20 * math.sin(x / 100 + 1)
    top_mid.append((x, y))
draw_mountain_layer(top_mid, COLOR_MID)

top_front = []
for x in range(0, WIDTH + 1, 6):
    y = 340 + 70 * abs(math.sin(x / 50)) + 25 * math.sin(x / 80 + 2)
    top_front.append((x, y))
draw_mountain_layer(top_front, COLOR_NEAR)

def draw_bird_up(x, y, size=18, thickness=4, spread_factor=1.5):

    height = size
    spread = size * spread_factor
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x - spread, y - height), thickness)
    
    pygame.draw.line(screen, (0, 0, 0), (x, y), (x + spread, y - height), thickness)

bird_positions = []
for _ in range(8):
    x = random.randint(80, WIDTH - 80)
    y = random.randint(60, 280)  
    bird_positions.append((x, y))

for (x, y) in bird_positions:
    draw_bird_up(x, y, size=18, thickness=4, spread_factor=1.5)

pygame.display.update()

clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()