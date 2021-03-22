# marinerscap

Setup python environment and install bowtie2.

```
cd OligoMiner
conda env create -f environment.yml
conda activate mariner
cd ..
conda install bowtie2
```

Then download a human genome index:

```
echo "$(tput setaf 2) DOWNLOADING HUMAN GENOME INDEX (4Gb). This will take some time. " $i $(tput sgr 0)
curl https://genome-idx.s3.amazonaws.com/bt/GRCh37.zip --output GRCh37.zip
unzip GRCh37.zip
```

Then run the design tool.
```
cd OligoMiner
sh designprobes.sh
```
