# :boat: :anchor: marinerscap :anchor: :boat:
[![Build Status](https://travis-ci.com/tractatus/marinerscap.svg?token=XzUeqSSuF44YQrbkvFT5&branch=main)](https://travis-ci.com/tractatus/marinerscap)

This is a simple shell script to design oligo probes for _in situ_ hybridization and purchasing from [IDT](https://www.idtdna.com/site/order/oligoentry). All you need to do is to download the desired `cdna.fasta` file from Ensemble. For example [this is the API call](https://useast.ensembl.org/Homo_sapiens/Export/Output/Gene?db=core;flank3_display=0;flank5_display=0;g=ENSG00000139618;output=fasta;strand=feature;param=cdna;_format=Text) to get `BRCA2` cDNA:

```
https://useast.ensembl.org/Homo_sapiens/Export/Output/Gene?db=core;
flank3_display=0;
flank5_display=0;
g=ENSG00000139618;
output=fasta;
strand=feature;
param=cdna;
_format=Text
```

Just place the `.cdna.fasta` file in the `cDNA` folder. And run the shell script from main directory with the genome of choice as input argument to the shell script (here I use GRCh37 with bwotie2 indexes stored in `./GRCh37/GRCh37/`):

```
conda activate probeMining
sh designprobes.sh GRCh37
```

## Installation.

1. Install [GitHub](https://desktop.github.com/)  if you dont have it. 

2. Make sure you have [conda](https://docs.conda.io/en/latest/miniconda.html) installed. 

3. Clone this repo, then create and activate the provided [environment](./environment.yml):

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
sh designprobes.sh
```
