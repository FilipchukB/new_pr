import pygame
import sys
from settings import Settings


class Level3:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.question = pygame.image.load('gg.jpg')
        self.rect_question = self.question.get_rect()
        self.rect_question.centerx = self.screen_rect.centerx
        self.rect_question.centery = self.screen_rect.centery
        self.right_answer = pygame.image.load('level_True.jpg')
        self.wrong_answer = pygame.image.load('level_False.jpg')
        self.img1 = pygame.image.load('g_2.jpg')
        self.img1 = pygame.transform.scale(self.img1, (700, 170))
        self.img2 = pygame.image.load('g3.jpg')
        self.img2 = pygame.transform.scale(self.img2, (700, 170))
        self.img3 = pygame.image.load('g1.jpg')
        self.img3 = pygame.transform.scale(self.img3, (700, 170))
        self.question0 = pygame.image.load('question.jpg')
        self.question_0 = pygame.transform.scale(self.question0, (60, 60))
        self.question_1 = pygame.transform.scale(self.question0, (70, 70))
        self.poyasnenna = pygame.image.load('POYASNENA.jpg')

    def pr_next(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #   button_sound = pygame.mixer.Sound('Sounds/button.wav')
        # print(self.settings.current_level)
        # print(self.settings.current_level == 1 and mouse[0] > self.screen_rect.centerx and mouse[1] > self.screen_rect.centery)
        if self.settings.current_level == 6 and mouse[0] < self.screen_rect.centerx and mouse[
            1] > self.screen_rect.centery:
            if click[0] == 1:
                self.settings.current_level = 0
                #         pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)
                sys.exit()
        elif self.settings.current_level == 5 and mouse[0] > self.screen_rect.centerx and mouse[1] > self.screen_rect.centery:
            print(click[0])
            if click[0] == 1:
                print('qqqqqqqq')
                self.settings.current_level = 2
                #  pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)
        if self.settings.current_level == 3:
            if 1160 > mouse[0] > 1100 and 1100 > mouse[1] > 10:
                print(123)
                self.screen.blit(self.question_1, (1090, 10))
                self.screen.blit(self.poyasnenna, (0, 0))

    def show(self):
        self.screen.blit(self.question, self.rect_question)
        self.screen.blit(self.question_0, (1100, 20))

    #  self.screen.blit(self.right_answer, (650, 600))
    # self.screen.blit(self.wrong_answer, (50, 600))

    def show_but(self):
        mouse = pygame.mouse.get_pos()
        xposg_2 = 180
        yposg_2 = 230
        nxg_2 = 700
        nyg_2 = 300
        #
        xposimg2 = 185
        yposimg2 = 350
        nximg2 = 960
        nyimg2 = 465
        #
        xposimg3 = 185
        yposimg3 = 490
        nximg3 = 960
        nyimg3 = 600
        #
        xposimg = 185
        yposimg = 615
        nximg = 980
        nyimg = 715

        click = pygame.mouse.get_pressed()
        print(pygame.mouse.get_pos())
        if self.settings.current_level == 3:
            if mouse[0] > xposg_2 and mouse[0] > yposg_2 and mouse[0] < nxg_2 and mouse[1] < nyg_2:
                self.screen.blit(self.img1, (180, 230))
                if click[0] == 1:
                    self.settings.current_level = 4
            if xposimg2 < mouse[0] < nximg2:
                if yposimg2 < mouse[1] < nyimg2:
                    self.screen.blit(self.img2, (180, 330))
            if xposimg3 < mouse[0] < nximg3 and yposimg3 < mouse[1] < nyimg3:
                self.screen.blit(self.img3, (180, 430))
            if xposimg < mouse[0] < nximg and yposimg < mouse[1] < nyimg:
                self.screen.blit(self.img3, (180, 590))