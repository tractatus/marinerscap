# :boat: :anchor: marinerscap :anchor: :boat:

Setup python environment and install bowtie2.

```
cd OligoMiner
conda env create -f environment.yml
conda activate probeMining
cd ..
conda install bowtie2
```

Then download a human genome index:

```
echo "$(tput setaf 2) DOWNLOADING HUMAN GENOME INDEX (4Gb)." 
echo "$(tput sgr 0) This will take some time." 
curl https://genome-idx.s3.amazonaws.com/bt/GRCh37.zip --output GRCh37.zip
unzip GRCh37.zip
```

Then run the design tool.
```
cd OligoMiner
sh designprobes.sh
```
