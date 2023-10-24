from random import randint

t = ["Rock", "Paper", "Sissors"]

score = 0

def logic(score=score):
    computer = t[randint(0,2)]
    player = input("Rock , Paper , Sissors?\n")
    player = player.capitalize()
    print('\n')
    if player == computer:
        print("Tie")
        s = score + 0
    elif player == 'Rock':
        if computer == 'Paper':
            print('You Lose!','\n', computer, "covers", player)
            s = score - 1
        elif computer == 'Sissors':
            print("You Win!",'\n', player, "smashes", computer)
            s = score + 1
    elif player == 'Paper':
        if computer == 'Rock':
            print('You Lose!','\n', computer, "cut", player)
            s = score - 1
        elif computer == 'Sissors':
            print("You Win!",'\n', player, "covers", computer)
            s = score + 1
    elif player == 'Sissors':
        if computer == 'Paper':
            print('You Lose!','\n', computer, "smashes", player)
            s = score - 1
        elif computer == 'Rock':
            print("You Win!",'\n', player, "cut", computer)
            s = score + 1

    else:
        print("That's not a valid play. Check Your spelling!")
        print('\n')
        logic()
    print(s)
    print('\n')
    endLogic(s)

def endLogic(s):
    print('\n')
    r = input("Wanna Play again? Y/N \n")
    r = r.lower()
    if r == 'y':
        print('\n')
        logic(s)
    if r == 'n':
        return
    else:
        print('Somthing went wrong here, try again Please')
        endLogic(s)

logic()
    
