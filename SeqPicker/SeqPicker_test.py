"""
Created on Fri Jun  3 16:33:49 2022

@author: Tiago Silva
"""

import pytest
from SeqPicker import genbankref

def test_NoSequence():
    assert genbankref("") == "BLAST run failed."

def test_invalidNucleotideSequence():
    assert genbankref("agjdhgou8ieyoquh!?") == "Please enter a valid nucleotide sequence"
    
def test_SameNucleotideSequence():
    assert genbankref("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") == "There are no BLAST results."
        
retcode = pytest.main()
