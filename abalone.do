#!/bin/bash
#SBATCH --job-name=calc-mdft
##SBATCH --mail-type=ALL
##SBATCH --mail-user=my-email-address-at-ENS
#SBATCH --time=24:00:00
#SBATCH --ntasks=1

# PLEASE DO NOT TOUCH THE FOLLOWING LINE
source /etc/slurm-llnl/slurm-setup.sh

module purge

# MPI-only version
#EXE=cp2k.popt

# This line is mandatory
cd ${SLURM_RUN_DIR}
# Please comment out the following if you need the subdirectories from    
#     your submission directory
rsync -av --update ${SLURM_SUBMIT_DIR}/ .

#------------------------------------------------------------------------------

# Basis sets, potentials, vdW-information, ...

# Execute the code
#mpirun --bind-to none ${EXE} md.in > md.out

export OMP_NUM_THREADS = 1
./mdft-dev

# Store the exit status of the parallel job, whether it was successful or not
MYSTATUS=$?

# If the job was not successful, do not copy and erase the data; but you
#     HAVE TO come and control the data, and delete it so soon as possible!!
if [ ${MYSTATUS} -ne 0 ] ; then
  echo "Problem with \"${EXE}\", non-zero exit status: ${MYSTATUS}"
  exit ${MYSTATUS}
fi
