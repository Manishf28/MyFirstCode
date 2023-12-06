import random
print('--*  GUESS THE NUMBER  *--')
list1 = [i for i in range(1, 11)]
Number = random.choice(list1)
chance = 3

while (chance != 0):
    Guess = int(input('Guess correct number in range 1  to 10 :-\n'))
    if (Guess == Number):
        print("Woooooohhhh___!! \n YOU GUESS CORRECT NUMBER  \n --*  YOU WIN  *--  ",Number)
        break
    elif(chance!=0):
        chance -= 1
        print('Incorrct Guess')
        print('Chances Left : ', chance)
        if(chance==0): 
            print('***  You Loose  ***')
            print("All the chancess are exhousted")
            print('The correct word is : ', Number)
print('--*  Game Over  *--')