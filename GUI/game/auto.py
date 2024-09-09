import random
import pygame
import time
import sys
import json
import pickle
from game.func import *
from game.cards import *

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
base=(100,100)

#メッセージを表示するコンソールをメニューから見れるようにする
#各アクションの実行後、ログを残す
def showlog(screen,log,save,debug):
    rect(screen,True)
    info(save,screen,debug)
    return

def mekureid(save,n,flag,key):
    return save

#カードを選択する
def choosecard(save,screen,zone):
    return

def gachinko_judge(save,screen,my_seigen,your_seigen):
    if save[0]==[] or my_seigen:
        mycost=0
        mycard=""
    else:
        me=save[0][0]
        mycost=me[3]
        mycard=me[0]
        if len(save[0])==1:
            save[0]=[me]
        else:
            save[0]=save[0][1:]+[me]
    if save[1]==[] or your_seigen:
        yourcost=0
        yourcard=""
    else:
        you=save[1][0]
        yourcost=you[3]
        yourcard=you[0]
        if len(save[1])==1:
            save[1]=[you]
        else:
            save[1]=save[1][1:]+[you]
    # カードの表示
    pygame.display.update()
    # 0は手前側の勝ち、1は奥側の勝ち
    if mycost>=yourcost:
        return [0,save]
    else:
        return [1,save]