import scipy.stats as stats
n=10
prob1=1-stats.binom.cdf(6,n,0.500001)
print('The probability of getting more than six heads in ten flips is ',prob1)

prob2=stats.poisson.pmf(6,10)
print('The probability of getting six days of rain is ',prob2)

prob3=stats.poisson.pmf(12,10)+stats.poisson.pmf(13,10)+stats.poisson.pmf(14,10)
print('The probability of getting between 12 and 14 days of rain is ',prob3)

prob4=1-stats.poisson.cdf(20,15)
print('The probability of getting more than 20 calls is ',prob4)

prob5=stats.poisson.cdf(21,15)-stats.poisson.cdf(16,15)
print('The probability of getting between 17 and 21 calls is ',prob5)