import sys
import pygame

from settings import Settings

class Alien_invasion:
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien_Invasion")

    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event in pygame.event.get():
                    sys.exit()

            # 每次循环时都重绘屏幕
            self.screen.fill(self.settings.bg_color)
            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()
