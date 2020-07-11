import numpy as np
from scipy.stats import weibull_min
from matplotlib import pyplot as plt



linestyles = ['-', '--', ':', '-.', '--']

class Effect():


    def weibull(self,stage):
        mu = 0
        x = np.linspace(-100, 100, 10000)
        fig, ax = plt.subplots(figsize=(5, 3.75))

        if stage == 0: #just started so wont have more impact 
            lam = 4
            k = 5
            plt.title("corona happend just now to mostly low effect" + str(stage))
        elif stage == 1:  #spreading stage
            lam = 1
            k = 3
            plt.title("corona is spreading stage and we have medium impact and more in next quaters"+ str(stage))
        elif stage == 4: # started and rapid
            lam = 1
            k = 2
            plt.title("corona is rapid"+ str(stage))
        else:  # end of corona soon we will b back to normal so exp distribution
            lam = 1
            k = 1 # exponential decay
            plt.title("corona cure is found and its decreasing at exponential stage"+ str(stage))


        for ls in linestyles:
            dist = weibull_min(k, mu, lam)
            plt.plot(x, dist.pdf(x), ls=ls, c='black')
        plt.xlim(0, 10)
        plt.ylim(0, 1)
        plt.xlabel('$x$')
        plt.ylabel(r'$p(x|k,\lambda)$') 
        plt.legend()
        plt.show()


eff  = Effect()
eff.weibull(1)
eff.weibull(2)
eff.weibull(3)
eff.weibull(4)