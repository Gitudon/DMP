import json
file=open("build.json","r")
loading=json.load(file)
card=[0]*12 #要素が増えたら更新
i=0
for value in loading:
    card[i]=value
    i+=1
print(card)