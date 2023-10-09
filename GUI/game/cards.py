import random
import pygame
import time
import sys
from game import func

#定数の設定
width=100
height=144
field=(1550,900)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 602)

def b_s_001(save,flag):
    return func.draw(2,save,flag)

def gb_c_001_cip(save,flag):
    return func.draw(2,save,flag)

def b_s_001(save,flag):
    return func.draw(1,save,flag)


def b_c_003_cip(save,flag):
    if flag:
        temp=save[0]+save[10]
        save[0]=func.shuffle(temp)
        save[10]=[]
    else:
        temp=save[1]+save[11]
        save[1]=func.shuffle(temp)
        save[11]=[]
    return save

def b_c_001_cip(save,flag):
    if flag:
        if len(save[0])>5:
            temp=save[:5]
    return save