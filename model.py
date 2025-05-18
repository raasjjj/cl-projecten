# -*- coding: utf-8 -*-
"""
Created on Sun May 18 13:33:22 2025

@author: thijs
"""

from corpusreader import CorpusReader
import re


class NgramModel:
    """
    tokes a tokenized list of lists of strings and removes punct
    """
    
    def __init__(self, corrpus_tokens,n=2):
        self.model = 
        self.n = n
        cleaned_tokens = []
        
        #gets rid of the .,?!() and ads a start and end string in the sentences and puts all of it in one list.
        for token in corpus_tokens:
            cleaned_tokens.extend("<s>" * self.n)
            cleaned_tokens.extend(s.lower() for s in token if not re.search(r"[?.,!()]", s))
            cleaned_tokens.extend("</s>" * self.n)
                    
                