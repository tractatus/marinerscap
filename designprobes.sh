for i in `find ../cDNA/ -name "*.fasta" -type f`; do
    echo "$(tput setaf 1) Finding candidates for " $i $(tput sgr 0)
    filename=$(basename -- "$i")
    extension="${filename##*.}"
    filename="${filename%.*}"
    python blockParse.py -f ../cDNA/${i} -l 40 -o "../output/${filename}"
done


for i in `find ../output/ -name "*.fastq" -type f`; do
    echo "$(tput setaf 2) Aligning against genome " $i $(tput sgr 0)
    filename=$(basename -- "$i")
    extension="${filename##*.}"
    filename="${filename%.*}"
    bowtie2 -x ../GRCh37/GRCh37 -U ../output/${i} --no-hd -t -k 100 --very-sensitive-local -S "../output/${filename}.sam"
    python outputClean.py -u -f "../output/${filename}.sam" -o "../output/${filename}"
done

num=0
for i in `find ../output/ -name "*.bed" -type f`; do
    echo "$(tput setaf 3) Printing IDT purchase order " $i $(tput sgr 0)
    filename=$(basename -- "$i")
    extension="${filename##*.}"
    filename="${filename%.*}"
    python printIDT.py "../output/${filename}.bed" "${num}" > "../probe_order/${filename}.tsv"
    num=$(( $num + 1 ))
    cat "../probe_order/${filename}.tsv"
done



