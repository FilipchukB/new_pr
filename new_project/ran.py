import pygame
import sys
from settings import Settings
from st_menu import Menu
from button0 import Button
from level_one import Level1
from level_two import Level2
from level_tre import Level3
from level4 import Level4
from level5 import Level5


def terminate():
    # pygame.QUIT()
    sys.exit()


def run_game():
    pygame.init()
    ol_settings = Settings()
    screen = pygame.display.set_mode((ol_settings.screen_width, ol_settings.screen_height))
    pygame.display.set_caption('Identiphishing')
    menu = Menu(screen)
    but = Button(screen, ol_settings)
    pygame.mixer.music.load('Sounds/back.mp3')
    pygame.mixer.music.play()
    level1 = Level1(screen, ol_settings)
    level2 = Level2(screen, ol_settings)
    level3 = Level3(screen, ol_settings)
    level4 = Level4(screen, ol_settings)
    level5 = Level5(screen, ol_settings)

    # button = Button(100, 100)

    while True:

        if ol_settings.current_level == 0:
            print('00000P')
            menu.blitme()
            but.dl()
            but.draw()
        elif ol_settings.current_level == 1:
            level1.show()
            level1.pr_next()
        elif ol_settings.current_level == 2:
            level2.show()
            level2.pr_next()
        elif ol_settings.current_level == 3:
            level3.show()
            level3.pr_next()
        elif ol_settings.current_level == 4:
            level4.show()
            level4.pr_next()
        elif ol_settings.current_level == 5:
            level5.show()
            level5.pr_next()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            # if event.type == pygame.KEYDOWN:
            #     ol_settings.current_level += 1
        #
        pygame.display.flip()
        # print(pygame.mouse.get_pos())


run_game()
