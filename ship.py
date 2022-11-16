import pygame


class Ship:
    '''飞船'''

    def __init__(self, ai_game):
        '''初始化'''
        self.screen = ai_game.screen
        self.settings= ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船图像并且获取其碰撞面积
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()

        # 将飞船置于底部中央
        self.rect.midbottom = self.screen_rect.midbottom
        
        # 存储小数值
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 移动开关
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        #更新飞船图像位置:
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.settings.ship_speed
            elif self.moving_left and self.rect.left > 0:
                self.x -= self.settings.ship_speed

            if self.moving_up and self.rect.top > 0:
                self.y -= self.settings.ship_speed
            elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.ship_speed
            # 根据飞船图像位置更新碰撞位置
            self.rect.x = self.x
            self.rect.y = self.y

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image, self.rect)

