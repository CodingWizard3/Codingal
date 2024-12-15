def probability(x,y):
    if x==1:
        prob_f=0.3
        if b==1:
            prob_dine=0.75
        else:
            prob_dine=0.25
    elif x==2:
        prob_f=0.7
        if b==1:
            prob_dine=0.6
        else:
            prob_dine=0.4
    prob_f_n_d=prob_f*prob_dine
    return prob_f_n_d


print('Probability Check Enter your Choice: ')
print('Is This Student A Freshman??? \n1.Yes \n2.No')
a=int(input("Enter your choice: (1/2): "))
print('Is This Student Eating In The Canteen??? \n1. Yes \n2.No')
b=int(input("Enter your choice: (1/2):"))
print('Probability of both events occuring is',probability(a,b))