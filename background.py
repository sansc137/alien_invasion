import pygame
from pygame.sprite import Sprite

class Background(Sprite):
    """游戏背景精灵"""

    def __init__(self, is_alt=False):

        super().__init__("images/background.png")

        # 2. 判断是否是交替图像，如果是，需要设置初始位置
    #     if is_alt:
    #         self.rect.y = -self.rect.height

    # def update(self):

    #     # 1. 调用父类的方法实现
    #     super().update()

    #     # 2. 判断是否移出屏幕，如果移出屏幕，将图像设置到屏幕的上方
    #     if self.rect.y >= self.settings.screen_height:
    #         self.rect.y = -self.rect.height
