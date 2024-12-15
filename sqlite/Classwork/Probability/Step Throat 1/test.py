def test(a,b):
    if a==1:
        prob_a=0.2
        if b==1:
            prob_bga=0.85
        elif b==2:
            prob_bga=0.15
        else:
            print('God, wrong Universe!')
        print("Probabiilty of B given A",prob_bga)
        print("Prob. of both events occuring", prob_a*prob_bga)

    
    if a==2:
        prob_a=0.8
        if b==1:
            prob_bga=0.02
        elif b==2:
            prob_bga=0.982
            
        else:
            print('God, wrong Universe!')
        print("Probabiilty of B given A",prob_bga)
        
        print("Prob. of both events occuring", prob_a*prob_bga)
        
a= int(input("Person has strep throat? \n1. Yes 2. No"))

b= int(input("Person is positive? \n1. Yes 2. No"))
test(a,b)