import pygame 

from settings import Settings
from ship import Ship
import game_functions as gf

#function: run game
def run_game():

	#construct
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))

	#windows size
	#screen = pygame.display.set_mode((1200,800))

	ship = Ship(ai_settings, screen)

	#title
	pygame.display.set_caption("Alien Invasion")

	#give color to bg_color
	#bg_color = (230,230,230)

	while True:

		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)

		# for event in pygame.event.get():
		# 	if event.type == pygame.QUIT:
		# 		sys.exit()

		#redraw the screen during each pass thought the loop
		screen.fill(ai_settings.bg_color)
		ship.blitme()

		# Make the most recently drawn screen visible
		pygame.display.flip()

run_game()