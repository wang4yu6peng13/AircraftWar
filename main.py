#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import traceback
from random import *
from pygame.locals import *

# 初始化
pygame.init()
pygame.mixer.init() # 混音器初始化
bg_size = width, height = 480, 652  # 设计背景尺寸
screen = pygame.display.set_mode(bg_size)  # 设置背景对话框
pygame.display.set_caption("飞机大战Demo")
backgroud = pygame.image.load("image/background.png") # 加载背景图片,并设置为不透明

# ==========载入游戏音乐====================
pygame.mixer.music.load("sound/game_music.wav")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("sound/bullet.wav")
bullet_sound.set_volume(0.2)
big_enemy_flying_sound = pygame.mixer.Sound("sound/big_spaceship_flying.wav")
big_enemy_flying_sound.set_volume(0.2)
enemy1_down_sound = pygame.mixer.Sound("sound/enemy1_down.wav")
enemy1_down_sound.set_volume(0.2)
enemy2_down_sound = pygame.mixer.Sound("sound/enemy2_down.wav")
enemy2_down_sound.set_volume(0.2)
enemy3_down_sound = pygame.mixer.Sound("sound/enemy3_down.wav")
enemy3_down_sound.set_volume(0.2)
me_down_sound = pygame.mixer.Sound("sound/game_over.wav")
me_down_sound.set_volume(0.2)
button_down_sound = pygame.mixer.Sound("sound/button.wav")
button_down_sound.set_volume(0.2)
level_up_sound = pygame.mixer.Sound("sound/achievement.wav")
level_up_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound("sound/use_bomb.wav")
bomb_sound.set_volume(0.2)
get_bomb_sound = pygame.mixer.Sound("sound/get_bomb.wav")
get_bomb_sound.set_volume(0.2)
get_bullet_sound = pygame.mixer.Sound("sound/get_double_laser.wav")
get_bullet_sound.set_volume(0.2)

def main():
    pygame.mixer.music.play(-1)
    running = True
    while running:
        screen.blit(backgroud, (0, 0))
        for event in pygame.event.get():  # 响应用户的偶然操作
            if event.type == QUIT:  # 如果用户按下屏幕上的关闭按钮，触发QUIT事件，程序退出
                pygame.quit()
                sys.exit()
        pygame.display.flip()

if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()