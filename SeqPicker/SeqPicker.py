# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:56:17 2022

@author: Tiago Silva
"""

def genbankref(seq):
    
     from Bio.Blast import NCBIWWW
     from Bio.Blast import NCBIXML 
     from Bio import Entrez
     from Bio import SeqIO
  
     result_handle = NCBIWWW.qblast("blastn", "nt", seq) #BLAST
    
     with open("blast_result.xml", "w+") as save_to:
        save_to.write(result_handle.read())
        result_handle.close() #SAVING RESULTS
        
        accessions=[]
        with open("blast_result.xml", "r") as result_handle:
            blast_record = NCBIXML.read(result_handle)
            for h in blast_record.alignments:
                accessions.append(h.accession) #OPENING RESULTS AND ACCESSION NUMBERS
        
        Entrez.email = "tjls2001@gmail.com"

        with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=accessions) as handle:
            for record in SeqIO.parse(handle,"gb"):
                print("Definition: " + record.description)
                print("Accession Number: " + record.id)
                print("Start Site: " + record.seq[:15] + "...")
                print("Stop Site:" + "..." + record.seq[-15:])
                print()
                if accessions == "":
                    break #PRINTING START AND STOP SITES
        

