import matplotlib.pyplot as plt
import numpy as np

class MdftPlotter:
	def __init__(self, x = [], y = []):
		self.x = np.array(x)
		self.y = np.array(y)
		
	def plot(self, plot_title, x_legend, y_legend):
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(self.x, self.y, "ro")
		lims = [np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()])]
		ax.plot(lims, lims, 'b-', alpha=0.75, zorder=0)
		ax.set_title(plot_title)
		ax.set_xlabel(x_legend)
		ax.set_ylabel(y_legend)	
		corr_coeff = np.corrcoef(self.x, self.y)[0,1]
		ax.text(np.min([ax.get_xlim(), ax.get_ylim()]), np.max([ax.get_xlim(), ax.get_ylim()]), r'R2 = {:.3f}'.format(corr_coeff), fontsize=12)
		plt.grid()
		plt.show()

