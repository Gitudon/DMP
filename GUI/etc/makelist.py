#辞書
import carddict

#カード名と枚数を受け取って入力する
def main():
    deck=[]
    while True:
        key=input("カード名を入力/終了なら'z'と入力> ")
        if key=="z":
            break
        if key in carddict.dic:
            value=carddict.dic[key]
            num=int(input("枚数を入力> "))
            for _ in range(num):
                deck.append(value)
        else:
            print("カードが存在しません。")
    print(*deck)

if __name__=="__main__":
    main()