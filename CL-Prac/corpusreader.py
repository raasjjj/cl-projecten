# -*- coding: utf-8 -*-
"""
Created on Sun May 18 13:33:22 2025

@author: thijs
"""
import nltk
import os

class CorpusReader:
    """Read the contents of a directory of files, and return the results as
    either a list of lines or a list of words.

    The pathname of the directory to read should be passed when
    creating the class:

    >>> reader = CorpusReader(r"path/to/dir")
    """

    def __init__(self, directory):
        """Checks if the given directory is a directory 
        if its not it gives an error, if its a real directory it makes self.path"""
        if os.path.isdir(directory) == True:
            self.path = directory
        else:
            raise ValueError("The given directory is not a valid directory.")    

    
    def _get_all_text(self):
        "Returns all text from a folder in a single string"
        text= ""
        folder = self.path
        for filename in os.listdir(folder):
            if filename.endswith(".txt"):
                with open(folder + "/" + filename,'r') as conn:
                    text += conn.read() +"\n"
        return text
    
    def sents(self): 
        "returns a list of lists of tokenized strings from the text in the directory"
        text = self._get_all_text()
        return [nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text)]
    