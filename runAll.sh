
$DIRECTORY = "mdft-dev/"
if [ ! -d "$DIRECTORY" ]; then
  # Control will enter here if $DIRECTORY doesn't exist.
    git clone https://github.com/maxlevesque/mdft-dev
    cd mdft-dev
    mkdir build
    cd build
    cmake ..
    make -j
    cd ../../
fi

for folder in *; do
	if [[ -d $folder ]]; then
	    cd $folder;
	    sbatch do;
	    cd ..;
    fi
done
