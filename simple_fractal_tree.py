import pygame
from math import cos, sin, radians

WIDTH, HEIGHT = 800, 800

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fractal Tree")

def drawTree(x1, y1, angle, depth):
    fork_angle = 30
    base_len = 30
    if depth > 0: 
        x2 = x1 + int(cos(radians(angle)) * depth * base_len)
        y2 = y1 + int(sin(radians(angle)) * depth * base_len)
        pygame.draw.line(screen, (0, 255, 0), (x1,y1), (x2,y2), 2)
        pygame.time.delay(200)
        pygame.display.update()
        drawTree(x2, y2, angle - fork_angle, depth-1)
        drawTree(x2, y2, angle + fork_angle, depth-1)

running = True
while running:

    screen.fill((0, 0, 0)) #color black

    drawTree(WIDTH / 2, HEIGHT - 100, -90, 4)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

