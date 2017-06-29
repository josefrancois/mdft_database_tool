import os

class DBCloner:
    def __init__(self, github_url, directory) :
        self.github_url = github_url
        self.directory = directory
        self.commit_hash = None
        self.ref_file = None
        
    def write(self):
        with open('cloneDB.sh', 'w') as clone_file: # Generation of a bash script to clone the database and copy the wanted files in the current directory
            clone_file.write("git clone " + self.github_url + '\n')
            if self.commit_hash != None:
                clone_file.write("git checkout " + self.commit_hash + '\n')
                
            if self.ref_file != None :
                clone_file.write("cp $( ls -td -- $( pwd )/*/ | head -n 1 )/" + self.ref_file + " ." + '\n')
                
            arch_ext = ['.zip', '.tar.gz']
            if any(ext in self.directory for ext in arch_ext):
                clone_file.write("tar -xzvf $( ls -td -- $( pwd )/*/ | head -n 1 )/" + self.directory)
                return self.directory[:self.directory.find(arch_ext[[ext in self.directory for ext in arch_ext].index(True)])]
            else:
                clone_file.write("cp $( ls -td -- $( pwd )/*/ | head -n 1 )/" + self.directory + " .")
                return self.directory
                   
            
    def execute(self):
        os.system("bash cloneDB.sh")
        
    def setCommitHash(self, commit_hash):
        self.commit_hash = commit_hash
        
    def setRefFile(self, ref_file):
        self.ref_file = ref_file
