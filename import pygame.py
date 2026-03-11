import pygame
import sys

pygame.init()

screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Задание 1")

YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    face_center = (200, 200)
    face_radius = 150
    pygame.draw.circle(screen, YELLOW, face_center, face_radius)
    pygame.draw.circle(screen, BLACK, face_center, face_radius, 2)

    left_eye_center = (130, 150)
    left_eye_radius = 25
    pygame.draw.circle(screen, RED, left_eye_center, left_eye_radius)
    pygame.draw.circle(screen, BLACK, left_eye_center, left_eye_radius, 2)
    pygame.draw.circle(screen, BLACK, (120, 140), 8)

    right_eye_center = (270, 150)
    right_eye_radius = 25
    pygame.draw.circle(screen, RED, right_eye_center, right_eye_radius)
    pygame.draw.circle(screen, BLACK, right_eye_center, right_eye_radius, 2)
    pygame.draw.circle(screen, BLACK, (280, 140), 8)

    pygame.draw.line(screen, BLACK, (80, 100), (150, 120), 20)
    pygame.draw.line(screen, BLACK, (320, 100), (250, 120), 20)

    pygame.draw.arc(screen, BLACK, pygame.Rect(130, 200, 140, 80), 3.5, 5.8, 4)


    pygame.display.flip()

pygame.quit()
sys.exit()