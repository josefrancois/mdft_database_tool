import json

class runAllWriter:
    "Definition of a runAll.sh writer in order to launch MDFT with the correct .do files"       
    def __init__(self):
        with open("./references/parameters/serversParam.json", 'r') as json_param:
            self.serv_param = json.load(json_param)
                
    def write(self, server_name, commit_hash, folder):                 
        with open("./references/runAll_file/runAll.sh", 'r') as frun_in: #Going from a runAll.sh model file...
            lines = frun_in.readlines()
            for i, line in enumerate(lines):
                if ".do" in line: #Add the right shell command according to the server
                    lines[i] = "\t    " + self.serv_param[server_name]["runCmd"] + ' ' + self.serv_param[server_name]["jobFile"] + '\n'
                elif "git clone" in line and commit_hash != None:  #Add the possibility to clone MDFT for Github with a specific commit
                    lines.insert(i+2, "    git checkout " + commit_hash + "\n")
                
        #...to generate the correct runAll.sh
        with open(folder + "runAll.sh", 'w') as frun_out:
            frun_out.write("".join(lines))
            

    def getDoFile(self, server_name):
        return self.serv_param[server_name]["jobFile"]
