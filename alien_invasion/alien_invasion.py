import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    
    ai_settings = Settings()
    # 初始化游戏并创建一个屏幕对象
    pygame.init() 
    pygame.display.set_caption("Alien Invasion")
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,
        ai_settings.screen_height))

    # 创建一艘飞船
    ship = Ship(screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标的事件
        gf.check_events()
        gf.update_screen(ai_settings, screen, ship)

run_game()