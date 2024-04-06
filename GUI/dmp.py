import pygame
import sys
import time
import json
import pickle
import copy
import codecs
from game.func import Shuffle,showcards,draw,recover,deck,sshield,shieldplus,grdeck,dimension,deckinfo,dmphelp,decklist,swap,grdeckinfo,choose,showlog,showmanazone,showbattlezone,expand,seal,showshield,addmana,bochiokuri,gotodeck,grsummon
from game import carddic
from game import deckdic
from game import deckbuild

width=100
height=144
field=(1550,1000)
fieldcolor=(0,200,0)
upbase=(230, 155)
downbase=(920, 696)
card=carddic.card
Deck=deckdic.Deck
logpath='GUI/etc/log.txt'

def main():
    logger=[]
    for i in range(30):
        path='GUI/decks/deck'+str(i)+'.txt'
        name='deck'+str(i)
        Deck[name]=deckbuild.build(path)
        logger.append(Deck[name])
    with open('GUI/etc/out/deckout.txt','w', encoding='utf-8') as o:
        for log in logger:
            print(log, file=o)
    initalize()

def initalize():
    log=[]
    pygame.init() 
    screen = pygame.display.set_mode(field)
    pygame.display.set_caption("Duel Masters")
    #デッキのリスト01、シールドのリスト23、手札のリスト45、マナのリスト67、バトルゾーンのリスト89、墓地のリスト1011、超次元ゾーンのリスト1213、GRゾーンのリスト1415
    save=[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    screen.fill(fieldcolor)
    pygame.display.update()
    advance=choose(screen,"フォーマットはアドバンスにしますか？")
    screen.fill(fieldcolor)
    pygame.display.update()
    mode=choose(screen,"簡易モードで実行しますか？")
    screen.fill(fieldcolor)
    pygame.display.update()
    deckname1=decklist(screen,True)
    deckname2=decklist(screen,False)
    tmp1=copy.deepcopy(Deck.get(deckname1))
    tmp2=copy.deepcopy(Deck.get(deckname2))
    if advance:
        for cards in tmp1:
            if any(substring in cards[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_","_rp_"]):
                save[12].append(cards)
            elif "_grc_" in cards[0]:
                save[14].append(cards)
            elif any(substring in cards[0] for substring in ["_k_", "_kf_","_zg_","_zs_"]):
                expand(save,cards,True)
            else:
                save[0].append(cards)
        for cards in tmp2:
            if any(substring in cards[0] for substring in ["_d_", "_dw_", "_df_", "_dc_", "_ds_", "_ed_", "_rp_"]):
                save[13].append(cards)
            elif "_grc_" in cards[0]:
                save[15].append(cards)
            elif any(substring in cards[0] for substring in ["_k_", "_kf_", "_zg_","_zs_"]):
                expand(save,cards,False)
            else:
                save[1].append(cards)
    save[0]=Shuffle(save[0])
    save[1]=Shuffle(save[1])
    if advance:
        save[14]=Shuffle(save[14])
        save[15]=Shuffle(save[15])
    print(save,file=codecs.open('GUI/etc/out/savelog.txt','w','utf-8'))
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
    if advance and save[8]!=[]:
        if "d_z_001" in save[8][0][0]:
            save=draw(1,save,True)
        elif "r_k_001" in save[8][0][0]:
            for _ in range(6):
                save=seal(save,True,0)
        elif "rd_kf_001" in save[8][0][0]:
            for _ in range(4):
                save=seal(save,True,0)
    if advance and save[9]!=[]:
        if "d_z_001" in save[9][0][0]:
            save=draw(1,save,False)
        elif "r_k_001" in save[9][0][0]:
            for _ in range(6):
                save=seal(save,False,0)
        elif "rd_kf_001" in save[9][0][0]:
            for _ in range(4):
                save=seal(save,False,0)
    sshield(screen)
    if mode==True:
        Easy(save,screen,log)
    else:
        Duel(save,screen,log)

def Easy(save,screen,log):
    debug=3
    save=shieldplus(5,save,True,screen,debug,False)
    save=shieldplus(5,save,False,screen,debug,False)
    save=draw(5,save,True)
    save=draw(5,save,False)
    recover(save,screen,debug)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 1260<=x<=1540:
                    if 10<=y<=60:
                        showcards(save,screen,True,4,debug)
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
                    elif 310<=y<=360:
                        showcards(save,screen,True,0,debug)
                    elif 370<=y<=420:
                        save[0]=Shuffle(save[0])
                    elif 430<=y<=480:
                        showshield(save,screen,True,2,debug)
                    elif 490<=y<=540:
                        save=addmana(1,save,True,False,screen,debug)
                    elif 550<=y<=600:
                        save=bochiokuri(1,save,True,screen,debug)
                    elif 610<=y<=660:
                        tmp=save[0][0]
                        save[0]=save[0][1:]
                        save=gotodeck(save,True,tmp,False)
                    elif 670<=y<=720:
                        save=grsummon(1,save,True,screen,debug)
                    elif 730<=y<=780:
                        save=shieldplus(1,save,True,screen,debug,True)
                    elif 790<=y<=840:
                        initalize()
                    elif 850<=y<=900:
                        showlog(screen,log,save,debug)
                    elif 910<=y<=960:
                        pygame.quit()
                        sys.exit()
                elif downbase[1]<=y<=downbase[1]+height:
                    #自分側デッキ
                    if downbase[0]<=x<=downbase[0]+width:
                        deckinfo(save,True,screen,debug)
                    #自分側墓地
                    elif downbase[0]+10+width<=x<=downbase[0]+2*width+10:
                        showcards(save,screen,True,10,debug)
                    #自分側超次元
                    elif downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                        showcards(save,screen,True,12,debug)
                elif downbase[1]+height+10<=y<=downbase[1]+2*height+10:
                    #自分側GRデッキ
                    if downbase[0]+20+2*width<=x<=downbase[0]+3*width+20:
                        grdeckinfo(save,True,screen,debug)
                    #自分側マナゾーン
                    elif upbase[0]-20-2*width<=x<=downbase[0]+10+2*width:
                        showmanazone(save,screen,True,6,debug)
                elif downbase[1]-10-height<=y<=downbase[1]-10:
                    if upbase[0]-2*(width+10)<=x<=downbase[0]+20+3*width:
                        #自分側バトルゾーン
                        showbattlezone(save,screen,True,8,debug)
                elif upbase[1]+10+height<=y<=upbase[1]+10+2*height:
                    if upbase[0]-2*(width+10)<=x<=downbase[0]+20+3*width:
                        #相手側バトルゾーン
                        showbattlezone(save,screen,True,9,debug)
                elif upbase[1]<=y<=upbase[1]+height:
                    #相手側デッキ
                    if upbase[0]<=x<=upbase[0]+width:
                        deckinfo(save,False,screen,debug)
                    #相手側墓地
                    elif upbase[0]-10-width<=x<=upbase[0]-10:
                        showcards(save,screen,True,11,debug)
                    #相手側超次元
                    elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                        showcards(save,screen,True,13,debug)
                elif upbase[1]-height-10<=y<=upbase[1]-10:
                    #相手側マナゾーン
                    if upbase[0]-10-width<=x<=downbase[0]+3*width+20:
                        showmanazone(save,screen,True,7,debug)
                    #相手側GRゾーン
                    elif upbase[0]-20-2*width<=x<=upbase[0]-20-width:
                        grdeckinfo(save,False,screen,debug)
            pygame.display.update()

#デュエル実行
def Duel(save,screen,log):
    sys.exit()

if __name__=="__main__":
    main() 