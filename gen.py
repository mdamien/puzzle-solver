from hey import *
from good_pieces import *
from random import *
from random import randint as rd
import time

def total_size(pieces):
    return sum([piece_size(p) for p in pieces])

def gen(w, h):
    good_pieces = parse_pieces(GOOD_PIECES)
    pieces = []
    while True:
        pieces.append(choice(good_pieces))
        s = total_size(pieces)
        if s == w*h:
            sol = ssolve(pieces, w, h)
            if sol != None:
                pptable(sol)
                return pieces
            else:
                print('no sol')
        if s >= w*h:
            print('back to sq. one', s)
            pieces = []

gen(5,5)