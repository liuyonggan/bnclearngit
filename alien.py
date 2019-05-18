import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """docstring for Alien"""
    def __init__(self, ai_settings,screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
#jia zai tu xiang bing she zhi "rect" shu xiang      
        self.image = pygame.image.load(r'C:\Users\admin\Desktop\alien\images\alien.bmp')
        self.rect = self.image.get_rect()

#mei ge wai xing ren zui chu dou zai ping mu de zuo shang jia
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

#cun chu wai xing ren zhun que wei zhi 
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*
            self.ai_settings.fleet_direction)
        self.rect.x = self.x

