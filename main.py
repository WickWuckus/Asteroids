import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	dt = 0
	clock = pygame.time.Clock()

	asteroids = pygame.sprite.Group()
	
	updatables = pygame.sprite.Group()
	
	drawables = pygame.sprite.Group()

	shots = pygame.sprite.Group()

	AsteroidField.containers = (updatables,)

	Asteroid.containers = (asteroids, updatables, drawables)
	
	Player.containers = (updatables, drawables,)

	Shot.containers = (shots, updatables, drawables,)

	asteroid_field = AsteroidField()

	updatables.add(asteroid_field)
	
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		updatables.update(dt)
				
		
		for asteroid in asteroids:
			if asteroid.collision(player):
				print("Game over!")
				return pygame.QUIT
			
			for shot in shots:
				if asteroid.collision(shot):
					shot.kill()
					asteroid.split()
		
			
		screen.fill("black")
		
		for drawable in drawables:
			drawable.draw(screen)

		

		pygame.display.flip()
		
		dt = clock.tick(60) / 1000
		
		
if __name__== "__main__":
	main()