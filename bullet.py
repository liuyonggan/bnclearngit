import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """docstring for Bullet"""
    def __init__(self,ai_settings,screen,ship):
        #zai fei chuan suo chu wei zhi zai chaung zao yi ge zi dan dui xiang
        super(Bullet, self).__init__()
        self.screen = screen
      #zai (0,0) chu chuang jian yi ge biao shi zi dan de ju xing ,zai she zhi zhengque de wei zhi
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.y=float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        self.y -=self.speed_factor
        self.rect.y = self.y
    
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        