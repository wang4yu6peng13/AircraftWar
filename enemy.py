#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from random import *


class SmallEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy1.png")  # 加载敌方飞机图片
        self.rect = self.image.get_rect()  # 获得敌方飞机的位置
        self.width, self.height = bg_size[0], bg_size[1]  # 本地化背景图片位置
        self.speed = 2  # 设置敌机的速度
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # 定义敌机出现的位置
                                         randint(-5 * self.rect.height, -5)  # 保证敌机不会在程序已开始就立即出现
                                         )

    def move(self):  # 定义敌机的移动函数
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # 当敌机向下移动出屏幕时
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-5 * self.rect.height, 0)
                                         )


class MidEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("image/enemy2.png")  # 加载敌方飞机图片
        self.rect = self.image.get_rect()  # 获得敌方飞机的位置
        self.width, self.height = bg_size[0], bg_size[1]  # 本地化背景图片位置
        self.speed = 1  # 设置敌机的速度
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # 定义敌机出现的位置
                                         randint(-10 * self.rect.height, -self.rect.height)
                                         )

    def move(self):  # 定义敌机的移动函数
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # 当敌机向下移动出屏幕时
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-10 * self.rect.height, -self.rect.height)
                                         )


class BigEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load("image/enemy3_n1.png")  # 加载敌方飞机图片,大型飞机有帧切换的特效
        self.image2 = pygame.image.load("image/enemy3_n2.png")
        self.rect = self.image1.get_rect()  # 获得敌方飞机的位置
        self.width, self.height = bg_size[0], bg_size[1]  # 本地化背景图片位置
        self.speed = 2  # 设置敌机的速度
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),  # 定义敌机出现的位置
                                         randint(-15 * self.rect.height, -5 * self.rect.height)
                                         )

    def move(self):  # 定义敌机的移动函数
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):  # 当敌机向下移动出屏幕时
        self.rect.left, self.rect.top = (randint(0, self.width - self.rect.width),
                                         randint(-15 * self.rect.height, -5 * self.rect.height)
                                         )
