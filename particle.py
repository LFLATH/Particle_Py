import pygame
import math
class Particle():
    def __init__(self, mass, cords, velocity, acceleration, screen):
        self.mass = mass
        self.cords = cords
        self.screen = screen
        self.velocity = velocity
        self.acceleration = acceleration
    def get_pos(self):
        return (self.cords[0], self.cords[1], self.mass)
    def spawn(self):
        pygame.draw.circle(self.screen,(255,255,255),(self.cords[0], self.cords[1]), self.mass)
    def move(self):
        self.velocity[0] = self.velocity[0] + self.acceleration[0] * (0.16666666)#0.166 is 1/60 or dt
        self.velocity[1] = self.velocity[1] + self.acceleration[1] * (0.16666666)
        self.cords[0] = self.cords[0] + self.velocity[0] * 0.16666666
        self.cords[1] = self.cords[1] +  self.velocity[1] * 0.16666666
        self.hit_edge()
    def hit_edge(self):
        boundx, boundy = self.screen.get_size()
        if self.cords[0] + self.mass >= boundx or self.cords[0] - self.mass <= 0:
            self.velocity[0] = self.velocity[0] * -1
        if self.cords[1] + self.mass >= boundy or self.cords[1] - self.mass <= 5:
            self.velocity[1] = self.velocity[1] * -1


    def collide(self, particles):
        for particle in particles:
            particle = particle.get_pos()
            if  [int(particle[0]), int(particle[1])] == [int(self.cords[0]), int(self.cords[1])]:
                continue
        
            elif math.dist([particle[0], particle[1]], [self.cords[0], self.cords[1]]) <= self.mass + particle[2]:
                print(math.dist([particle[0], particle[1]], [self.cords[0], self.cords[1]]))
                self.velocity[1] = self.velocity[1] * -1
                self.velocity[0] = self.velocity[0] * -1
                
               

