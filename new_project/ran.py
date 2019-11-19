import pygame
import sys
from settings import Settings
from st_menu import Menu
from button0 import Button
from level_one import Level1


def terminate():
    pygame.QUIT()
    sys.exit()


def run_game():
    pygame.init()
    ol_settings = Settings()
    screen = pygame.display.set_mode((ol_settings.screen_width, ol_settings.screen_height))
    pygame.display.set_caption('Identiphishing')
    menu = Menu(screen)
    but = Button(screen)
    pygame.mixer.music.load('Sounds/back.mp3')
    pygame.mixer.music.play()
    level1 = Level1(screen)

    # button = Button(100, 100)

    while True:

        if ol_settings.current_level == 0:
            print('00000P')
            menu.blitme()
            but.dl()
            but.draw()
        if ol_settings.current_level == 1:
            level1.show()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN:
                ol_settings.current_level += 1
            print(1223)
        pygame.display.flip()
        print(pygame.mouse.get_pos())


run_game()
