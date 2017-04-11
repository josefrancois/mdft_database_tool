import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (7.0, 7.0)

class MdftPlotter:
    def __init__(self, db = None):
        self.database = db
    
    def plotVS(self, x_column, y_column, x_label, y_label, title):
        self.database.plot.scatter(x_column, y_column, figsize = (5,5))
        limit_min = min(min(self.database[x_column]), min(self.database[y_column])) -10        
        limit_max = max(max(self.database[x_column]), max(self.database[y_column])) +10
        #print limit_min, limit_max
        plt.xlim(limit_min, limit_max)
        plt.ylim(limit_min, limit_max)
        plt.plot([limit_min,limit_max], [limit_min,limit_max], lw=2)
        fit = np.polyfit(self.database[x_column], self.database[y_column], deg = 1)
        x = self.database[x_column]
        plt.plot(x, fit[0] * x + fit[1], color='green')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(["Ideal","Fit equation : y = {1:.3f} + {0:.3f}x\n\t==> R$^2$  = {2:.3f}".format(fit[0], fit[1],self.database[x_column].corr(self.database[y_column]))], shadow = True, edgecolor = 'black')
        plt.savefig("./mdft_plots/" + y_column + "VS" + x_column  + ".pdf", format="pdf", dpi=1000)

        

