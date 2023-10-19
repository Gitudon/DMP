import json
import codecs
file=open('DMP/GUI/etc/cardlist.json','r',encoding="utf_8")
loading=json.load(file)
deck=[]
card=[]
li=[]
#ここに登録するデッキリストのパスを入れる
with open('DMP/GUI/decks/decklist.txt','r',encoding='utf-8') as f:
    li=f.read().split()
for names in li:
    temp=loading[names]
    for vals in temp:
        card.append(temp[vals])
    deck.append(card)
    card=[]
print(deck,file=codecs.open('DMP/GUI/etc/output.txt','w','utf-8'))