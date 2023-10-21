import pygame
import sys
import time
import json
import pickle
import copy
import codecs
from game.func import Shuffle,showcards,draw,recover,move,check,deck,shield,menu,showcard,sshield,shieldplus,grdeck,dimension,deckinfo,debugmenu,dmphelp,decklist
from game import cards
from game import carddic
from game import deckdic
from game import deckbuild

#定数の設定
width=100
height=144
field=(1550,900)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 602)
# 動的に指定するための辞書
card=carddic.card
Deck=deckdic.Deck
#実行ログのパス
logpath='DMP/GUI/etc/log.txt'

#タイトル画面
def main():
    #登録されたデッキリストから選びたい
    #自分で空きスロットに登録できるようにもしたい
    #テキストファイルをもととしたデッキのビルド
    for i in range(30):
        path='DMP/GUI/decks/deck'+str(i)+'.txt'
        name='deck'+str(i)
        Deck[name]=deckbuild.build(path)
    Duel()

#デュエル実行
def Duel():
    #初期設定だよ
    pygame.init() 
    screen = pygame.display.set_mode(field) 
    pygame.display.set_caption("Duel Masters")
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415
    save=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
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
    print(save,file=codecs.open('DMP/GUI/etc/output.txt','w','utf-8'))
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
                                save=card["b_s_002"](save,True)
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
                                Duel()
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
                                Duel()
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