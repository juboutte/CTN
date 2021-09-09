# -*- coding: us-ascii -*-

import sys

### Usage ###

#CTN.py - Parse a fasta files to standardise the name of species and use PickMe and PickMeQ software
#Example: Asclepiassolanoana256-15 ==> Asclepiassolanoana256

#Command line example: python CTN.py my_data.fasta

#By Julien Boutte, September 2021
#Copyright (c) 2021 Julien Boutte.
#Version 1.0.0

#This program is free software: you can redistribute it and/or modify it under
#the terms of the GNU General Public License as published by the Free Software
#Foundation, either version 3 of the License, or (at your option) any later
#version. A copy of this license is available at <http://www.gnu.org/licenses/>.
#Great effort has been taken to make this software perform its said
#task, however, this software comes with ABSOLUTELY NO WARRANTY,
#not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

#####

def parse_fasta(file):
    inputfile=open(file)
    list_name=[]
    list_seq=[]
    seq_temp=''
    for ligne in inputfile:
        if ligne[0]!='>':
            temp=ligne.split()
            if len(temp)>0:
                seq_temp=seq_temp+temp[0]
        else:
            list_name.append(ligne[1:].split()[0]) 
            if seq_temp!='': 
                list_seq.append(seq_temp)
                seq_temp=''
    list_seq.append(seq_temp)
    #checking
    #print list_name
    #print list_seq
    yield (list_name, list_seq)
    
#####

inputfile=open(sys.argv[1],'r')

temp=sys.argv[1].split(".")
extension_name='.'+temp[-1]

outputname=sys.argv[1].replace(extension_name, "_cleaned.fasta")
print 'output name file:', outputname

output=open(outputname,'w')

for name, seq in (parse_fasta(sys.argv[1])):
    list_name=name
    list_seq=seq

for name, seq in zip(list_name, list_seq):
    temp=name.split('-')
    if len(temp)==2:
        new_name=temp[0]
    elif len(temp)==3:
        new_name=temp[0]+'-'+temp[1]
    else:
        print 'ici'
        print name
        exit()
    output.write('>'+new_name+'\n'+seq+'\n')

inputfile.close()
output.close()

