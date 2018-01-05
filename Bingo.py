import random
#Skapa tom lista som fylls på
list = []

# Generera Random siffra plus BINGO bokstav skicka tillbaka som svar
def bingoGen():
    #Plocka random siffra mellan 1-70
    rnumber = random.randint(1,70)
    #Gör om till string för att kunna sammanfoga
    rnumber = str(rnumber)

    #Plocka random bokstav ur BINGO
    rletter =random.choice('BINGO')

    # Sammanfoga och Skicka tillbaka värden
    gen = rletter + rnumber
    return (gen)



#Spela antal varv / räknar varv i loopen.
rolls = 0
inbing = 'no'
bingo = ['b', 'B']
print('Välkommen till Bingospelet du får göra egna brickor')

while inbing not in bingo and rolls < 280:
    # Åkalla funktion för random och spara i lista.
    seed = bingoGen()
    print(rolls)
    #print('dragigts innan:',list)
    #ifall dragningen är unik och inte dragits innan
    if seed not in list:
        #
        inbing = input('\nSpela bingo! skriv b for bingo:')
        #Break loop ifall du får bingo
        if inbing in bingo:
            print('BINGOOOOOOOO !')
            break
        print('dragits innan:', list)
        print('\n','Dragning:   ',seed)
        #lägger till dragningen i en lista över alla dragningar för att inte dra dubletter
        list.append(seed)
        #ökar bara om vi spelar dvs inte vid dublett
        rolls = rolls + 1
    #else:
    #    print('dublett!:', seed, 'rerolling')


print('Det tog:', rolls, 'dragningar att vinna')