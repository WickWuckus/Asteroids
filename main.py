import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()

	asteroids = pygame.sprite.Group()
	
	updatables = pygame.sprite.Group()
	
	drawables = pygame.sprite.Group()

	AsteroidField.containers = (updatables,)

	Asteroid.containers = (asteroids, updatables, drawables)
	
	Player.containers = (updatables, drawables)

	asteroid_field = AsteroidField()

	updatables.add(asteroid_field)
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
				
		screen.fill("black")
		
		updatables.update(dt)
		
		for drawable in drawables:
			drawable.draw(screen)
		
		pygame.display.flip()
		
		dt = clock.tick(60) / 1000
		
		
if __name__== "__main__":
	main()