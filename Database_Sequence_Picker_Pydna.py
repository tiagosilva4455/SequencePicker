# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:56:17 2022

@author: Tiago Silva
"""

from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

seq = "ctgacgctca"

# def genbankref(seq):
    
#Blast

result_handle = NCBIWWW.qblast("blastn", "nt", seq)

blast_records = NCBIXML.parse(result_handle)

print(result_handle)
    
#Saving results

#with open("blast_results.xml", "w+") as save_to:
    #save_to.write(result_handle.read())
    #result_handle.close()
    
#Opening results

#result_handle=open("blast_results.xml","r")
#blast_record=NCBIXML.read(result_handle)
#print(blast_record)




