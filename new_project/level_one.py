import pygame


class Level1:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.question = pygame.image.load('level_1.jpg')
        self.rect_question = self.question.get_rect()
        self.rect_question.centerx = self.screen_rect.centerx
        self.rect_question.centery = self.screen_rect.centery
        self.right_answer = pygame.image.load('level_True.jpg')
        self.wrong_answer = pygame.image.load('level_flase.jpg')

    def show(self):
        print('yes')
        self.screen.blit(self.question, self.rect_question)
        self.screen.blit(self.right_answer, (650, 600))
        self.screen.blit(self.wrong_answer, (50, 600))

