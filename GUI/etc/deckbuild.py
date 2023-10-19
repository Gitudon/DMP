import json
import codecs
file=open('DMP/GUI/etc/build.json','r',encoding="utf_8")
loading=json.load(file)
deck=[]
card=[0]*12  #要素が増えたら更新

li=[]
#ここに登録するデッキリストのパスを入れる
with open('DMP/GUI/decks/decklist.txt','r',encoding='utf-8') as f:
    li=f.read().split()

for names in li:
    i=0
    temp=loading[names]
    for vals in temp:
        card[i]=temp[vals]
        i+=1
    deck.append(card)
print(deck,file=codecs.open('DMP/GUI/etc/output.txt','w','utf-8'))