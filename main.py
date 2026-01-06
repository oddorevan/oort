import pygame
from logger import log_state, log_event
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver} \n
        Screen width: {SCREEN_WIDTH} \n
        Screen height: {SCREEN_HEIGHT}

            """)
    pygame.init()
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    AsteroidField1 = AsteroidField()  # noqa: F841
    dt = 0
    q = 1
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)  # noqa: F841
    while q > 0:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        pygame.display.flip()
        for thing in updatable:
            thing.update(dt)
        for roid in asteroids:
            if player1.collides_with(roid):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()
            for bullet in shots:
                if roid.collides_with(bullet):
                    roid.kill()
                    bullet.kill()
                    log_event("asteroid_shot")
                else:
                    continue
if __name__ == "__main__":
    main()
