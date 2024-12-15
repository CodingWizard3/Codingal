import random 
def balls():
    options=['red','blue','blue','blue','blue','blue','blue','white','white','white']
    chance=random.choice(options)

    prob=options.count('white')/len(options)
    print('probability of picking a white ball is', prob)
    if chance=='white':
        return "You got a White Ball!!!"
    else:
        return "Wah Wah Waaaaaaaahhhhh"
    
luck = balls()
print(luck)