#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
import sys
import traceback
from random import *
from pygame.locals import *
import myplane
import enemy

# ==========初始化===================
pygame.init()
pygame.mixer.init()  # 混音器初始化
bg_size = width, height = 480, 652  # 设计背景尺寸
screen = pygame.display.set_mode(bg_size)  # 设置背景对话框
pygame.display.set_caption("飞机大战Demo")
backgroud = pygame.image.load("image/background.png")  # 加载背景图片,并设置为不透明

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


# ====================敌方飞机生成控制函数====================
def add_small_enemies(group1, group2, num):
    for i in range(num):
        e1 = enemy.SmallEnemy(bg_size)
        group1.add(e1)
        group2.add(e1)


def add_mid_enemies(group1, group2, num):
    for i in range(num):
        e2 = enemy.MidEnemy(bg_size)
        group1.add(e2)
        group2.add(e2)


def add_big_enemies(group1, group2, num):
    for i in range(num):
        e3 = enemy.BigEnemy(bg_size)
        group1.add(e3)
        group2.add(e3)


def main():
    clock = pygame.time.Clock()  # 设置帧率
    switch_image = False  # 控制飞机图片切换的标志位（用以模拟发动机喷火效果）
    delay = 60  # 控制分级图片切换的频率（延时参数）
    pygame.mixer.music.play(-1)  # 循环播放背景音乐
    running = True
    me = myplane.MyPlane(bg_size)  # 生成我方飞机
    # ====================实例化敌方飞机====================
    enemies = pygame.sprite.Group()  # 生成敌方飞机组
    small_enemies = pygame.sprite.Group()  # 敌方小型飞机组
    add_small_enemies(small_enemies, enemies, 1)  # 生成若干敌方小型飞机
    mid_enemies = pygame.sprite.Group()  # 敌方中型飞机组
    add_mid_enemies(mid_enemies, enemies, 1)  # 生成若干敌方中型飞机
    big_enemies = pygame.sprite.Group()  # 敌方大型飞机组
    add_big_enemies(big_enemies, enemies, 1)  # 生成若干敌方大型飞机

    while running:
        screen.blit(backgroud, (0, 0))  # 将背景图片打印到内存的屏幕上
        for event in pygame.event.get():  # 响应用户的偶然操作
            if event.type == QUIT:  # 如果用户按下屏幕上的关闭按钮，触发QUIT事件，程序退出
                pygame.quit()
                sys.exit()
        # ====================检测用户的键盘操作====================
        key_pressed = pygame.key.get_pressed()  # 获得用户所有的键盘输入序列
        if key_pressed[K_w] or key_pressed[K_UP]:
            me.move_up()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            me.move_down()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            me.move_left()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            me.move_right()
        # ====================绘制我方飞机，设置两种飞机交替绘制，以实现动态喷气效果====================
        if delay == 0:
            delay = 60
        delay -= 1
        if not delay % 3:
            switch_image = not switch_image
        if switch_image:
            screen.blit(me.image1, me.rect)  # 绘制我方飞机的两种不同的形式
        else:
            screen.blit(me.image2, me.rect)

        for each in small_enemies:  # 绘制小型敌机并自动移动
            each.move()
            screen.blit(each.image, each.rect)
        for each in mid_enemies:
            each.move()
            screen.blit(each.image, each.rect)
        for each in big_enemies:  # 绘制大型敌机并自动移动
            each.move()
            if switch_image:
                screen.blit(each.image1, each.rect)  # 绘制大型敌机的两种不同的形式
            else:
                screen.blit(each.image2, each.rect)
            if each.rect.bottom == -50:
                big_enemy_flying_sound.play(-1)

        pygame.display.flip()  # 将内存中绘制好的屏幕刷新到设备屏幕上
        clock.tick(60)  # 设置帧数为60


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
