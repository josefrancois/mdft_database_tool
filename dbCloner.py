import os

class DBCloner:
    def __init__(self, github_url, directory) :
        self.github_url = github_url
        self.directory = directory
        
    def write(self):
        with open('cloneDB.sh', 'w') as clone_file:
            clone_file.write("git clone " + self.github_url + '\n')
            arch_ext = ['.zip', '.tar.gz']
            if any(ext in self.directory for ext in arch_ext):
                clone_file.write("tar -xzvf $( ls -td -- ../mdft_project_clean/*/ | head -n 1 )/" + self.directory)
                return self.directory[:self.directory.find(arch_ext[[ext in self.directory for ext in arch_ext].index(True)])]
            else:
                clone_file.write("cp $( ls -td -- ../mdft_project_clean/*/ | head -n 1 )/" + self.directory + " .")
                return self.directory 
            
    def execute(self):
        os.system("bash cloneDB.sh")
         
