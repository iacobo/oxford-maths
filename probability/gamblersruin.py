import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

def gamblerWalk(start=10,n=100,m=10,p=0.5,win=1,lose=-1,llim=0,ulim=None):
    """Simulate m trials of a gambler's walk of length n with starting amount
    £10, probability of success p, £win on win, and £lose on lose.
    Walk ends if walk reaches lower/upper limits llim or ulim."""
    
    x = np.arange(n)
    Y = np.random.choice([win,lose], size=(m,n), p=[p,1-p])
    Y[:,0] = start
    Y = np.cumsum(Y, axis=1)
    
    # Flatten score once reaches lower/upper limit
    for i, y in enumerate(Y):
        if llim in y:
            y[list(y).index(llim):] = llim
        if ulim and ulim in y:
            y[list(y).index(ulim):] = ulim
        
        Y[i] = y
        # Plot walk
        plt.plot(x,y)
    
    # Annotate plot
    plt.title("Gambler's Ruin")
    plt.xlabel("Number of steps")
    plt.ylabel("Winnings")
    
    return Y

if __name__ == "__main__":
    gamblerWalk()
