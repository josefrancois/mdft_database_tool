# MDFT Database Tool : an efficient wrapper around MDFT code
## Background
**Molecular Density Functional Theory (MDFT)** is a solvation model associated to a high-performing code, **MDFT code**, proposed by Daniel Borgis from La Maison De La Simulation and Maximilien Levesque from L'Ecole Normale Supérieure to compute fast and accurate solvation free energies.\
This work provides an easy-to-use and efficient computational tool enabling to run MDFT code on large databases and providing in-depth comparative analysis to evaluate the performance of MDFT on a large chemical space in a reliable and reproducible way.
## Requirements
This project has only been tested on Linux. It has been written in [Python](https://www.python.org/) 2.7 which is required to use the project. \
It can be easily installed on Linux, if not, by using apt : 
```bash
sudo apt install python2.7
```
After installing Python, some Python libraries are required :
- [numpy](http://www.numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [pandas](http://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)

They can be installed via :
- apt :
```bash
sudo apt install python-numpy python-matplotlib python-pandas python-seaborn
```
- [conda](https://conda.io/docs/download.html) :  
```bash
conda install numpy matplotlib pandas seaborn
```
- [pip](https://pip.pypa.io/en/stable/installing/)  : 
```bash
sudo pip install numpy matplotlib pandas seaborn
```  


## Installation procedure
To install the project directly from GitHub :\
`git clone https://github.com/josefrancois/mdft_database_tool`

## What does the user need to do ?
1. To provide a database of molecules, in GROMACS or JSON format
2. To provide reference values of solvation free energy for each molecule of the database, in JSON format (not mandatory but recommended)
3. Edit database_definition.json (see the next section)
4. Execute four simple commands

## Editing database_definition.json
This parameter file is written in [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). 
In the file, one database is described by a dictionnary containing several keys to describe it. Some are mandatory, some are optional. The user can choose any key to indicate its database, for instance `"freesolv"` in the example below.\
Then, the available keys to describe the database are listed as followed :
- **"mol_db"** (mandatory) : Database of molecules\
  If the format is JSON, indicate the JSON file.\
  If it is GROMACS, indicate the name of the directory containing all the .gro and .top files.
- **"format"** (mandatory) : Format of the database ('gromacs' or 'json')
- **"github"** (optional) : GitHub URL of the input database\
If the database is stored on GitHub and is an archive, indicate the name of the archive
- **"commit"** (optional) : Commit of the input database if 'github' is indicated
- **"ref_values"** (optional but recommended) : File containing the reference values of solvation free energies for each molecule of the database\
  Must be provided in JSON.
- **"mdft_output"** (optional but recommended) : Name of the output JSON file from MDFT results
- **"values_to_parse"** : Values block to indicate values that have to be parsed from the database of reference values and their associated label 
- **"plots"** : Plots block to accurately parametrize the plots

#### Values block :
Each indicated value should be present into the submitted database of reference values. Then to parse one value, indicate its corresponding field in the database as a key. For each value a label must be indicated by the **"label"** key (see the example below). This label will appear on the subsequent plots.

#### Plots block :
Three kinds of plots are available in the project, each of those can be activated by its corresponding key into the plots block :
- Correlation plots : **"plotsvs"**
- Error Distribution plots : **"plotserrdistrib"**
- Average Unsigned Errors : **"plotsby"**

All the plots are generated in *png* format.
For each plot, which can be indicated by any key, a value must be indicated for x and y axis.\
For x axis, only one value can be attributed to the x axis through the **"x"** key. For y axis, a list of values can be indicated to plot them against the x value through **"y"** key (see the example below)\
For Error Distribution plots, a further **"filename"** key much be specified to indicate the name of the png file. No need to put the .png extension.\
For AUE plots, a categorical field from the input database must be indicated througfh a further **"cat_column"** key.\
A final **"unit"** key must be indicated to specify the unit of the involved values. The unit will appear besides the labels in th plots.

Example with [FreeSolv](https://github.com/MobleyLab/FreeSolv) database built by David L. Mobley and al.:
```
{
    "freesolv" : {                          
        "mol_db" : "gromacs_solvated.tar.gz", 
        "format" : "gromacs",
        "github" : "https://github.com/MobleyLab/FreeSolv",
        "ref_values" : "database.json",
        "mdft_output": "mdft_results.json",
        "values_to_parse" : {
            "calc" : {
                "label" : "MD Simulations"
            },
            "expt" : {
                "label" : "Experimental"
            }
        },
        "plots" : {
            "plotsvs" : {
                "vs Experimental" : {
                    "x" : "expt",
                    "y" : ["calc","mdft_energy_pc", "mdft_energy_pc+"]
                },
                "vs MD Simulations" : {
                    "x" : "calc",
                    "y" : ["mdft_energy_pc", "mdft_energy_pc+"]
                }
            },
            "plotserrdistrib" : {
                "vs Experimental" : {
                    "x" : "expt",
                    "y" : ["calc","mdft_energy_pc", "mdft_energy_pc+"],
                    "filename" : "error_distribution_exp"
                },
                "vs MD Simulations" : {
                    "x" : "calc",
                    "y" : ["mdft_energy_pc", "mdft_energy_pc+"],
                    "filename" : "error_distribution_calc"
                }
            },
            "plotsby" : {
                "vs Experimental" : {
                    "x" : "expt",
                    "y" : ["calc","mdft_energy_pc"],
                    "cat_column" : "groups"
                }
            },
            "unit" : "kcal/mol"
        }
    }
}
```

A template of` database_definition.json` is available into the project. In this template, some keys are prepended by "\*\*". These keys can be moduled by the user as he wants. But the other ones must be written as it is.

## Four steps - Four commands
After providing the input database and editing `database_definition.json`, the user needs to execute four main scripts via four commands to get what he wants.
1) **Processing** : transforming the molecules of the database into files compatible with MDFT code\
Command : **`python mdft_db_process.py --database DATABASE`**\
The **database** option awaits the key that was chosen by the user to indicate its database in the parameter file `database_definition.json`.\
Other options are available to parametrize the MDFT calculations or the computer where they will be performed.\
The user can do the calculations on his localhost or on a remote server through the **server** option. All the available servers are showed in the file `serversParam.json` stored into the `references/parameters/` directory.\
The output of this step is a folder whose name will be the key indicating the database and containing one subfolder for each molecule and all the files necessary for the second and third steps.\
Here, only the database option is mandatory. 
2) **Running** : running MDFT code on every molecules\
Command : **`bash runAll.sh`**\
`runAll.sh` is generated on the fly from the first step. Beware : it has different forms according to the computer where the calculations are done. This step can not work if the form of this script and the wanted server are not in accordance.
3) **Parsing** : getting the results from MDFT calculations\
Command : **`python mdft_parse.py --database DATABASE`**\
If the key for the database is indicated and the file for the reference values is provided and indicated in `database_definition.json` (key : **"ref_values"**), the values from MDFT calculations will be merged with the values of the database into a single JSON file as the output of this step.\
The name of this file can be managed through the **"mdft_output"** key in `database_definition.json`.
4) **Analyzing** : generating the plots and analyzing the results\
Command : **`python mdft_db_analysis.py --database DATABASE`**\
Here, the database option is mandatory. This step creates a folder with all the needed plots (in png format) taking into account the parameters indicated in `database_definition.json`.

The help of the commands and all their possible options are available using the **`-h`** option.

## solutein_to_json.py
As a complement, `solutein_to_json.py` has been added into the project to enable formatting data from a solute.in file, which is the input format to describe a molecule for MDFT code, into JSON format. These data can be added to a database in JSON format.\
It also can be used on several solute.in files. To do so, the user just needs to put every solute.in files which has to be transformed into a folder and then use the indicated command at the end of `solutein_to_json.py` showed as a commentary.
