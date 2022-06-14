"""
Created on Fri Jun  3 16:33:49 2022

@author: Tiago Silva
"""

import pytest
from SeqPicker import genbankref

def test_noseq():
    assert genbankref("") == "BLAST run failed." #Working on it

def test_invalidNucleotideSequence():
    assert genbankref("agjdhgou8ieyoquh!?") == "Please enter a valid nucleotide sequence"
    
def test_seqSameNucleotide():
    assert genbankref("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "BLAST run failed." #WORKING ON IT
    
retcode = pytest.main()

