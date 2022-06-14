# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:56:17 2022

@author: Tiago Silva
"""

def genbankref(seq):
    
    def validSequence(seq):
        valid = "actg ACTG"
        for letter in seq:
            if letter not in valid:
                return False
        return True
    
    if validSequence(seq) == False:
        return "Please enter a valid nucleotide sequence"
    
    else:
    
     from Bio.Blast import NCBIWWW
     from Bio.Blast import NCBIXML 
     from Bio import Entrez
     from Bio import SeqIO
     
     result_handle = NCBIWWW.qblast("blastn", "nt", seq) #BLAST
   
         
    with open("blast_result.xml", "w+") as save_to:
        save_to.write(result_handle.read())
        result_handle.close() #SAVING RESULTS
                
    E_VALUE_THRESH = 0.00000000001
            
    accessions=[]
                
    e_value=[]
               
    with open("blast_result.xml", "r") as result_handle:
        blast_record = NCBIXML.read(result_handle)
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                if hsp.expect < E_VALUE_THRESH:
                    accessions.append(alignment.accession)
                    e_value.append(hsp.expect) #OPENING RESULTS AND ACCESSION NUMBERS
                                    
    
           
    Entrez.email = "tjls2001@gmail.com"
        
    with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=accessions[0]) as handle:
        for record in SeqIO.parse(handle,"gb"):
            print("Definition: " + record.description)
            print("Accession Number: " + record.id)
            print("Start Site: " + record.seq[:15] + "...")
            print("Stop Site: " + "..." + record.seq[-15:])
            print()
            print(accessions)
            print()
            print(e_value)
            if accessions == "":
                break #PRINTING START AND STOP SITES
                    
