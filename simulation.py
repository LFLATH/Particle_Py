import pygame
import sys
import random
from particle import Particle
pygame.init()

clock = pygame.time.Clock()
black = [0,0,0]
screen = pygame.display.set_mode((500,500))
particles = []
for i in range(0,11):
    particle = Particle(10,[0 + random.randint(0, 400), 0 + random.randint(0, 400)],[random.randint(1,2), random.randint(-1, 1)], screen)
    particles.append(particle)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(black)
    for particle in particles:
        particle.hit_edge()
        particle.move()
        particle.spawn()
    pygame.display.update()
