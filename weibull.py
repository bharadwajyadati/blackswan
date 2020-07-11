import numpy as np
from scipy.stats import weibull_min
from matplotlib import pyplot as plt


"""
    corona effect can be modelled rather than single value
    but by a pdf that varies with time and taking as_of_today as variable parameter 
    find the effect which will be reducing w.r.t time since it maybe cured :D , needs to be 

    we even got few hyper paremeters which will be impact factors ?

    k and lamdba values  needs to be fixed    

"""



#k_values = [0.5, 1, 2, 2] # if the values of k are 1 and 2 they follow to expon and reylein 
#lam_values = [1, 1, 1, 2]

k_values = [0.5, 1, 2, 4] # 
lam_values = [1, 1, 1, 4]
linestyles = ['-', '--', ':', '-.', '--']
mu = 0
x = np.linspace(-100, 100, 10000)

print("every value from possible distribution , we just need to take weighted avg of it")
fig, ax = plt.subplots(figsize=(5, 3.75))

for (k, lam, ls) in zip(k_values, lam_values, linestyles):
    dist = weibull_min(k, mu, lam)
    #print(x)
    print(dist.pdf(x))
    plt.plot(x, dist.pdf(x), ls=ls, c='black',
             label=r'$k=%.1f,\ \lambda=%i$' % (k, lam))

plt.xlim(0, 10)
plt.ylim(0, 1)

plt.xlabel('$x$')
plt.ylabel(r'$p(x|k,\lambda)$')
plt.title('Weibull Distribution w.r.t to time ')

plt.legend()
plt.show()