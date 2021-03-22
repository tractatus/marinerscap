# :boat: :anchor: marinerscap :anchor: :boat:

1. Make sure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed. 

2. Clone this repo, then create and activate the provided [environment](./environment.yml):

```
git clone https://github.com/tractatus/marinerscap.git
cd marinerscap
```

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
