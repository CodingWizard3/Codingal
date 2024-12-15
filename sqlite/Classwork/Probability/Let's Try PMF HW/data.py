import scipy.stats as stats 
x = 2 
n=10
y=4
prob_1=stats.binom.pmf(x, n, 0.5)
print("Probability of getting 2 heads")
print(prob_1) 

prob_2=stats.binom.pmf(y, n, 0.5)
print("Probability of getting 4 heads")
print(prob_2)