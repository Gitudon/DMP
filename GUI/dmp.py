import pygame
import sys
import time
import json
import pickle
import copy
import codecs
from game.func import Shuffle,showcards,draw,recover,move,check,deck,shield,menu,showcard,sshield,shieldplus,grdeck,dimension,deckinfo,debugmenu,dmphelp,decklist,emenu,swap,grdeckinfo,choose,showlog
from game import cards
from game import carddic
from game import deckdic
from game import deckbuild

#定数の設定
width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
#動的に指定するための辞書
card=carddic.card
Deck=deckdic.Deck
#実行ログのパス
logpath='GUI/etc/log.txt'

#タイトル画面
def main():
    #登録されたデッキリストから選びたい
    #自分で空きスロットに登録できるようにもしたい
    #テキストファイルをもととしたデッキのビルド
    for i in range(30):
        path='GUI/decks/deck'+str(i)+'.txt'
        name='deck'+str(i)
        Deck[name]=deckbuild.build(path)
    #モード切り替え
    mode=1
    
    initalize(mode)

def initalize(mode):
    log=[]
    #初期設定
    pygame.init() 
    screen = pygame.display.set_mode(field) 
    pygame.display.set_caption("Duel Masters")
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415
    save=[[],[],[],[],[],[],[],[],[],[],[],[],[['b_c_003', '水上第九院 シャコガイル', ['ムートピア'], 9, 1, 13000, ['b'], True, True, False, False, False, 'c', ['T-Breaker'], False, False]],[['b_c_003', '水上第九院 シャコガイル', ['ムートピア'], 9, 1, 13000, ['b'], True, True, False, False, False, 'c', ['T-Breaker'], False, False]],[['b_c_003', '水上第九院 シャコガイル', ['ムートピア'], 9, 1, 13000, ['b'], True, True, False, False, False, 'c', ['T-Breaker'], False, False]],[['b_c_003', '水上第九院 シャコガイル', ['ムートピア'], 9, 1, 13000, ['b'], True, True, False, False, False, 'c', ['T-Breaker'], False, False]]]
    #アドバンス/オリジナルの選択
    advance=True
    screen.fill(fieldcolor)
    pygame.display.update()
    
    
    #デッキ選択
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
    save[0]=copy.deepcopy(Deck.get(deckname1))
    save[1]=copy.deepcopy(Deck.get(deckname2))
    #アドバンスかオリジナルだったりもするのでそれも判定する。
    if advance:
        temp=[]
        
        for cards in save[0]:
            break
    #禁断がある場合はここではじく
    save[0]=Shuffle(save[0])
    save[1]=Shuffle(save[1])
    print(save,file=codecs.open('GUI/etc/output.txt','w','utf-8'))
    #シールド展開
    screen.fill(fieldcolor)
    pygame.display.update()
    deck(screen,save[0],save[1])
    pygame.display.update()
    time.sleep(1)
    dimension(screen,save[12],save[13])
    if len(save[12])>0 or len(save[13])>0:
        time.sleep(1)
    grdeck(screen,save[14],save[15])
    if len(save[14])>0 or len(save[15])>0:
        time.sleep(1)
    #ここに禁断の処理
    
    #シールド展開
    sshield(screen)
    save=shieldplus(5,save,True)
    save=shieldplus(5,save,False)
    #最初のドロー
    save=draw(5,save,True)
    save=draw(5,save,False)
    #ゼーロンドロー
    if "d_z_001" in save[8]:
        save=draw(1,save,True)
    if "d_z_001" in save[9]:
        save=draw(1,save,False)
    #実行モード切り替え
    if mode==1:
        Easy(save,screen,log)
    else:
        Duel(save,screen,log)

#簡易版デュエル実行
def Easy(save,screen,log):
    #temp=[save,screen]
    emenu(screen)
    debug=3
    fflag=True #フィールドを表示している
    tflag=False #手札全体を見ている
    qflag=False #手札のカードを見ている
    dflag=False #デッキ枚数を確認中
    while True:
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
                        if 10<=y<=60:
                            fflag=False
                            showcards(save[4],screen,True)
                            tflag=True
                        elif 70<=y<=120:
                            save[4]=sorted(save[4])
                        elif 130<=y<=180:
                            save[4]=Shuffle(save[4])
                        elif 190<=y<=240:
                            save=swap(save)
                            recover(save,screen,debug)
                        elif 250<=y<=300:
                            a="b_s_002"
                            save=card[a](save,True)
                        #追加の余地
                        elif 730<=y<=780:
                            fflag=False
                            dmphelp(screen)
                            tflag=True
                        elif 790<=y<=840:
                            initalize(1)
                        elif 850<=y<=900:
                            fflag=False
                            showlog(screen,log)
                            tflag=True
                        elif 910<=y<=960:
                            pygame.quit()
                            sys.exit()
                    elif downbase[1]<=y<=downbase[1]+height:
                        #自分側デッキ
                        if downbase[0]<=x<=downbase[0]+width:
                            deckinfo(save,True,screen)
                            dflag=True
                            fflag=False
                        #自分側墓地
                        elif downbase[0]+10+width<=x<=downbase[0]+2*width+10:
                            fflag=False
                            tflag=True
                            showcards(save[10],screen,True)
                        #自分側超次元
                        elif downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                            fflag=False
                            tflag=True
                            showcards(save[12],screen,True)
                    elif downbase[1]+height+10<=y<=downbase[1]+2*height+10:
                        #自分側GRデッキ
                        if downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                            fflag=False
                            dflag=True
                            grdeckinfo(save,True,screen)
                        #自分側マナゾーン
                        elif upbase[0]-20-2*width<=x<=downbase[0]+10+2*width:
                            fflag=False
                            tflag=True
                            showcards(save[6],screen,True)
                    elif upbase[1]<=y<=upbase[1]+height:
                        #相手側デッキ
                        if upbase[0]<=x<=upbase[0]+width:
                            deckinfo(save,False,screen)
                            dflag=True
                            fflag=False
                        #相手側墓地
                        elif upbase[0]-10-width<=x<=upbase[0]-10:
                            fflag=False
                            tflag=True
                            showcards(save[11],screen,True)
                        #相手側超次元
                        elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                            fflag=False
                            tflag=True
                            showcards(save[13],screen,True)
                    elif upbase[1]-height-10<=y<=upbase[1]-10:
                        #相手側マナゾーン
                        if upbase[0]-10-width<=x<=downbase[0]+3*width+20:
                            fflag=False
                            tflag=True
                            showcards(save[7],screen,True)
                        #相手側GRゾーン
                        elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                            fflag=False
                            dflag=True
                            grdeckinfo(save,False,screen)
                elif tflag:
                    if 1420<=x<=1440 and 110<=y<=130:
                        tflag=False
                        fflag=True
                        recover(save,screen,debug)
                elif dflag:
                    if (downbase[0]+80<=x<=downbase[0]+100 and downbase[1]+110<=y<=downbase[1]+130) or (upbase[0]+80<=x<=upbase[0]+100 and upbase[1]+110<=y<=upbase[1]+130) or (downbase[0]+2*width+100<=x<=downbase[0]+2*width+120 and downbase[1]+120+height<=y<=downbase[1]+140+height) or (upbase[0]+60-2*width<=x<=upbase[0]+80-2*width and upbase[1]-height+100<=y<=upbase[1]-height+120):
                        dflag=False
                        fflag=True
                        recover(save,screen,debug)
            pygame.display.update()

#デュエル実行
def Duel(save,screen,log):
    #表示フラグ
    fflag=True #フィールドを表示している
    tflag=False #手札全体を見ている
    qflag=False #手札のカードを見ている
    dflag=False #デッキ枚数を確認中
    debug=2
    d1=True
    d2=True
    temp=[save,screen]
    menu(screen)
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
                        if debug==1:
                            if 10<=y<=60:
                                fflag=False
                                showcards(save[4],screen,True)
                                tflag=True
                            elif 70<=y<=120:
                                save[4]=sorted(save[4])
                            elif 130<=y<=180:
                                save=card["b_s_002"](save,True)
                            elif 190<=y<=240:
                                fflag=False
                                showcards(save[2],screen,True)
                                tflag=True
                            elif 250<=y<=300:
                                save=swap(save)
                                recover(save,screen,debug)
                                pygame.display.update()
                            elif 670<=y<=720:
                                debug=2
                                menu(screen)
                            elif 730<=y<=780:
                                fflag=False
                                dmphelp(screen)
                                tflag=True
                            elif 790<=y<=840:
                                initalize(2)
                            elif 850<=y<=900:
                                fflag=False
                                showlog(screen,log)
                                tflag=True
                            elif 910<=y<=960:
                                pygame.quit()
                                sys.exit()
                        else:
                            if 10<=y<=60:
                                fflag=False
                                showcards(save[4],screen,True)
                                tflag=True
                            elif 70<=y<=120:
                                save[4]=sorted(save[4])
                            elif 130<=y<=180:
                                save[4]=Shuffle(save[4])
                            elif 670<=y<=720:
                                debug=1
                                debugmenu(screen)
                            elif 730<=y<=780:
                                fflag=False
                                dmphelp(screen)
                                tflag=True
                            elif 790<=y<=840:
                                initalize(2)
                            elif 850<=y<=900:
                                fflag=False
                                showlog(screen,log)
                                tflag=True
                            elif 910<=y<=960:
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
                elif dflag:
                    if downbase[0]+80<=x<=downbase[0]+100 and downbase[1]+110<=y<=downbase[1]+130:
                        dflag=False
                        fflag=True
                        recover(save,screen,debug)
                    elif upbase[0]+80<=x<=upbase[0]+100 and upbase[1]+110<=y<=upbase[1]+130:
                        dflag=False
                        fflag=True
                        recover(save,screen,debug)
            pygame.display.update()

if __name__=="__main__":
    main()