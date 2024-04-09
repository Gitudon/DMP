import random
import pygame
import time
import sys
import json
import pickle

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
base=(100,100)

def deck(screen,me,opposite):
    img = pygame.image.load("GUI/image/uramen/ura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, downbase)
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, upbase)

def dimension(screen,me,opposite):
    if len(me)>0:
        img = pygame.image.load("GUI/image/cards/"+me[0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]))
    if len(opposite)>0:
        img = pygame.image.load("GUI/image/cards/"+opposite[0][0]+".jpg")
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]))
    pygame.display.update()

def grdeck(screen,me,opposite):
    img = pygame.image.load("GUI/image/uramen/grura.jpg")
    if len(me)>0:
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+20+width*2,downbase[1]+10+height))
    if len(opposite)>0:
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-20-width*2,upbase[1]-10-height))
    pygame.display.update()

def manazone(screen,me,opposite):
    for i in range(len(me)):
        if me[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+me[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if me[i][1]:
            img = pygame.transform.rotate(img, 270)
            screen.blit(img, (downbase[0]+width-22-50*i,downbase[1]+32+height))
        else:
            img1 = pygame.transform.rotate(img, 180)
            screen.blit(img1, (downbase[0]+width+10-50*i,downbase[1]+10+height))
    for i in range(len(opposite)):
        if opposite[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+opposite[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if opposite[i][1]:
            img = pygame.transform.rotate(img, 90)
            screen.blit(img, (upbase[0]-width-22+50*i,upbase[1]+12-height))
        else:
            screen.blit(img, (upbase[0]-width-10+50*i,upbase[1]-10-height))
    pygame.display.update()
    return

def battlezone(screen,me,opposite):
    for i in range(len(me)):
        if me[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+me[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if me[i][1]:
            img = pygame.transform.rotate(img, 270)
            screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,downbase[1]-(height+10)+22))
        else:
            screen.blit(img, (upbase[0]-20-width*2+(10+width)*i,downbase[1]-(height+10)))
    for i in range(len(opposite)):
        if opposite[i][2]:
            img = pygame.image.load("GUI/image/uramen/ura.jpg")
        else:
            img = pygame.image.load("GUI/image/cards/"+opposite[i][0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        if opposite[i][1]:
            img = pygame.transform.rotate(img, 90)
            screen.blit(img, (upbase[0]-32-width*2+(10+width)*i,upbase[1]+(height+10)+22))
        else:
            img1 = pygame.transform.rotate(img, 180)
            screen.blit(img1, (upbase[0]-20-width*2+(10+width)*i,upbase[1]+(height+10)))
    pygame.display.update()
    return

def graveyard(screen,me,opposite):
    if len(me)>0:
        img = pygame.image.load("GUI/image/cards/"+me[0][0]+".jpg")
        img = pygame.transform.scale(img, (width, height))
        screen.blit(img, (downbase[0]+10+width,downbase[1]))
    if len(opposite)>0:
        img = pygame.image.load("GUI/image/cards/"+opposite[0][0]+".jpg")
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img2, (upbase[0]-10-width,upbase[1]))
    pygame.display.update()
    return

def emenu(screen):
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
    gTxt = font.render("視点切り替え", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    gTxt = font.render("1枚ドロー", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("デッキを確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("デッキをシャッフル", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("シールドを確認する", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("マナチャージする", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("山上を墓地送り", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("山上を山下へ", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("GR召喚", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("シールド追加", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ログを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.update()

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
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 200])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,250,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("デバッグメニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ログを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.update()

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
    gTxt = font.render("視点切り替え", True, (255,255,255))
    screen.blit(gTxt, [1265, 260])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,310,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 320])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,370,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 380])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,430,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 440])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,490,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 500])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,550,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 560])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,610,280,50))
    gTxt = font.render("", True, (255,255,255))
    screen.blit(gTxt, [1265, 620])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,670,280,50))
    gTxt = font.render("通常メニュー", True, (255,255,255))
    screen.blit(gTxt, [1265, 680])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,730,280,50))
    gTxt = font.render("ヘルプを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 740])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,790,280,50))
    gTxt = font.render("ゲームをリセット", True, (255,255,255))
    screen.blit(gTxt, [1265, 800])
    pygame.draw.rect(screen, (0,191,255), pygame.Rect(1260,850,280,50))
    gTxt = font.render("ログを表示", True, (255,255,255))
    screen.blit(gTxt, [1265, 860])
    pygame.draw.rect(screen, (226,4,27), pygame.Rect(1260,910,280,50))
    gTxt = font.render("ゲームを終了", True, (255,255,255))
    screen.blit(gTxt, [1265, 920])
    pygame.display.update()

def move(a,b,i):
    b.append(a[i])
    a.remove(a[i])
    return [a,b]

def Shuffle(a):
    sh=[]
    while len(a)!=0:
        b=random.choice(a)
        sh.append(b)
        a.remove(b)
    return sh

def swap(save):
    for i in range(len(save)//2):
        tmp=(save[2*i+1])
        save[2*i+1]=save[2*i]
        save[2*i]=tmp
    return save

def check(a):
    b=sorted(a)
    print(b)
    return len(b)

def put(save,card,flag):
    tmp=[card,False,False,[],[],-1,1,0]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save

def expand(save,card,flag):
    tmp=[card,False,False,[],[]]
    if flag:
        save[8].append(tmp)
    else:
        save[9].append(tmp)
    return save

def summon(save,card,flag):
    return put(save,flag,card)

def grsummon(n,save,flag,screen,debug):
    for _ in range(n):
        if flag:
            if len(save[14])==0:
                return save
            card=save[14][0]
            save[14]=save[14][1:]
        else:
            if len(save[15])==0:
                return save
            card=save[15][0]
            save[15]=save[15][1:]
        save=put(save,card,flag)
    recover(save,screen,debug)
    return save

def gotodeck(save,flag,card,up):
    if flag:
        if up:
            save[0]=[card]+save[0]
        else:
            save[0].append(card)
    else:
        if up:
            save[1]=[card]+save[1]
        else:
            save[1].append(card)
    return save

def bounce(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            save[4].append(card)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            save[5].append(card)
    return save

def draw(n,save,flag):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=bounce(save,save[0][0],flag)
                save[0] = save[0][1:]
            else:
                print("You can't draw a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=bounce(save,save[1][0],flag)
                save[1] = save[1][1:]
            else:
                print("You can't draw a card.")
    return save

def putgrave(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
                save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            save[10]=[card]+save[10]
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            save[11]=[card]+save[11]
    return save

def bochiokuri(n,save,flag,screen,debug):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putgrave(save,save[0][0],flag)
                save[0] = save[0][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putgrave(save,save[1][0],flag)
                save[1] = save[1][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    return save

def putmana(save,card,flag,crystal,zone):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            tmp=[card,False,False]
            tap=0
            if zone:
                if "_cs_" in card[0]:
                    tap=len(card[6][0])
                else:
                    tap=len(card[6])
            else:
                if "_cs_" in card[0]:
                    tap=max(len(card[6][0]),len(card[6][1]))
                else:
                    tap=len(card[6])
            if tap>=2:
                tmp[1]=True
            if crystal:
                tmp[2]=True
            save[6].append(tmp)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            tmp=[[card],False,False]
            tap=0
            if zone:
                if "_cs_" in card[0]:
                    tap=len(card[6][0])
                else:
                    tap=len(card[6])
            else:
                if "_cs_" in card[0]:
                    tap=max(len(card[6][0]),len(card[6][1]))
                else:
                    tap=len(card[6])
            if tap>=2:
                tmp[1]=True
            if crystal:
                tmp[2]=True
            save[7].append(tmp)
    return save

def addmana(n,save,flag,crystal,screen,debug):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putmana(save,save[0][0],flag,crystal,False)
                save[0] = save[0][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putmana(save,save[1][0],flag,crystal,False)
                save[1] = save[1][1:]
                recover(save,screen,debug)
            else:
                print("You can't put a card.")
    return save

def putshield(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            tmp=[card,True]
            save[2].append(tmp)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            tmp=[card,True]
            save[3].append(tmp)
    return save

def shieldplus(n,save,flag,screen,debug,mode):
    if flag:
        for _ in range(n):
            if save[0]!=[]:
                save=putshield(save,save[0][0],flag)
                save[0] = save[0][1:]
            else:
                print("You can't add a shield.")
    else:
        for _ in range(n):
            if save[1]!=[]:
                save=putshield(save,save[1][0],flag)
                save[1] = save[1][1:]
            else:
                print("You can't add a shield.")
    if mode:
        recover(save,screen,debug)
    return save

def seal(save,flag,key):
    if flag:
        tmp=save[0][0]
        save[0]=save[0][1:]
        save[8][key][2]=True
        save[8][key][3].insert(0,tmp)
    else:
        tmp=save[1][0]
        save[1]=save[1][1:]
        save[9][key][2]=True
        save[9][key][3].insert(0,tmp)
    return save

# 表示したカードを選択し、選択したカードがどれかという情報を返す関数select
# クリック位置でどのカードか判断して返す
def select(cards,screen,flag):
    return

def showcard(screen,cards,n):
    tmp=("GUI/image/"+cards[n][0]+".jpg")
    tmp=pygame.image.load(tmp)
    tmp=pygame.transform.scale(tmp, (500, 720))
    screen.blit(tmp, (525,90))
    pygame.display.update()
    return

#左右の切り替えカーソル
def lr(screen,flag):
    return

def rect(screen,flag):
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(base[0],base[1],field[0]-200,field[1]-200))
    if flag:
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(1420,110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [1417,107])
    pygame.display.update()
    return

def printcards(tmp,screen,mode,cards):
    w=200
    h=288
    for i in range(len(tmp)):
        tmp[i]=pygame.image.load(tmp[i])
        if mode==1:
            if cards[i][11]:
                pixel = pygame.PixelArray(tmp[i])
                for y in range(tmp[i].get_height()):
                    for x in range(tmp[i].get_width()):
                        rgba = screen.unmap_rgb(pixel[x][y])
                        gray = int((rgba[0] + rgba[1] + rgba[2]) / 3)
                        pixel[x][y] = (gray,gray,gray)
                del pixel
        elif mode==2:
            if cards[i][1]:
                pixel = pygame.PixelArray(tmp[i])
                for y in range(tmp[i].get_height()):
                    for x in range(tmp[i].get_width()):
                        rgba = screen.unmap_rgb(pixel[x][y])
                        gray = int((rgba[0] + rgba[1] + rgba[2]) / 3)
                        pixel[x][y] = (gray,gray,gray)
                del pixel
        elif mode==3:
            if cards[i][1]:
                pixel = pygame.PixelArray(tmp[i])
                for y in range(tmp[i].get_height()):
                    for x in range(tmp[i].get_width()):
                        rgba = screen.unmap_rgb(pixel[x][y])
                        gray = int((rgba[0] + rgba[1] + rgba[2]) / 3)
                        pixel[x][y] = (gray,gray,gray)
                del pixel
        tmp[i]=pygame.transform.scale(tmp[i], (w, h))
        # 総枚数に応じて表示形式を変えたい
        if i<=5:
            screen.blit(tmp[i], (base[0]+10*(i+1)+w*i,base[1]+10))
        elif 6<=i<=11:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+20+height))
        elif 12<=i<=17:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+30+height*2))
        elif 18<=i<=23:
            screen.blit(tmp[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+40+height*3))
    pygame.display.update()
    return

def info(save,screen,debug):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    recover(save,screen,debug)
                    return

def page(save,screen,debug,tmp,end):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    recover(save,screen,debug)
                    return
                #ページ切り替え
                #カード個別の処理(showcard呼び出し)

def showcards(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
    rect(screen,flag)
    for i in range(len(cards)):
        if i<=23:
            tmp[0].append("GUI/image/cards/"+cards[i][0]+".jpg")
        elif i<=47:
            tmp[1].append("GUI/image/cards/"+cards[i][0]+".jpg")
        elif i<=71:
            tmp[2].append("GUI/image/cards/"+cards[i][0]+".jpg")
        else:
            tmp[3].append("GUI/image/cards/"+cards[i][0]+".jpg")
    current=0
    end=len(tmp[current])//4+1
    if len(tmp[current])%4==0:
        end-=1
    printcards(tmp[current],screen,1,cards)
    page(save,screen,debug,tmp,end)
    return

def showmanazone(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
    rect(screen,flag)
    for i in range(len(cards)):
        if i<=23:
            if cards[i][2]:
                tmp[0].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[0].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=47:
            if cards[i][2]:
                tmp[1].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[1].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=71:
            if cards[i][2]:
                tmp[2].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[2].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        else:
            if cards[i][2]:
                tmp[3].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[3].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
    current=0
    end=len(tmp[current])//4+1
    if len(tmp[current])%4==0:
        end-=1
    printcards(tmp[current],screen,2,cards)
    page(save,screen,debug,tmp,end)
    return

def showbattlezone(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
    rect(screen,flag)
    for i in range(len(cards)):
        if i<=23:
            if cards[i][2]:
                tmp[0].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[0].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=47:
            if cards[i][2]:
                tmp[1].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[1].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=71:
            if cards[i][2]:
                tmp[2].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[2].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        else:
            if cards[i][2]:
                tmp[3].append("GUI/image/uramen/ura.jpg")
            else:
                tmp[3].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
    current=0
    end=len(tmp[current])//4+1
    if len(tmp[current])%4==0:
        end-=1
    printcards(tmp[current],screen,3,cards)
    page(save,screen,debug,tmp,end)
    return

def showshield(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    rect(screen,flag)
    cards=save[key]
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(base[0],base[1],field[0]-200,field[1]-200))
    for i in range(len(cards)):
        if i<=23:
            tmp[0].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=47:
            tmp[1].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        elif i<=71:
            tmp[2].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
        else:
            tmp[3].append("GUI/image/cards/"+cards[i][0][0]+".jpg")
    current=0
    end=len(tmp[current])//4+1
    if len(tmp[current])%4==0:
        end-=1
    printcards(tmp[current],screen,1,cards)
    page(save,screen,debug,tmp,end)
    return

def sshield(screen):
    for i in range(5):
        img = pygame.image.load("GUI/image/uramen/ura.jpg")
        img = pygame.transform.scale(img, (width, height))
        img2 = pygame.transform.rotate(img, 180)
        img2 = pygame.transform.scale(img2, (width, height))
        screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
        screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))
        pygame.display.update()
        time.sleep(0.5)

def shield(screen,flag,save):
    img = pygame.image.load("GUI/image/uramen/ura.jpg")
    if flag:
        for i in range(len(save[2])): 
            img = pygame.transform.scale(img, (width, height))
            screen.blit(img, ((downbase[0]-110)-width*i, downbase[1]))
    else:
        img2 = pygame.transform.rotate(img, 180)
        for i in range(len(save[3])):
            img2 = pygame.transform.scale(img2, (width, height))
            screen.blit(img2, ((upbase[0]+110)+width*i, upbase[1]))
    pygame.display.update()

def recover(save,screen,flag):
    screen.fill(fieldcolor)
    deck(screen,save[0],save[1])
    dimension(screen,save[12],save[13])
    grdeck(screen,save[14],save[15])
    shield(screen,True,save)
    shield(screen,False,save)
    manazone(screen,save[6],save[7])
    battlezone(screen,save[8],save[9])
    graveyard(screen,save[10],save[11])
    if flag==1:
        debugmenu(screen)
    elif flag==2:
        menu(screen)
    else:
        emenu(screen)
    pygame.display.update()
    return

def deckinfo(save,flag,screen,debug):
    font = pygame.font.SysFont("msgothic", 30)
    if flag:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(downbase[0]-10,downbase[1]+100,120,50))
        gTxt = font.render(str(len(save[0]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+10,downbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(downbase[0]+80,downbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+77,downbase[1]+107])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (downbase[0]+80<=x<=downbase[0]+100 and downbase[1]+110<=y<=downbase[1]+130):
                        recover(save,screen,debug)
                        return
    else:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(upbase[0]-10,upbase[1]+100,120,50))
        gTxt = font.render(str(len(save[1]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+10,upbase[1]+110])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(upbase[0]+80,upbase[1]+110,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+77,upbase[1]+107])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (upbase[0]+80<=x<=upbase[0]+100 and upbase[1]+110<=y<=upbase[1]+130):
                        recover(save,screen,debug)
                        return

def grdeckinfo(save,flag,screen,debug):
    font = pygame.font.SysFont("msgothic", 30)
    if flag:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(downbase[0]+2*width+10,downbase[1]+110+height,120,50))
        gTxt = font.render(str(len(save[14]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+2*width+30,downbase[1]+120+height])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(downbase[0]+2*width+100,downbase[1]+120+height,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [downbase[0]+2*width+97,downbase[1]+117+height])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (downbase[0]+2*width+100<=x<=downbase[0]+2*width+120 and downbase[1]+120+height<=y<=downbase[1]+140+height):
                        recover(save,screen,debug)
                        return
    else:
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(upbase[0]-30-2*width,upbase[1]-height+90,120,50))
        gTxt = font.render(str(len(save[15]))+"枚", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]-10-2*width,upbase[1]-height+100])
        pygame.draw.rect(screen, (255,0,0), pygame.Rect(upbase[0]+60-2*width,upbase[1]-height+100,20,20))
        font = pygame.font.SysFont("msgothic", 25)
        gTxt = font.render("×", True, (255,255,255))
        screen.blit(gTxt, [upbase[0]+57-2*width,upbase[1]-height+97])
        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (upbase[0]+60-2*width<=x<=upbase[0]+80-2*width and upbase[1]-height+100<=y<=upbase[1]-height+120):
                        recover(save,screen,debug)
                        return
    return

def decklist(screen,flag):
    max=11
    size=(510, 620)
    font = pygame.font.SysFont("msgothic", 50)
    rect(screen,False)
    if flag:
        gTxt = font.render("自分のデッキを選択", True, (255,255,255))
    else:
        gTxt = font.render("相手のデッキを選択", True, (255,255,255))
    screen.blit(gTxt, (550,110))
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(100,810,(field[0]-200)//2,90))
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(100+(field[0]-200)//2,810,(field[0]-200)//2,90))
    gTxt = font.render("←", True, (255,255,255))
    screen.blit(gTxt, (412,830))
    gTxt = font.render("→", True, (255,255,255))
    screen.blit(gTxt, (412+(field[0]-200)//2,830))
    num=1
    Pass="GUI/image/decks/deck"+str(num-1)+".jpeg"
    img = pygame.image.load(Pass)
    img = pygame.transform.scale(img, size) 
    screen.blit(img, (210, 180))
    Pass="GUI/image/decks/deck"+str(num)+".jpeg"
    img2 = pygame.image.load(Pass)
    img2 = pygame.transform.scale(img2, size)
    screen.blit(img2, (830, 180))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 110<=y<=730:
                    if 210<=x<=720:
                        return "deck"+str(num-1)
                    elif 830<=x<=1340:
                        return "deck"+str(num)
                elif 750<=y<=900:
                    if 100<=x<=100+(field[0]-200)//2:
                        if num==1:
                            num=max
                        else:
                            num-=2
                    elif 100+(field[0]-200)//2<x<=field[0]-100:
                        if num==max:
                            num=1
                        else:
                            num+=2
                    Pass="GUI/image/decks/deck"+str(num-1)+".jpeg"
                    img = pygame.image.load(Pass)
                    img = pygame.transform.scale(img, size)
                    screen.blit(img, (210, 180))
                    Pass="GUI/image/decks/deck"+str(num)+".jpeg"
                    img2 = pygame.image.load(Pass)
                    img2 = pygame.transform.scale(img2, size)
                    screen.blit(img2, (830, 180))
                    pygame.display.update()

def choose(screen,message):
    font = pygame.font.SysFont("msgothic", 50)
    rect(screen,False)
    font = pygame.font.SysFont("msgothic", 100)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(base[0],base[1]+600,(field[0]-200)//2,200))
    gTxt = font.render("は　い", True, (255,255,255))
    screen.blit(gTxt, [base[0]+187,base[1]+650])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(base[0]+(field[0]-200)//2,base[1]+600,(field[0]-200)//2,200))
    gTxt = font.render("いいえ", True, (255,255,255))
    screen.blit(gTxt, [base[0]+(field[0]-200)//2+187,base[1]+650])
    #messageを適切な長さで分割して複数行で表示する
    tmp=[]
    point=0
    current=""
    while len(message)>0:
        c=message[0]
        current+=c
        if len(c)==len(c.encode()):
            point+=0.5
        else:
            point+=1
        message=message[1:]
        if point>25 or c=="。" or c=="？":
            tmp.append(current)
            point=0
            current=""
    if current!="":
        tmp.append(current)
    font = pygame.font.SysFont("msgothic", 50)
    for i in range(len(tmp)):
        gTxt = font.render(tmp[i], True, (255,255,255))
        screen.blit(gTxt, [base[0]+20,base[1]+10*(i+1)+50*i])
    pygame.display.update()
    while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if base[1]+600<=y<=base[1]+800:
                        if base[0]<=x<=base[0]+(field[0]-200)//2:
                            return True
                        elif base[0]+(field[0]-200)//2<x<=field[0]-100:
                            return False

#メッセージを表示するコンソールをメニューから見れるようにする
#各アクションの実行後、ログを残す
def showlog(screen,log,save,debug):
    rect(screen,True)
    info(save,screen,debug)
    return

#説明書を表示する。画像でいいのではないでしょうか。
def dmphelp(screen,save,debug):
    rect(screen,True)
    info(save,screen,debug)
    return

def mekureid(save,n,flag,key):
    return save