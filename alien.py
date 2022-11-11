import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    '''外星人对象'''

    def __init__(self, ai_game):
        '''初始化'''
        super().__init__()          # 用于继承ship类的属性
        self.screen = ai_game.screen 

        # 加载图像和碰撞面积
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)