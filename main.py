import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    asteroid_field = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        updatable.update(dt)

        for sprite in drawable:
            sprite.draw(screen)

        for sprite in asteroids:
            hit = sprite.collides_with(player)
            if hit == True:
                log_event("player_hit")
                print("Game Over")
                sys.exit()

        pygame.display.flip()  
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
