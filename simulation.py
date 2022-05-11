import pygame
import sys
import random
from particle import Particle
pygame.init()

clock = pygame.time.Clock()
black = [0,0,0]
screen = pygame.display.set_mode((500,500))
particles = []
for i in range(0,4):
    particle = Particle(20,[0 + random.randint(40, 400), 0 + random.randint(40, 400)],[random.randint(10,11), random.randint(-5, 5)],[0,0], screen)
    particles.append(particle)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(black)
    for particle in particles:
        particle.move()
        particle.collide(particles)
        particle.spawn()

    clock.tick(120)

    pygame.display.update()
