#!/usr/bin/env python3

def return_evens(num_list):
    return [el for el in num_list if el % 2 == 0]


def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]
    return res