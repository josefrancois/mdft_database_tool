import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

HEIGHT_FIGSIZE = 7.0
WIDTH_FIGSIZE = 7.0
plt.style.use('classic')
plt.rcParams['figure.figsize'] = (7.0, 7.0)


class MdftPlotter:
    def __init__(self, db = None, plots_dir = None):
        self.database = db
        self.plots_dir = plots_dir
        
    def plotVS(self, x_column, y_column, x_label, y_label, unit):
        self.database.plot.scatter(x_column, y_column, c='black')
        limit_min = min(min(self.database[x_column]), min(self.database[y_column])) -2        
        limit_max = max(max(self.database[x_column]), max(self.database[y_column])) +2
        #print limit_min, limit_max
        plt.xlim(limit_min, limit_max)
        plt.ylim(limit_min, limit_max)
        plt.plot([limit_min,limit_max], [limit_min,limit_max], lw=0.5, color='black')
        rmse = np.sqrt(((self.database[y_column] - self.database[x_column]) ** 2).mean())
        #fit = np.polyfit(self.database[x_column], self.database[y_column], deg = 1)
        x = self.database[x_column]
        #plt.plot(x, fit[0] * x + fit[1], color='green', label="Fit equation : y = {1:.3f} + {0:.3f}x\n\tR$^2$  = {2:.3f} | RMSE = {3:.3f}"\
        #.format(fit[0], fit[1], self.database[x_column].corr(self.database[y_column]), rmse))
        #plt.title(title+" with {0} solutes".format(self.database.shape[0]), fontsize=8)
        plt.xlabel(x_label + " ({0})".format(unit))
        plt.ylabel(y_label + " ({0})".format(unit))
        #plt.annotate(s='mobley_5857', xy = (self.database.loc['mobley_5857'][x_column], self.database.loc['mobley_5857'][y_column]), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))
        plt.text(limit_min+abs(limit_min-limit_max)*0.23, limit_max-abs(limit_min-limit_max)*0.1, "RMSE = {1:.3f}\nPearson R$^2$  = {0:.3f}\nSpearman R$^2$ = {2:.3f}"\
        .format(self.database[x_column].corr(self.database[y_column]), rmse, self.database[x_column].corr(self.database[y_column], method = 'spearman')), ha='center', va='center', bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})
        #plt.legend(["R$^2$  = {0:.3f} | RMSE = {1:.3f}".format(self.database[x_column].corr(self.database[y_column]), rmse)], shadow = True, edgecolor = 'black', bbox_to_anchor=(1.7, 0.3))
        plt.savefig("./"+self.plots_dir+"/" + y_column + "VS" + x_column +".png", format="png", dpi = 130, bbox_inches='tight', edgecolor='black')
    
    def calcDiffs(self, ref_column, comp_columns_list, ref_label, comp_labels):
        diff_db = pd.DataFrame()
        diff_db_labels = []
        for comp_column in comp_columns_list:
            diff_db = pd.concat([diff_db, self.database[comp_column]-self.database[ref_column]], axis=1)
            diff_db_labels.append(comp_labels[comp_column] + ' - ' + ref_label)
        diff_db.columns = diff_db_labels
        return diff_db
        
    def plotErrorDistribution(self, errors_db, name):   
        plt.figure()          
        sns.violinplot(data=errors_db, orient='h').set_title("Error distribution (kcal/mol)"+" for {0} solutes".format(self.database.shape[0]))
        plt.savefig("./"+self.plots_dir+"/"+name+".png", format="png",bbox_inches='tight')
        
    def calcErrorGroups(self, x_column, y_columns_list, y_labels):
        db_groups = pd.DataFrame()
        error_groups = {}
        count_groups = {}
        rel_groups = {}
        labels_list = []
        
        for y_column in y_columns_list:
            for i, liste in enumerate(self.database['groups']):
                for group in liste:
                    count_groups[group] = 0
                    error_groups[group] = 0
                    error_groups[group] += abs(self.database[y_column][i]-self.database[x_column][i])
                    
            for liste in self.database['groups']:
                for group in liste:
                    count_groups[group] += 1

            for group in error_groups:
                rel_groups["({0}) ".format(count_groups[group])+group] = error_groups[group] / count_groups[group]

            db_groups = pd.concat([db_groups, pd.DataFrame.from_dict(rel_groups, orient='index')], axis=1)
            labels_list.append(y_labels[y_column])
            
        db_groups.columns = labels_list
        return db_groups
        
    def plotErrorGroups(self, db_groups):
        db_groups.plot.bar(figsize=(30,15), yticks=(range(0,10,2)))
        plt.ylabel('AUE (kcal/mol)')
        plt.title('Average Unsigned Error (AUE) due to functional groups with respect to Experiment relative to number of molecules')
        plt.savefig("./"+self.plots_dir+"/error_groups.png", format="png", bbox_inches='tight')
"""        
    def plotEnrichmentCurve(self, x_column, y_column):
        diff = abs(self.database[x_column] - self.database[y_column])
        diff_label = "{0}-{1}".format(x_column, y_column)
        sorted_diff = diff.sort_values()
        pc_db = pd.Series(np.arange(1,len(diff)+1), index=sorted_diff.index)/len(diff)*100
        enrichment_db = pd.concat([sorted_diff, pc_db], axis=1)
        enrichment_db.columns = [diff_label, '% ranked database']
        enrichment_db.plot(diff_label, "% ranked database", title = 'Enrichment curve', ylim=(0,100), xlim=(0, max(enrichment_db[diff_label])))
        plt.plot([0,max(enrichment_db[diff_label])], [0,max(enrichment_db['% ranked database'])]) 
        plt.savefig("./"+self.plots_dir+"/" + y_column + "-" + x_column+".png", format="png", dpi = 130)
"""        
    
        

