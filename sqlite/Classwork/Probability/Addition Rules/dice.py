def prob(a, b, events):

    set_a= len(a)/len(events)
    set_b = len(b)/len(events)

    inter = a.intersection(b)
    prob_inter=len(inter)/len(events)

    return(set_a + set_b - prob_inter)

evens={2,4,6}
twoplus={3,4,5,6}
roll_events={1,2,3,4,5,6}
print('probability getting an ans in any of the sets are',prob(evens,twoplus,roll_events))