import json
import codecs
def build(path):
    file=open('DMP/GUI/game/cardlist.json','r',encoding="utf_8")
    loading=json.load(file)
    deck=[]
    card=[]
    li=[]
    with open(path,'r',encoding='utf-8') as f:
        li=f.read().split()
    for names in li:
        temp=loading[names]
        for vals in temp:
            card.append(temp[vals])
        deck.append(card)
        card=[]
    print(deck,file=codecs.open('DMP/GUI/etc/output.txt','w','utf-8'))
    return deck