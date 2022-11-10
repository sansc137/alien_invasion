import sys
import pygame

class Alien_invasion:
    def __init__(self):
        '''初始化游戏'''
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien_Invasion")

        #设置背景色
        self.bg_color = (230, 230,230)

    def run_game(self):
        while True:
            # 监视键盘和鼠标事件
            for event in pygame.event.get():
                if event in pygame.event.get():
                    sys.exit()

            # 让最近绘制的屏幕可见
            pygame.display.flip()


if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()
