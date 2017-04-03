if [ ! -d "mdft-dev" ]; then
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
	if [ -d $folder -a $folder != "mdft-dev" ]; then
	    cp mdft-dev/build/mdft-dev $folder
	    cp -r mdft-dev/build/data $folder
	    cd $folder;
	    sbatch do;
	    cd ..;
    fi
done
mv ../input_mdft ../output_mdft
tar -czvf ../output_mdft.tar.gz ../output_mdft
