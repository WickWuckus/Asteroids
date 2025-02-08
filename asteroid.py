import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
            
    def spawn(self, radius, position, velocity):
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        new_velocity_rgt = self.velocity.rotate(random_angle) * 1.2
        new_velocity_lft = self.velocity.rotate(-random_angle) * 1.2
    
        new_radius = self.radius - ASTEROID_MIN_RADIUS 
    
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity_lft
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = new_velocity_rgt
    
        
        
