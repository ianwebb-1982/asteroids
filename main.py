import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
from player import Player
from circleshape import CircleShape
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys
from shot import Shot


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print(f"Starting Asteroids with pygame version {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    clock = pygame.time.Clock()
    dt = 0.0

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH /2, SCREEN_HEIGHT /2)
    asteroid_field = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        
        updatable.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()

        for draw in drawable:
            draw.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        #print(dt)




if __name__ == "__main__":
    main()
