import sys
import os.path
import numpy as np
import csv
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq


def main():
    """Prints output for IDT order."""
    print ("This is the name of the script: ", sys.argv[0])
    print ("Number of arguments: ", len(sys.argv))
    print ("The arguments are: " , str(sys.argv))

    filename = sys.argv[1] #"../output/VIM_cDNA.bed"
    barcodeN = int(sys.argv[2])
    with open(filename) as csvfile:
        data = list(csv.reader(csvfile, delimiter='\t'))

    primer = 'CGGTGCATACACTA' # M13 rev CAGGAAACAGCTATGAC
    barcode2 = ''
    UDP0003 = 'ATATGAGACG'
    UDP0007 = 'AGAGCACTAG'
    UDP0011 = 'GAACATACGG'
    UDP0013 = 'TAATGGCAAG'

    barcode = [UDP0003, UDP0007, UDP0011, UDP0013][barcodeN];


    splitat = 20
    tmDiff = np.array
    for x in range(len(data)):
        l, r = Seq(data[x][3][:(splitat-1)]), Seq(data[x][3][(splitat+1):])
        tmp = abs( mt.Tm_Wallace(l) -  mt.Tm_Wallace(r) )
        tmDiff = np.append(tmDiff, tmp)

    idx = np.argpartition(tmDiff, 4)
    for i in (idx[:4]-1):
        l, r = data[i][3][:(splitat-1)], data[i][3][(splitat+1):]
        print(os.path.splitext(os.path.basename(filename))[0]  + "_B_" + barcode + "_" + 'Primer'+ str(i) + "\t" + l + 'AATGTTATCTT' + '\t100nm\tSTD')
        print(os.path.splitext(os.path.basename(filename))[0] + "_B_" + barcode + "_" + 'Padlock'+ str(i) + "\t" + '/5Phos/ACATTA' + r + barcode + primer + barcode2 + 'AAGATA' + '\t100nm\tSTD')

if __name__ == '__main__':
    main()
