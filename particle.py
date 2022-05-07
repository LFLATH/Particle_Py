import pygame
class Particle():
    def __init__(self, mass, cords, velocity, screen):
        self.mass = mass
        self.cords = cords
        self.screen = screen
        self.velocity = velocity
    def spawn(self):
        pygame.draw.circle(self.screen,(255,255,255),(self.cords[0], self.cords[1]), self.mass)
    def move(self):
        self.cords[0] +=  self.velocity[0]
        self.cords[1] += self.velocity[1]
    def hit_edge(self):
        boundx, boundy = self.screen.get_size()
        if self.cords[0] >= boundx - 10 or self.cords[0] <= self.mass:
            self.velocity[0] = self.velocity[0] * -1
        if self.cords[1] >= boundy - 10 or self.cords[1] <= self.mass:
            self.velocity[1] = self.velocity[1] * -1