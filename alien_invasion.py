import sys
from typing import Self

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

    def _check_events(self):
        '''响应玩家操作'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # 向右移动
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                # 向左移动
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                

    def _update_screen(self):
        '''依照操作更新图像'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        '''运行游戏'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
