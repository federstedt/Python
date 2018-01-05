import random
#Create empty array to be populated
list = []

# Generate random number and letter from the word BINGO and return answer
def bingoGen():
    #Pick a random number between 1-70
    rnumber = random.randint(1,70)
    #Make inteter a string to be able to put the values together with letter below
    rnumber = str(rnumber)

    #pick a random letter BINGO
    rletter =random.choice('BINGO')

    # put the strings together and return
    gen = rletter + rnumber
    return (gen)



#Keeps count of number of loops
rolls = 0
inbing = 'no'
bingo = ['b', 'B']
#input b if you get BINGO
print('Välkommen till Bingospelet du får göra egna brickor')

while inbing not in bingo and rolls < 280:
    # Call function that generates bingo-values
    seed = bingoGen()
    print(rolls)
    #print('dragigts innan:',list)
    #check if the returned values are unique and not been drawn before
    if seed not in list:
        #
        inbing = input('\nSpela bingo! skriv b for bingo:')
        #Break loop if you get bingo
        if inbing in bingo:
            print('BINGOOOOOOOO !')
            break
        print('dragits innan:', list)
        print('\n','Dragning:   ',seed)
        #add values to a list that we check next time to make sure it is unique
        list.append(seed)
        #increses by 1 to keep track of loops
        rolls = rolls + 1
    #else:
    #    print('dublett!:', seed, 'rerolling')


print('Det tog:', rolls, 'dragningar att vinna')
