# -*- coding: utf-8 -*-
"""
Created on Tue May  3 21:56:17 2022

@author: Tiago Silva
"""

import Bio
import Bio.Blast

#Input for the sequence
from Bio.Seq import Seq

my_seq= Seq("sequence")

#Searching Database for sequence
from Bio.Blast import NCIBWWW
result_handle = NCIBWWW.qblast( "blastn", "nt", Seq("sequence", generic_dna))


