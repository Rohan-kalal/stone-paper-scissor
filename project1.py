import random

def playerwin(comp,player):
    if comp==player:
        return None
    elif comp == 's':
        if player == 'p':
            return True
        elif player=='sci':
            return False
    elif comp == 'p':
        if player == 'sci':
            return True
        elif player=='stone':
            return False
    elif comp == 'sci':
        if player == 'p':
            return True
        elif player=='s':
            return False
print("comp turn:stone(s) paper(p) scissor(sci)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='p'
elif randNo==3:
    comp='sci'


player=input("player' turn: stone(s) paper(p) scissor(sci)")
a=playerwin(comp,player)

print(f"computer choose {comp}")
print(f"player choose {player}")
if a==None:
    print("The game is tie")
elif a:
    print("player win")
else :
    print("player loose")
