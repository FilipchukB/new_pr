import pygame


class Level_menu():
    def __init__(self, screen):
        #super().__
        self.screen = screen
        self.image_fon = pygame.image.load('menu_new.jpg')
        self.rect = (0, 0)
        # self.image_level1 = pygame.image.load()

    def blitme(self):
        self.screen.blit(self.image_fon, (0, 0))
