import random 
def probability():
    balls=['red','blue','green']
    result=random.choice(balls)

    prob=balls.count('red')/len(balls)
    print('probability of picking a red ball is', prob)
    if result=='red':
        return "The red ball got picked"
    else:
        return "Better Luck Next Time"
    
res = probability()
print(res)