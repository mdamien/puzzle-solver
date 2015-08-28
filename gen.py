from hey import *
from random import *
from random import randint as rd
import time

def explode(table, x, y, depth_left=4):
    if depth_left <= 0:
        return 0
    if not bound_checks(x, y, table) or table[y][x] != '_':
        return 0
    table[y][x] = str(depth_left)[-1]
    if rd(0,100) > 99:
        os.system('clear')
        pptable(table)
        time.sleep(0.4)
    s = 1
    dirs = [(1, 0),(0, 1), (-1 , 0), (0, -1)]
    shuffle(dirs)
    for dx, dy in dirs:
        depth_left -= rd(0,2)
        s += explode(table, x+dx, y+dy, depth_left-1)
    return s

import time, os
while True:
    W, H = 300, 100
    table = empty(W, H)
    for _ in range(10):
        explode(table,rd(0,W),rd(0,H),depth_left=rd(0,1000))