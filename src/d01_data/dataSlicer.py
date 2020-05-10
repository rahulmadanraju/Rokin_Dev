
import pandas as pd
import sys, os


def data_slicer(path_in,path_out,size):
    '''
    function to slice the whole data set to small chunk

    input :  string: path of input file, with file extention
          :  string: path of output file, with file extention
          :  size of slice you want
    '''

    print('---> data slicer in action <---')
    article_complete = pd.read_json(path_in)
    article_small = article_complete.head(size)   # make this a parameter
    article_small.to_csv('path_out')
    

