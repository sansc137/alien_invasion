import pygame


class Ship:
    '''飞船'''

    def __init__(self, ai_game):
        '''初始化'''
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并且获取其碰撞面积
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 将飞船置于底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        # 移动开关
        self.moving_right = False

    def update(self):
            if self.moving_right:
                self.rect.x += 1
                
    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

    