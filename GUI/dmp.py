import pygame
import sys
import time
import json
import pickle
import copy
from game.func import Shuffle,showcards,draw,recover,move,check,deck,shield,menu,showcard,sshield,shieldplus,grdeck,dimension,deckinfo,debugmenu,dmphelp,decklist
from game import cards
from game import decks

#定数の設定
width=100
height=144
field=(1550,900)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 602)
# 動的に指定するための辞書
card={}
Deck={'deck0':decks.deck0,'deck1':decks.deck1,'deck2':decks.deck2,'deck3':decks.deck3,'deck4':decks.deck4,'deck5':decks.deck5,'deck6':decks.deck6,'deck7':decks.deck7,'deck8':decks.deck8,'deck9':decks.deck9,'deck10':decks.deck10,'deck11':decks.deck11,'deck12':decks.deck12,'deck13':decks.deck13,'deck14':decks.deck14,'deck15':decks.deck15,'deck16':decks.deck16,'deck17':decks.deck17,'deck18':decks.deck18,'deck19':decks.deck19,'deck20':decks.deck20,'deck21':decks.deck21,'deck22':decks.deck22,'deck23':decks.deck23,'deck24':decks.deck24,'deck25':decks.deck25,'deck26':decks.deck26,'deck27':decks.deck27,'deck28':decks.deck28,'deck29':decks.deck29,'deck30':decks.deck30}

def main():
    #初期設定だよ
    pygame.init() 
    screen = pygame.display.set_mode(field) 
    pygame.display.set_caption("Duel Masters")
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415
    save=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    # カードを表す配列の形式
    # card = [key, name, race, cost, power, color, cipTF, tapTF, cardtype, keywordskills, STTF, GSTF]
    #デッキ選択
    screen.fill(fieldcolor)
    pygame.display.update()
    choosing=True
    num=1
    decklist(screen,num)
    pygame.display.update()
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 210<=x<=720 and 110<=y<=730:
                    deckname1="deck"+str(num-1)
                    choosing=False
                elif 830<=x<=1340 and 110<=y<=730:
                    deckname1="deck"+str(num)
                    choosing=False
    choosing=True
    num=1
    decklist(screen,num)
    pygame.display.update()
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 110<=x<=770 and 110<=y<=730:
                    deckname2="deck"+str(num-1)
                    choosing=False
                elif 780<=x<=1440 and 110<=y<=730:
                    deckname2="deck"+str(num)
                    choosing=False
    #デッキ登録 仕様変更が必要。
    save[0]=copy.deepcopy(Deck.get(deckname1))
    save[1]=copy.deepcopy(Deck.get(deckname2))
    save[0]=Shuffle(save[0])
    save[1]=Shuffle(save[1])
    
    #シールド展開
    screen.fill(fieldcolor)
    pygame.display.update()
    deck(screen,save[0],save[1])
    pygame.display.update()
    time.sleep(1)
    dimension(screen,save[12],save[13])
    if len(save[12])>0 or len(save[13])>0:
        pygame.display.update()
        time.sleep(1)
    grdeck(screen,save[14],save[15])
    if len(save[14])>0 or len(save[15])>0:
        pygame.display.update()
        time.sleep(1)
    sshield(screen)
    save=shieldplus(5,save,True)
    save=shieldplus(5,save,False)
    menu(screen)
    pygame.display.update()
    time.sleep(1)
    #最初のドロー
    save=draw(5,save,True)
    save=draw(5,save,False)
    #表示フラグ
    fflag=True #フィールドを表示している
    tflag=False #手札全体を見ている
    qflag=False #手札のカードを見ている
    dflag=False #デッキ枚数を確認中
    debug=False
    d1=True
    d2=True
    #以下、ゲーム処理
    while True:
        #山札切れ
        if save[0]==[] and d1:
            recover(save,screen,debug)
            d1=False
        if save[1]==[] and d2:
            recover(save,screen,debug)
            d2=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #ボタン操作
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            #クリック操作
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if fflag:
                    if 1260<=x<=1540:
                        if debug:
                            if 10<=y<=60:
                                fflag=False
                                showcards(save[4],screen,True)
                                pygame.display.update()
                                tflag=True
                            elif 70<=y<=120:
                                save[4]=sorted(save[4])
                            elif 130<=y<=180:
                                save=cards.b_s_001(save,True)
                            elif 190<=y<=240:
                                fflag=False
                                showcards(save[2],screen,True)
                                pygame.display.update()
                                tflag=True
                            elif 670<=y<=720:
                                debug=False
                                menu(screen)
                                pygame.display.update()
                            elif 730<=y<=780:
                                dmphelp()
                            elif 790<=y<=840:
                                main()
                            elif 850<=y<=900:
                                pygame.quit()
                                sys.exit()
                        else:
                            if 10<=y<=60:
                                fflag=False
                                showcards(save[4],screen,True)
                                pygame.display.update()
                                tflag=True
                            elif 70<=y<=120:
                                save[4]=sorted(save[4])
                            elif 130<=y<=180:
                                save[4]=Shuffle(save[4])
                            elif 670<=y<=720:
                                debug=True
                                debugmenu(screen)
                                pygame.display.update()
                            elif 730<=y<=780:
                                dmphelp()
                            elif 790<=y<=840:
                                main()
                            elif 850<=y<=900:
                                pygame.quit()
                                sys.exit()
                    elif downbase[0]<=x<=downbase[0]+width and downbase[1]<=y<=downbase[1]+height:
                        deckinfo(save,True,screen)
                        dflag=True
                        fflag=False
                    elif upbase[0]<=x<=upbase[0]+width and upbase[1]<=y<=upbase[1]+height:
                        deckinfo(save,False,screen)
                        dflag=True
                        fflag=False
                elif tflag:
                    if 1420<=x<=1440 and 110<=y<=130:
                        tflag=False
                        fflag=True
                        recover(save,screen,debug)
                        pygame.display.update()
                elif dflag:
                    if downbase[0]+80<=x<=downbase[0]+100 and downbase[1]+110<=y<=downbase[1]+130:
                        dflag=False
                        fflag=True
                        recover(save,screen,debug)
                        pygame.display.update()
                    elif upbase[0]+80<=x<=upbase[0]+100 and upbase[1]+110<=y<=upbase[1]+130:
                        dflag=False
                        fflag=True
                        recover(save,screen,debug)
                        pygame.display.update()
            pygame.display.update()

if __name__=="__main__":
    main()