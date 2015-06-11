####
## Author: Shelby Matlock
## Takes in a list of PDB IDs and removes redundant IDs,
## replacing them with their chains provided those are also
## non-redundant.
####

## IDs is the list of protein IDs downloaded from the PDB
## NR is Dunbrack's pdbaanr file (non-redundant protein chain file)
## pdbaanr can be found here: http://dunbrack.fccc.edu/Guoli/pisces_download.php
## OUT is the desired location for the outfile

## Open the files

import sys
IDs = sys.argv[1]
NR = sys.argv[2]
OUT = sys.argv[3]

with open(IDs, 'r+') as id_reference:
        read_ref = id_reference.read()
ids = read_ref.splitlines()

with open(NR, 'r+') as nr_reference:
        read_nr = nr_reference.read()
lines = read_nr.splitlines()

output  = open(OUT, 'w')

## Create a list of the ids from IDs and a 
## list of ids from NR. We will use NR_list to
## eliminate redundant ids from id_list

id_list = []
for item in ids:
        id_list.append(item)

nr_ids = []
for line in lines:
        if line.startswith(">"):
                nr_ids.append(line[1:5])

for item in id_list:
        if item not in nr_ids:
                id_list.remove(item)

## create a list of headers from NR and a 
## list of the associated peptide sequences
## from NR

cluster_list = []
headers = []
ctr = 0
while ctr < len(lines)-1:
        if lines[ctr].startswith(">"):
                header = lines[ctr]
                cluster = []
                headers.append(header)
                ctr += 1
                while ctr < len(lines)-1 and not lines[ctr].startswith(">"):
                        cluster.append(lines[ctr])
                        ctr += 1
                cluster_list.append(cluster)

values = []
for i in cluster_list:
        value = ''.join(i)
        values.append(value)

## Create a dictionary. headers are keys  => peptides are values.

reference_dict = {}
ctr = 0
while ctr < len(headers):
        reference_dict.update({headers[ctr]:values[ctr]})
        ctr += 1

## if keys in id_list, then output the header and 
## the peptide sequence

for ref in reference_dict.keys():
        if ref[1:5] in id_list:
                output.write(str(ref) + "\n")
                output.write(str(reference_dict[ref]) + "\n")



