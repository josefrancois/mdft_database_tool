import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (7.0, 7.0)

class MdftPlotter:
    def __init__(self, db = None):
        self.database = db
    
    def plotVS(self, x_column, y_column, x_label, y_label):
        self.database.plot.scatter(x_column, y_column, figsize = (5,5))
        x = self.database[x_column]
        plt.xlim(-30, 5)
        plt.ylim(-30, 5)
        plt.plot(range(-30, 6), range(-30,6), lw=2)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend(['Correlation Coefficient  = {:.3f}'.format(self.database[x_column].corr(self.database[y_column]))], shadow = True, edgecolor = 'black')
        plt.savefig(y_column + "VS" + x_column  + ".pdf", format="pdf", dpi=1000)

        

