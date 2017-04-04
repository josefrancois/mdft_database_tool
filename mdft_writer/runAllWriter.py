import json

class runAllWriter:
	def __init__(self, paramfile = None)
		self.param_file = param_file
		
	def write(self, folder, server_name):
		with open(self.param_file, 'r') as json_param:
			serv_param = json.load(json_param)
			
		with open("runAll.sh", 'r') as frun_in:
			lines = frun_in.readlines()
			for i, line in enumerate(lines):
				if ".do" in line:
					lines[i] = serv_param[server_name][runCmd] + ' ' + serv_param[server_name][jobFile] + '\n'
		
		with open("runAll.sh", 'w') as frun_out:
			frun_out.write(lines)
