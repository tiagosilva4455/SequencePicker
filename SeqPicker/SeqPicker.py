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
     
    try:
         result_handle = NCBIWWW.qblast("blastn", "nt", seq) #BLAST
    except Exception:
             return "BLAST run failed."
        
    with open("blast_result.xml", "w+") as save_to:
        save_to.write(result_handle.read())
        result_handle.close() #SAVING RESULTS
            
    accessions_e_values=[]
               
    with open("blast_result.xml", "r") as result_handle:
        blast_record = NCBIXML.read(result_handle)
        for alignment in blast_record.alignments:
            for hsp in alignment.hsps:
                    accessions_e_values.append((alignment.accession,hsp.expect)) #OPENING RESULTS AND ACCESSION NUMBERS
                                    
    if accessions_e_values==[]:
        
        return "There are no BLAST results."
    
    else:
           
        Entrez.email = "tjls2001@gmail.com"
        
        values_sorted = sorted(accessions_e_values, key=lambda v: v[1])
        accessions = [v[0] for v in values_sorted]            
        e_value = [v[1] for v in values_sorted]    
    
    
        with Entrez.efetch(db="nucleotide", rettype="gb", retmode="text", id=accessions[0]) as handle:
            for record in SeqIO.parse(handle,"gb"):
                print()
                print("Definition: " + record.description)
                print("Accession Number: " + record.id)
                print("Start Site: " + record.seq[:15] + "...")
                print("Stop Site: " + "..." + record.seq[-15:])
                print()
                if accessions == "":
                    break #PRINTING START AND STOP SITES
                    
