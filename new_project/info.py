import pygame
from settings import Settings


class Info:
    def __init__(self, screen, settings):
        self.settings = settings
        self.screen = screen
        self.fon = pygame.image.load('fon2.jpg').convert_alpha()
       # self.c_1 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_2 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_3 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_4 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_5 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_6 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
      #  self.c_7 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
        #self.c_8 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
       # self.c_9 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
      #  self.c_10 = pygame.transform.scale(pygame.image.load('comp.jpg').convert_alpha(), (200, 200))
        self.c_not = pygame.transform.scale(pygame.image.load('comp_not.jpg').convert_alpha(), (200, 200))
        self.pl1 = pygame.image.load('pl1.jpg')
        self.pl2 = pygame.image.load('pl2.jpg')

    def info_ansver(self):
        print(pygame.mouse.get_pos())
        mouse = pygame.mouse.get_pos()
        if self.settings.current_level == 11:
            if self.settings.histori_1 == 0:  # L1
                self.screen.blit(self.c_not, (70, 290))
                if 100 < mouse[0] < 300 and 100 < mouse[1] < 300:
                    self.screen.blit(self.pl1, (0, 0))
                    print('o0p')
            if self.settings.histori_2 == 0:  # L2
                self.screen.blit(self.c_not, (300, 290))
            if self.settings.histori_3 == 0:  # L3
                self.screen.blit(self.c_not, (550, 290))
            if self.settings.histori_4 == 0:  # L4
                self.screen.blit(self.c_not, (770, 290))
            if self.settings.histori_5 == 0:  # L5
                self.screen.blit(self.c_not, (950, 290))
            if self.settings.histori_6 == 0:  # L6
                self.screen.blit(self.c_not, (70, 590))
            if self.settings.histori_7 == 0:  # L7
                self.screen.blit(self.c_not, (300, 590))
            if self.settings.histori_8 == 0:  # L8
                self.screen.blit(self.c_not, (550, 590))
            if self.settings.histori_9 == 0:  # L9
                self.screen.blit(self.c_not, (770, 590))
            if self.settings.histori_10 == 0:  # L10
                self.screen.blit(self.c_not, (1000, 590))

    def show_info_answer(self):
        print(pygame.mouse.get_pos())
        mouse = pygame.mouse.get_pos()
        if self.settings.current_level == 11:
            if 70 < mouse[0] < 260 and 290 < mouse[1] < 460:
                self.screen.blit(self.pl1, (0, 0))
            if 320 < mouse[0] < 470 and 315 < mouse[1] < 470:
                self.screen.blit(self.pl2, (0, 0))

    def blitme(self):
        self.screen.blit(self.fon, (0, 0))
#        self.screen.blit(self.c_1, (100, 100))
 #       self.screen.blit(self.c_2, (300, 100))
        #self.screen.blit(self.c_3, (500, 100))
       # self.screen.blit(self.c_4, (700, 100))
      #  self.screen.blit(self.c_5, (900, 100))
        #self.screen.blit(self.c_6, (100, 500))
       # self.screen.blit(self.c_7, (300, 500))
      #  self.screen.blit(self.c_8, (500, 500))
     #   self.screen.blit(self.c_9, (700, 500))
        #self.screen.blit(self.c_10, (900, 500))
