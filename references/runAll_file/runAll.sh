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
	if [ -d $folder -a $folder != "mdft-dev" -a $folder != "mdft_parser" -a $folder != "mdft_writer" -a $folder != "references" ]; then
	    cp mdft-dev/build/mdft-dev $folder
	    cp -r mdft-dev/build/data $folder
	    cd $folder
	    bash pc.do
	    cd ..
    fi
done
