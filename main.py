import pygame
from logger import log_state
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player


def main():
    print(f"""Starting Asteroids with pygame version: {pygame.version.ver} \n
        Screen width: {SCREEN_WIDTH} \n
        Screen height: {SCREEN_HEIGHT}

            """)
    pygame.init()
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
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
        for thing in updateable:
            thing.update(dt)


if __name__ == "__main__":
    main()
