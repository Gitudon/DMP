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
    gTxt = font.render("デッキの上を見る", True, (255,255,255))
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

def putshield2(save,card,flag):
    if flag:
        if "_grc_" in card[0]:
            save[14].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[12].append(card)
        else:
            tmp=[card,False]
            save[2].append(tmp)
    else:
        if "_grc_" in card[0]:
            save[15].append(card)
        elif any(substring in card[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_"]):
            save[13].append(card)
        else:
            tmp=[card,False]
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

def showcard(screen,card,flag,key):
    if flag==1:
        tmp= pygame.image.load("GUI/image/uramen/ura.jpg")
    elif flag==2:
        tmp=pygame.image.load("GUI/image/cards/"+card[0][0]+".jpg")
        pixels = pygame.PixelArray(tmp)
        for y in range(tmp.get_height()):
            for x in range(tmp.get_width()):
                r, g, b, _ = screen.unmap_rgb(pixels[x][y])
                gray = int((r + g + b) / 3)
                pixels[x][y] = (gray, gray, gray)
        del pixels
    elif flag==3:
        tmp=pygame.image.load("GUI/image/uramen/ura.jpg")
        pixels = pygame.PixelArray(tmp)
        for y in range(tmp.get_height()):
            for x in range(tmp.get_width()):
                r, g, b, _ = screen.unmap_rgb(pixels[x][y])
                gray = int((r + g + b) / 3)
                pixels[x][y] = (gray, gray, gray)
        del pixels
    else:
        if key in [2,3,6,7,8,9]:
            tmp=pygame.image.load("GUI/image/cards/"+card[0][0]+".jpg")
        else:
            tmp=pygame.image.load("GUI/image/cards/"+card[0]+".jpg")
    tmp=pygame.transform.scale(tmp, (500, 720))
    screen.blit(tmp, (110,140))
    pygame.display.update()
    return

def cardmenu(screen,key):
    font = pygame.font.SysFont("msgothic", 50)
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415、構成カード1617
    mode=[0,0,3,3,6,6,7,7,8,8,5,5,2,2,0,0,4,4]
    n=mode[key]
    for i in range(n):
        txt=""
        pygame.draw.rect(screen, (0,191,255), pygame.Rect(630,145+80*i,780,70))
        gTxt = font.render(txt, True, (255,255,255))
    # if key in [2,3]:
    #     return
    pygame.display.update()
    return

def lr(screen):
    font = pygame.font.SysFont("msgothic", 50)
    pygame.draw.rect(screen, (255,0,0), pygame.Rect(1370,280,70,300))
    gTxt = font.render("→", True, (255,255,255))
    screen.blit(gTxt, [1380,405])
    pygame.draw.rect(screen, (0,0,255), pygame.Rect(1370,590,70,300))
    gTxt = font.render("←", True, (255,255,255))
    screen.blit(gTxt, [1380,715])
    pygame.display.update()
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

def cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key):
    rect(screen,True)
    cardmenu(screen,key)
    card=cards[cardkey]
    if key in [2,3]:
        if card[1]:
            showcard(screen,card,1,key)
        else:
            showcard(screen,card,0,key)
    elif key in [6,7]:
        if card[1]:
            if card[2]:
                showcard(screen,card,3,key)
            else:
                showcard(screen,card,2,key)
        else:
            showcard(screen,card,0,key)
    elif key in [8,9]:
        if card[11]:
            showcard(screen,card,2,key)
        else:
            showcard(screen,card,0,key)
    else:
        showcard(screen,card,0,key)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1420<=x<=1440 and 110<=y<=130:
                    rect(screen,True)
                    printcards(tmp[current],screen,flag,cards,flag2)
                    page(save,screen,debug,tmp,current,end,flag,cards,flag2,key)
                    return
                #ここから下、個別処理
                # if key==2 or key==3:
                #     #更新して閉じる
                #     rect(screen,True)
                #     printcards(tmp[current],screen,flag,cards,flag2)
                #     page(save,screen,debug,tmp,current,end,flag,save[key],flag2,key)
                #     return

def printcards(tmp,screen,mode,cards,flag):
    w=200
    h=288
    rect(screen,flag)
    t=[0]*len(tmp)
    for i in range(len(tmp)):
        flg=False
        t[i]=pygame.image.load(tmp[i])
        t[i]=pygame.transform.scale(t[i], (w, h))
        if mode==1:
            if cards[i][11]:
                t[i]=pygame.transform.rotate(t[i], 90)
                flg=True
        elif mode==2:
            if cards[i][1]:
                t[i]=pygame.transform.rotate(t[i], 90)
                flg=True
        elif mode==3:
            if cards[i][1]:
                t[i]=pygame.transform.rotate(t[i], 90)
                flg=True
        if i<=5:
            if flg:
                screen.blit(t[i], (base[0]+10*(i+1)+w*i,base[1]+54))
            else:
                screen.blit(t[i], (base[0]+10*(i+1)+w*i,base[1]+10))
        elif 6<=i<=11:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+64+height))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+20+height))
        elif 12<=i<=17:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+74+height*2))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+30+height*2))
        elif 18<=i<=23:
            if flg:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+84+height*3))
            else:
                screen.blit(t[i], (base[0]+10*(i%6+1)+w*(i%6),base[1]+40+height*3))
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

def page(save,screen,debug,tmp,current,end,flag,cards,flag2,key):
    lr(screen)
    cards=save[key]
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
                if 1370<=x<=1440:
                    if 280<=y<=580:
                        current+=1
                        if current==4 or len(tmp[current])==0:
                            current=0
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page(save,screen,debug,tmp,current,end,flag,cards,flag2,key)
                        return
                    elif 590<=y<=890:
                        current-=1
                        if current==-1:
                            current=3
                            while len(tmp[current])==0:
                                current-=1
                        end=len(tmp[current])//6
                        if len(tmp[current])%6==0:
                            end-=1
                        printcards(tmp[current],screen,flag,cards,flag2)
                        page(save,screen,debug,tmp,current,end,flag,cards,flag2,key)
                        return
                for i in range(end+1):
                    if i==end:
                        if 110+144*i<=y<=398+144*i:
                            edge=len(tmp[current])%6-1
                            if edge==-1:
                                edge=6
                            for j in range(edge+1):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key)
                                    return
                    else:
                        if 110+144*i<=y<=254+144*i:
                            for j in range(6):
                                if 110+210*j<=x<=310+210*j:
                                    cardkey=24*current+6*i+j
                                    cardinfo(cardkey,save,screen,debug,tmp,current,end,flag,cards,flag2,key)
                                    return

def showcards(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
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
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,1,cards,flag)
    page(save,screen,debug,tmp,current,end,1,cards,flag,key)
    return

def showmanazone(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
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
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,2,cards,flag)
    page(save,screen,debug,tmp,current,end,2,cards,flag,key)
    return

def showbattlezone(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
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
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,3,cards,flag)
    page(save,screen,debug,tmp,current,end,3,cards,flag,key)
    return

def showshield(save,screen,flag,key,debug):
    tmp=[[],[],[],[]]
    cards=save[key]
    pygame.draw.rect(screen, (0,0,0), pygame.Rect(base[0],base[1],field[0]-200,field[1]-200))
    for i in range(len(cards)):
        if i<=23:
            if cards[i][1]:
                path="GUI/image/uramen/ura.jpg"
            else:
                path="GUI/image/cards/"+cards[i][0][0]+".jpg"
            tmp[0].append(path)
        elif i<=47:
            if cards[i][1]:
                path="GUI/image/uramen/ura.jpg"
            else:
                path="GUI/image/cards/"+cards[i][0][0]+".jpg"
            tmp[1].append(path)
        elif i<=71:
            if cards[i][1]:
                path="GUI/image/uramen/ura.jpg"
            else:
                path="GUI/image/cards/"+cards[i][0][0]+".jpg"
            tmp[2].append(path)
        else:
            if cards[i][1]:
                path="GUI/image/uramen/ura.jpg"
            else:
                path="GUI/image/cards/"+cards[i][0][0]+".jpg"
            tmp[3].append(path)
    current=0
    end=len(tmp[current])//6
    if len(tmp[current])%6==0:
        end-=1
    printcards(tmp[current],screen,4,cards,flag)
    page(save,screen,debug,tmp,current,end,4,cards,flag,key)
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

def maisu(screen):
    #枚数を聞く
    n=0
    return n

#枚数を聞き、その枚数分山札の上からカードを表示する 全カードに対して処理が終わるまでウィンドウは閉じないようにする
def miru():
    return



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