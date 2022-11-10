import sys

import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien_Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event in pygame.event.get():
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
