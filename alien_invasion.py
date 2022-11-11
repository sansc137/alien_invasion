import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        '''初始化游戏'''
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien_Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

# 以下两个函数是为_check_events()函数设置的
    def _check_keydowm_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_ESCAPE: 
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
                    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _fire_bullet(self):
        '''创造一颗子弹,将其加入编组bullets中'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullets = Bullet(self)
            self.bullets.add(new_bullets)


    def _check_events(self):
        '''响应玩家操作'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydowm_events(event)
        
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
        
    def _update_bullets(self):
        self.bullets.update()
            # 删除消失的子弹
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))
                
    def _update_screen(self):
        '''依照操作更新图像'''
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # 让最近绘制的屏幕可见
        pygame.display.flip()

    def run_game(self):
        '''运行游戏'''
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
