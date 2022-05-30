#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 30 01:54:10 2022

@author: taha
"""

from noise import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_file', '-i', help="Path to the input text file", type=str)
parser.add_argument('--output_file', '-o', help="Path to output file", type=str)
parser.add_argument('--delete_random_words', '-d', help="Probability of deleting a word",\
                    type=float, default=0.1)
parser.add_argument('--insert_random_words', '-i', help="Probability of inserting a random word",\
                    type=float, default=0.1)   
parser.add_argument('--replace_random_words', '-r',\
                    help="Probability of replacing a word with another random word",\
                    type=float, default=0.1)
parser.add_argument('--random_permutation', '-p', help="Permuting words at the end",\
                    type=bool, default=False) 
args = parser.parse_args()

input_file = args.input_file
output_file = args.output_file
delete_random_words = args.delete_random_words
insert_random_words = args.insert_random_words
replace_random_words = args.replace_random_words
random_permutation = args.random_permutation
