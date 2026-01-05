import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver} \n
        Screen width: {SCREEN_WIDTH} \n
        Screen height: {SCREEN_HEIGHT}

            """)
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    AsteroidField1 = AsteroidField()
    dt = 0
    q = 1
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
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


if __name__ == "__main__":
    main()
