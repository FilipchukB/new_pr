import pygame
from levels_menu import Level_menu
from settings import Settings

# trans = pygame.transform.scale('play_.jpg', (1200, 800))


class Menu:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('menu_new.jpg').convert_alpha()
        self.image = pygame.transform.scale(self.image, (1200, 800))
        self.rect = (0, 0)
        self.screens = screen
        self.lev = pygame.image.load('question.jpg')
        self.lev = pygame.transform.scale(self.lev, (50, 50))
        # self.image2 = pygame.image.load('1.jpg').convert_alpha()
        # self.rect2 = (280, 40)

    def level_menu(self):
        set = Settings()
        mouse = pygame.mouse.get_pos()
        clik = pygame.mouse.get_pressed()
        l_m = Level_menu(self.screen)
        print(mouse[0], mouse[1])
        if 950 > mouse[0] > 900 and 530 > mouse[1] > 480:
            if clik[0] == 1:
                print(1)
                self.settings.current_level = 100

             #   l_m.blitme()

    def blitme(self):
        self.screen.blit(self.image, self.rect)
       # self.screen.blit(self.lev, (900, 480))
        # self.screens.blit(self.image2, self.rect2)
