import random
import pygame
import time
import sys
import json
import pickle

#定数の設定
width=100
height=144
field=(1550,900)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 602)

def deck(screen,me,opposite):
    img = pygame.image.load("DMP/GUI/image/ura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, downbase)
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, upbase)

def dimension(screen,me,opposite):
    img = pygame.image.load("DMP/GUI/image/r_d_001.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]))
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]))

def grdeck(screen,me,opposite):
    img = pygame.image.load("DMP/GUI/image/grura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]+10+height))
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]-10-height))

def menu(screen):
    font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (192,192,192), pygame.Rect(field[0]-300,0,300,field[1]))
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,10,280,50))
    gTxt = font.render("手札を確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 20])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,70,280,50))
    gTxt = font.render("手札をソートする", True, (255,255,255))
    screen.blit(gTxt, [1265, 80])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,130,280,50))
    gTxt = font.render("手札をシャッフル", True, (255,255,255))
    screen.blit(gTxt, [1265, 140])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,190,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("デバッグメニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])

def debugmenu(screen):
    font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (192,192,192), pygame.Rect(field[0]-300,0,300,field[1]))
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,10,280,50))
    gTxt = font.render("手札を確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 20])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,70,280,50))
    gTxt = font.render("手札をソートする", True, (255,255,255))
    screen.blit(gTxt, [1265, 80])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,130,280,50))
    gTxt = font.render("1枚ドロー", True, (255,255,255))
    screen.blit(gTxt, [1265, 140])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,190,280,50))
    gTxt = font.render("シールド確認", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("通常メニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])

def move(a,b,i):
    b.append(a[i])
    a.remove(a[i])
    return [a,b]

def shuffle(a):
    sh=[]
    while len(a)!=0:
        b=random.choice(a)
        sh.append(b)
        a.remove(b)
    return sh

def check(a):
    b=sorted(a)
    print(b)
    return len(b)

# 配列から要素を選んでほかの配列に移動させる関数
def choice(save,flag,screen):
    return save

def draw(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save[4].append(save[0][0])
                save[0] = save[0][1:]
            else:
                print("You can't draw a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save[5].append(save[1][1])
                save[1] = save[1][1:]
            else:
                print("You can't draw a card.")
    return save

def bochiokuri(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save[10].append(save[0][0])
                save[0] = save[0][1:]
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save[11].append(save[1][1])
                save[1] = save[1][1:]
            else:
                print("You can't put a card.")
    return save

def addmana(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save[6].append(save[0][0])
                if len(save[6][-1][4])>=2:
                    save[6][-1][6]=True
                save[0] = save[0][1:]
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save[7].append(save[1][1])
                if len(save[7][-1][4])>=2:
                    save[7][-1][6]=True
                save[1] = save[1][1:]
            else:
                print("You can't put a card.")
    return save

def shieldplus(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save[2].append(save[0][0])
                save[0] = save[0][1:]
            else:
                print("You can't add a shield.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save[3].append(save[1][1])
                save[1] = save[1][1:]
            else:
                print("You can't add a shield.")
    return save

def showcards(cards,screen,flag):
    w=200
    h=288
    tmp=[]
    base=(100,100)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(100,100,field[0]-200,field[1]-200))
    # カードを配列として記録するので要変更
    for i in range(len(cards)):
        tmp.append("DMP/GUI/image/"+cards[i]+".jpg")
    for i in range(len(tmp)):
        tmp[i]=pygame.image.load(tmp[i])
        tmp[i]=pygame.transform.scale(tmp[i], (w, h))
        # 総枚数に応じて表示形式を変えたい
        if i<=5:
            screen.blit(tmp[i], (base[0]+10*(i+1)+w*i,base[1]+10))
        elif 6<=i<=11:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+20+height))
        elif 12<=i<=17:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+30+height*2))
        else:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+40+height*3))
    if flag:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(1420,110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [1417,107])

# 表示したカードを選択し、選択したカードがどれかという情報を返す関数select
def select(cards,screen,flag):
    return

def showcard(screen,cards):
    n=0
    # カードを配列として記録するので要変更
    tmp=("DMP/GUI/image/"+cards[n]+".jpg")
    tmp=pygame.image.load(tmp)
    tmp=pygame.transform.scale(tmp, (500, 720))
    screen.blit(tmp, (525,90))

def sshield(screen):
    for i in range(5):
        img = pygame.image.load("DMP/GUI/image/ura.jpg")
        img = pygame.transform.scale(img, (width, height))
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
        screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))
        pygame.display.update()
        time.sleep(0.5)

def shield(screen,flag,save):
    img = pygame.image.load("DMP/GUI/image/ura.jpg")
    if flag:
        for i in range(len(save[2])):
            img = pygame.transform.scale(img, (width, height))
            screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
    else:
        img2 = pygame.transform.rotate(img, 180)
        for i in range(len(save[3])):
            img2 = pygame.transform.scale(img2, (width, height))
            screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))

def recover(save,screen,flag):
    screen.fill(fieldcolor)
    deck(screen,save[0],save[1])
    dimension(screen,save[12],save[13])
    grdeck(screen,save[14],save[15])
    shield(screen,True,save)
    shield(screen,False,save)
    if flag:
        debugmenu(screen)
    else:
        menu(screen)

#説明書を表示する。画像でいいのではないでしょうか。
def dmphelp():
    return

def deckinfo(save,flag,screen):
    font = pygame.font.SysFont("msgothic", 30)
    if flag:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(downbase[0]-10,downbase[1]+100,120,50))
        gTxt = font.render(str(len(save[0]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+10,downbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(downbase[0]+80,downbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+77,downbase[1]+107])
    else:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(upbase[0]-10,upbase[1]+100,120,50))
        gTxt = font.render(str(len(save[1]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+10,upbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(upbase[0]+80,upbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+77,upbase[1]+107])

def decklist(screen,num):
    size=(510, 620)
    # font = pygame.font.SysFont("msgothic", 30)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(100,100,field[0]-200,field[1]-200))
    Pass="DMP/GUI/image/decks/deck"+str(num-1)+".jpeg"
    img = pygame.image.load(Pass)
    img = pygame.transform.scale(img, size)
    screen.blit(img, (210, 110))
    Pass="DMP/GUI/image/decks/deck"+str(num)+".jpeg"
    img2 = pygame.image.load(Pass)
    img2 = pygame.transform.scale(img2, size)
    screen.blit(img2, (830, 110))