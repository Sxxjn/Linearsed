from random import *

o=-1
sõnad=["hello","cat","cow","mouse","hen","lizard","uncle","apple","wasp","fly","lucky","fish","horse","goat","pig"]
rnd=choice(wrds)
rndlist=list(rnd)
k=len(rndlist)
for i in range(0,6,1):
    o-=1
    print("Guess the word. You have ", 6-i,"attempts")
    answer=input("[] "*k)
    answerlist=list(answer)
    for a in range(0,k,1):
        o+=1
        if answerlist[o]==rndlist[o]:
            print(answerlist[o],end=" ")
        else:
            print("*",end=" ")
    print()
    if answer==rnd:
        print("Correct! the word was ", rnd, )
        break
    else:
        print("Wrong! ", 6-i-1, "attemps remains")