from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius >= ASTEROID_MIN_RADIUS:
            log_event("asteroid_split")
            new_direction = random.uniform(20, 50)
            new1 = self.velocity.rotate(new_direction)
            new2 = self.velocity.rotate(-new_direction)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid1 = Asteroid(self.position.x, self.position.y, new_radius)
            roid1.velocity = new1 * 1.2
            roid2 = Asteroid(self.position.x, self.position.y, new_radius)
            roid2.velocity = new2 * 1.2
        else:
            return