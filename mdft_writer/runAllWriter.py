import json

class runAllWriter:      
           def __init__(self):
                                 with open("serversParam.json", 'r') as json_param:
                                                       self.serv_param = json.load(json_param)
                                 
           def writeRunCmd(self, server_name):                
                      with open("runAll.sh", 'r') as frun_in:
                                 lines = frun_in.readlines()
                                 for i, line in enumerate(lines):
                                            if ".do" in line:
                                                       lines[i] = "\t    " + self.serv_param[server_name]["runCmd"] + ' ' + self.serv_param[server_name]["jobFile"] + '\n'
                                                       print i, lines
                      
                      with open("runAll.sh", 'w') as frun_out:
                                 frun_out.write("".join(lines))

           def getDoFile(self, server_name):
                                 return self.serv_param[server_name]["jobFile"]
