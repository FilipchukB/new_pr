import pygame


class Level1:
    def __init__(self, screen, settings):
        self.screen = screen
        self.settings = settings
        self.screen_rect = self.screen.get_rect()
        self.question = pygame.image.load('level_1.jpg')
        self.rect_question = self.question.get_rect()
        self.rect_question.centerx = self.screen_rect.centerx
        self.rect_question.centery = self.screen_rect.centery
        self.right_answer = pygame.transform.scale(pygame.image.load('level_True.jpg'), (530, 130))
        self.wrong_answer = pygame.transform.scale(pygame.image.load('level_False.jpg'), (530, 130))
        self.question0 = pygame.image.load('question.jpg')
        self.question_0 = pygame.transform.scale(self.question0, (60, 60))
        self.question_1 = pygame.transform.scale(self.question0, (70, 70))
        self.poyasnenna = pygame.image.load('POYASNENA.jpg')

    def pr_next(self):
        print(000)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        button_sound = pygame.mixer.Sound('Sounds/button.wav')
        # print(self.settings.current_level) print(self.settings.current_level == 1 and mouse[0] >
        # self.screen_rect.centerx and mouse[1] > self.screen_rect.centery)
        if self.settings.current_level == 1 and mouse[0] < self.screen_rect.centerx and mouse[
            1] > self.screen_rect.centery:
            if click[0] == 1:
                self.settings.current_level = 2
                self.settings.histori_1 = 0
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)
        elif self.settings.current_level == 1 and mouse[0] > self.screen_rect.centerx and mouse[
            1] > self.screen_rect.centery:
            print(click[0])
            if click[0] == 1:
                print('qqqqqqqq')
                self.settings.current_level = 2
                self.settings.histori_1 = 0
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(200)

        if self.settings.current_level == 1:
            if 1160 > mouse[0] > 1100 and 1100 > mouse[1] > 10:
                print(123)
                self.screen.blit(self.question_1, (1090, 10))
                self.screen.blit(self.poyasnenna, (0, 0))

    def show(self):
        self.screen.blit(self.question, self.rect_question)
        self.screen.blit(self.right_answer, (650, 600))
        self.screen.blit(self.wrong_answer, (50, 600))
        self.screen.blit(self.question_0, (1100, 20))
    #   self.screen.blit(self.question_1, (1090, 10))
