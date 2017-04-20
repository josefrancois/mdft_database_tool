import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')
plt.rcParams['figure.figsize'] = (7.0, 7.0)


class MdftPlotter:
    def __init__(self, db = None, plots_dir = None):
        self.database = db
        self.plots_dir = plots_dir
        
    def plotVS(self, x_column, y_column, x_label, y_label, unit, title):
        self.database.plot.scatter(x_column, y_column, figsize = (5,5))
        limit_min = min(min(self.database[x_column]), min(self.database[y_column])) -2        
        limit_max = max(max(self.database[x_column]), max(self.database[y_column])) +2
        #print limit_min, limit_max
        plt.xlim(limit_min, limit_max)
        plt.ylim(limit_min, limit_max)
        plt.plot([limit_min,limit_max], [limit_min,limit_max], lw=0.5)
        rmse = np.sqrt(((self.database[y_column] - self.database[x_column]) ** 2).mean())
        fit = np.polyfit(self.database[x_column], self.database[y_column], deg = 1)
        x = self.database[x_column]
        plt.plot(x, fit[0] * x + fit[1], color='green', label="Fit equation : y = {1:.3f} + {0:.3f}x\n\tR$^2$  = {2:.3f} | RMSE = {3:.3f}"\
        .format(fit[0], fit[1], self.database[x_column].corr(self.database[y_column]), rmse))
        plt.title(title, fontsize=8)
        plt.xlabel(x_label + " ({0})".format(unit))
        plt.ylabel(y_label + " ({0})".format(unit))
        plt.legend(shadow = True, edgecolor = 'black', bbox_to_anchor=(1, 0.5))
        plt.savefig("./"+self.plots_dir+"/" + y_column + "VS" + x_column +".png", format="png", dpi = 130, bbox_inches='tight', edgecolor='black')
        
    def plotEnrichmentCurve(self, x_column, y_column):
        diff = abs(self.database[x_column] - self.database[y_column])
        diff_label = "{0}-{1}".format(x_column, y_column)
        sorted_diff = diff.sort_values()
        pc_db = pd.Series(np.arange(1,len(diff)+1), index=sorted_diff.index)/len(diff)*100
        enrichment_db = pd.concat([sorted_diff, pc_db], axis=1)
        enrichment_db.columns = [diff_label, '% ranked database']
        enrichment_db.plot(diff_label, "% ranked database", title = 'Enrichment curve', ylim=(0,100), xlim=(0, max(enrichment_db[diff_label])))
        plt.plot([0,max(enrichment_db[diff_label])], [0,max(enrichment_db['% ranked database'])]) 
        plt.savefig("./"+self.plots_dir+"/" + y_column + "-" + x_column, format="png", dpi = 130)

        

