from consts import *
from copy import deepcopy

def ppi(p):
    for x in p: print(x)

def ppis(pieces):
    for p in pieces: ppi(p);print('-')

def pptable(table):
    for line in table: print(''.join(line))

def parse(pieces):
    pieces = [x.split('\n') for x in pieces.split('-')]
    pieces = [[x.replace('x',str(i)) for x in p if x.strip() != ''] for i, p in enumerate(pieces)]
    return pieces

def empty(w, h):
    return [['_' for _ in range(w)] for _ in range(h)]

def put(piece, table, dx, dy):
    ntable = None
    for y, line in enumerate(piece):
        for x, v in enumerate(line):
            if v != ' ':
                nx, ny = x+dx, y+dy
                assert bound_checks(nx, ny, table)
                assert table[ny][nx] == '_'
                if ntable == None:
                    ntable = deepcopy(table)
                ntable[ny][nx] = v
    return ntable

def bound_checks(x, y, table):
    return 0 <= y < len(table) and 0 <= x < len(table[0])

def print_calls(f):
    def wrap(*args,**kwargs):
        print('call:',f.__name__,args,kwargs)
        result = f(*args,**kwargs)
        print('result:',result)
        return result
    return wrap

def piece_size(p):
    return len(''.join([''.join(x) for x in p]).replace(' ',''))

def sort_by_size(pieces):
    return list(reversed(sorted(pieces, key=piece_size)))

def island_size(table, x, y):
    if not bound_checks(x, y, table) or table[y][x] != '_':
        return 0
    table[y][x] = 'E'
    s = 1
    for dx, dy in (1, 0),(0, 1), (-1 , 0), (0, -1):
        s += island_size(table, x+dx, y+dy)
    return s

def islands_sizes(table):
    table = deepcopy(table)
    for y, line in enumerate(table):
        for x, v in enumerate(line):
            if v == '_':
                yield island_size(table, x, y)

def impossible_cells(table, pieces):
    min_p_size = min([piece_size(p) for p in pieces])
    for size in islands_sizes(table):
        if size < min_p_size:
            return True
    return False

def solve(pieces, table):
    if len(pieces) == 0:
        return table
    if len(pieces) == 5:
        islands_sizes(table)
    if impossible_cells(table, pieces):
        return
    W, H = len(table[0]), len(table)
    piece = pieces[0]
    for dx in range(W):
        for dy in range(H):
            try:
                ntable = put(piece, table, dx, dy)
                res = solve(pieces[1:], ntable)
                if res is not None:
                    return res
            except AssertionError:
                pass

if __name__ == '__main__':
    sol = solve(sort_by_size(parse(PIECES)), empty(W,H))
    print('SOOOLUUUTIOOOON\n===')
    if sol == None:
        print('NOT SOLUTION FOUND :(')
    else:
        pptable(sol)