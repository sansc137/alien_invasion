class Settings:
    '''存储<alien invasion>中的设置参数'''

    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1    # fleet_direction表示外星人的方向,1为向右,-1为向左
        
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3