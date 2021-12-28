chessBoard = {'bking': 1, 'bqueen': 1, 'bbishop': 2, 'btowers': 2, 'bhorses': 2, 'bpawns': 8, 
'wking': 1, 'wqueen': 1, 'wbishop': 2, 'wtowers': 2, 'whorses': 2, 'wpawns': 8}

whites = 0
blacks = 0

def validChessBoard(chessBoard):
    count = {}
    for v in chessBoard.values():
        count.setdefault(v, 0)
        count[v] += count[v] + 1

    for x in ['bking', 'wking']:
        if count[x] != 1:
            return False
    
    for x in ['bpawns', 'wpawns']:
        if count[x] > 8:
            return False
        
    for x in count.keys():
        if x[0] == 'b':
            blacks += 1
        elif x[0] == 'w':
            whites += 1
        else:
            return False

    if blacks >16 or whites > 16:
        return False




    

