import random 
def ludo():
    options=[1,2,3,4,5,6]
    chance=random.choice(options)

    prob=options.count(6)/len(options)
    print('probability of rolling a 6 is', prob)
    if chance==6:
        return "You rolled a SIX!!!"
    else:
        return "Wah Wah Wah "
    
luck = ludo()
print(luck)

#EEEEEAAAASSSYYY