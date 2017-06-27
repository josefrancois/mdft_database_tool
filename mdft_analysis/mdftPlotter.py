import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

HEIGHT_FIGSIZE = 7.0
WIDTH_FIGSIZE = 7.0
plt.style.use('classic')
plt.rcParams['figure.figsize'] = (7.0, 7.0)
plt.rcParams['axes.labelsize'] = 20

class MdftPlotter:
    def __init__(self, db = None, plots_dir = None):
        self.database = db
        self.plots_dir = plots_dir
        
    def plotVS(self, x_column, y_column, x_label, y_label, unit):
        self.database.plot.scatter(x_column, y_column, c='black')
        limit_min = min(min(self.database[x_column]), min(self.database[y_column])) -2        
        limit_max = max(max(self.database[x_column]), max(self.database[y_column])) +2
        plt.xlim(limit_min, limit_max)
        plt.ylim(limit_min, limit_max)
        plt.plot([limit_min,limit_max], [limit_min,limit_max], lw=0.5, color='black')
        rmse = np.sqrt(((self.database[y_column] - self.database[x_column]) ** 2).mean())
        rsr = rmse/self.database[x_column].std()
        pearson_r = self.database[x_column].corr(self.database[y_column])
        spearman_rho = self.database[x_column].corr(self.database[y_column], method = 'spearman')
        kendall_tau = self.database[x_column].corr(self.database[y_column], method = 'kendall')
        r2 = pearson_r**2
        x = self.database[x_column]
        #plt.title(title+" with {0} solutes".format(self.database.shape[0]), fontsize=8)
        plt.xlabel("$\mathrm{\mathsf{\Delta G^{"+x_label+"}_{solv}}}$" + " ({0})".format(unit), fontsize=16)
        plt.ylabel("$\mathrm{\mathsf{\Delta G^{"+y_label+"}_{solv}}}$" + " ({0})".format(unit), fontsize=16)
        #for mol in self.database.index:
        #    plt.annotate(s=mol, xy = (self.database.loc[mol][x_column], self.database.loc[mol][y_column]), xytext=(self.database.loc[mol][x_column]+2, self.database.loc[mol][y_column]-1))
        
        pbias = 0
        for i in range(self.database.shape[0]):
            pbias += (self.database[x_column][i] - self.database[y_column][i])*100
        pbias = pbias / self.database[x_column].sum()
            
        plt.text(limit_min+abs(limit_min-limit_max)*0.23, limit_max-abs(limit_min-limit_max)*0.15, \
        "RMSE = {0:.2f} {9:s}\n P Bias = {1:.2f} %\nPearson R = {2:.2f}\nSpearman {3:s} = {4:.2f}\nKendall {5:s} = {6:.2f}\nR{7:s} = {8:.2f}"\
        .format(rmse, pbias, pearson_r, r'$\rho$', spearman_rho, r'$\tau$', kendall_tau, r'$^2$', r2, unit), ha='center', va='center', bbox={'facecolor':'white', 'alpha':0.5, 'pad':10})       
        plt.savefig(self.plots_dir+"/"+"correlation__"+ y_column + "__vs__" + x_column +".png", format="png", dpi = 200, bbox_inches='tight', edgecolor='black')
    
    def calcDiffs(self, ref_column, comp_columns_list, ref_label, comp_labels):
        diff_db = pd.DataFrame()
        diff_db_labels = []
        for comp_column in comp_columns_list:
            diff_db = pd.concat([diff_db, self.database[comp_column]-self.database[ref_column]], axis=1)
            diff_db_labels.append("$\mathrm{\Delta G^{"+comp_labels[comp_column]+"}_{solv}}$" + ' - ' + "$\mathrm{\Delta G^{"+ref_label+"}_{solv}}$")
        diff_db.columns = diff_db_labels
        return diff_db
        
    def plotErrorDistribution(self, errors_db, name):   
        plt.figure()         
        sns.violinplot(data=errors_db, orient='h',zorder=1, split=True)
        plt.xlim(-20, 20)
        plt.axvline(0, color = 'black', linestyle='dotted', linewidth=0.7)
        plt.savefig("./"+self.plots_dir+"/"+name+".png", format="png",bbox_inches='tight')
        
    def calcErrorby(self, x_column, y_columns_list, y_labels, cat_column):
        db_by = pd.DataFrame()
        error_by = {}
        count_by = {}
        rel_by = {}
        labels_list = []
        
        for y_column in y_columns_list:
            for i, liste in enumerate(self.database[cat_column]):
                for category in liste:
                    count_by[category] = 0
                    error_by[category] = 0
                    error_by[category] += abs(self.database[y_column][i]-self.database[x_column][i])
                    
            for liste in self.database[cat_column]:
                for category in liste:
                    count_by[category] += 1

            for category in error_by:
                if category != '':
                    rel_by["({0}) ".format(count_by[category])+category] = error_by[category] / count_by[category]

            db_by = pd.concat([db_by, pd.DataFrame.from_dict(rel_by, orient='index')], axis=1)
            labels_list.append(y_labels[y_column])
            
        db_by.columns = labels_list
        db_by = db_by.sort_values(by=labels_list[-1], ascending=True)
        return db_by
        
        
    def plotErrorby(self, db_by, cat_column):
        db_by[db_by.index != ''].plot.barh(figsize=(15,25), xticks=(range(0,8)))
        plt.ylabel('AUE (kcal/mol)')
        plt.legend(loc='lower right')
        #plt.title('Average Unsigned Error (AUE) due to functional by with respect to Experiment relative to number of molecules')
        plt.savefig("./"+self.plots_dir+"/error_by_"+cat_column+".png", format="png", bbox_inches='tight')
        
    def calcPbiasby(self, x_column, y_columns_list, y_labels, cat_column):
        db_pbias_by = pd.DataFrame()
        error100_by = {}
        sum_x_column_by = {}
        count_by = {}
        pbias_by = {}
        labels_list = []
        
        for y_column in y_columns_list:
            for i, liste in enumerate(self.database[cat_column]):
                for category in liste:
                    sum_x_column_by[category] = 0
                    count_by[category] = 0
                    error100_by[category] = 0
                    error100_by[category] += (self.database[x_column][i]-self.database[y_column][i])*100
                    sum_x_column_by[category] += self.database[x_column][i]
                    
            for liste in self.database[cat_column]:
                for category in liste:
                    count_by[category] += 1

            for category in error100_by:
                pbias_by["({0}) ".format(count_by[category])+category] = error100_by[category] / sum_x_column_by[category]
                #print category, error100_by[category], sum_x_column_by[category]    
            db_pbias_by = pd.concat([db_pbias_by, pd.DataFrame.from_dict(pbias_by, orient='index')], axis=1)
            labels_list.append(y_labels[y_column])
            
        db_pbias_by.columns = labels_list
        return db_pbias_by
        
    def plotPbiasby(self, db_pbias_by, cat_column):
        db_pbias_by.plot.bar(figsize=(30,15)) #yticks=(range(0,10,2))
        plt.ylabel('Pbias (%)')
        plt.title('Pbias due to functional by with respect to Experiment relative to number of molecules')
        plt.savefig("./"+self.plots_dir+"/pbias_by_"+cat_column+".png", format="png", bbox_inches='tight')
        
     
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
    
        

