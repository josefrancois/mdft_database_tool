# mdft_database_tool
This project is only compatible with Linux. It has been written in [Python](https://www.python.org/) 2.7 which is required to use the project. \
It can be easily installed on Linux, if not, by using apt : `sudo apt install python2.7`

## Background
## Required Python Libraries
Some libraries are required and can be easily installed via [pip](https://pip.pypa.io/en/stable/installing/) :
- [numpy](http://www.numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [pandas](http://pandas.pydata.org/)
- [seaborn](https://seaborn.pydata.org/)

One command to install all the needed libraries : `sudo pip install numpy matplotlib pandas seaborn`

## Installation procedure
To install the project directly from GitHub :\
`git clone https://github.com/josefrancois/mdft_database_tool`

## What the user needs to do ?
1. To provide a database of molecules : only GROMACS and JSON format are compatible
2. To provide reference values of solvation free energy for each molecule of the database, in JSON format (not mandatory but recommended)
3. Edit database_definition.json (see the next section)

## Editing database_definition.json
This parameter file is written in [JSON](https://fr.wikipedia.org/wiki/JavaScript_Object_Notation). 
In the file, one database is described by a dictionnary containing several keys to describe it. Some are mandatory, some are optional. The user can choose any key to indicate its database, for instance `"freesolv"` in the example below.\
Then, the available keys to describe the database are listed as followed :
- **"mol_db"** (mandatory) : Database of molecules\
  If the format is JSON, indicate the JSON file.\
  If it is GROMACS, indicate the name of the directory containing all the .gro and .top files.
- **"format"** (mandatory) : Format of the database ('gromacs' or 'json')
- **"github"** (optional) : GitHub URL of the input database
If the database is stored on GitHub and is an archive, indicate the name of the archive
- **"commit"** (optional) : Commit of the input database if 'github' is indicated
- **"ref_values"** (optional but recommended) : File containing the reference values of solvation free energy for every molecules of the database
  Must be provided in JSON.
- **"mdft_output"** (optional but recommended) : Name of the output JSON file from MDFT calculations
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
For AUE plots, a categorical field from the input database must be indicated througfh a further **"cat_column"** key.
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
            "expt" : {
                "label" : "Experimental"
            }
        },
        "plots" : {
            "plotsvs" : {
                "vs Experimental" : {
                    "x" : "expt",
                    "y" : ["calc","mdft_energy_pc", "mdft_energy_pc+"]
                }
            },
            "plotserrdistrib" : {
                "vs Experimental" : {
                    "x" : "expt",
                    "y" : ["calc","mdft_energy_pc", "mdft_energy_pc+"],
                    "filename" : "error_distribution_exp"
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
## Four steps - Four commands
After providing the input database and editing `database_definition.json`, the user needs to go through four simple steps via four commands to get what he wants.
1) Process : transforming the molecules of the database into files compatible with MDFT code\
Command : `python mdft_db_process.py -db database`
2) Running : running MDFT code on every molecules\
Command : `bash runAll.sh`
3) Parsing : getting the results from MDFT calculations\
Command : `python mdft_parse.py -db database`
4) Analysis : generating the plots and analyzing the results\
Command : `python mdft_db_analysis.py -db database`

Enjoy !
