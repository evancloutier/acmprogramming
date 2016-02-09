import copy

tray = [
    [None, None, None],
    [None, None, None]
    
]

combo_set = set()

block_possibilities = ['1', '2t', '2b', '2l', '2r']

all_possibilities = []

def get_coords(count):
    x = count % 3
    y = count // 3
    return [x,y]

def generate_block(count, tray, block_possibilities, all_possibilities):
    tray_copy = copy.deepcopy(tray)
    x,y = get_coords(count)
    
    for symbol in block_possibilities:
        tray_copy[y][x] = symbol
        #another_tray_copy = copy.deepcopy(tray)
        if count != 5:
            generate_block(count + 1, tray_copy, block_possibilities, all_possibilities)
        all_possibilities.append(tray_copy)
        tray_copy = copy.deepcopy(tray)
        #another_tray_copy = copy.deepcopy(tray_copy)
        #print tray_copy
        
                
def is_illegal(arr):

    #print arr
    for y in range(2):
        for x in range(3):
            if arr[y][x] is None:
                return True

    for y in range(2):
        if arr[y][0] == '2r':
            return True
        if arr[y][2] == '2l':
            return True
        
    for x in range(3):
        if arr[1][x] == '2t':
            return True
        if arr[0][x] == '2b':
            return True
        if arr[1][x] == '2b' and arr[0][x] != '2t':
            return True

        if arr[0][x] == '2t' and arr[1][x] != '2b':
            return True

    for x in range(2):
        for y in range(2):
            if arr[y][x] == '2l' and arr[y][x+1] != '2r':
                return True

    for x in range(1,3):
        for y in range(2):
            if arr[y][x] == '2r' and arr[y][x-1] != '2l':
                return True

    return False 

def conv_to_tup(lst):
    lst = [item for sublist in lst for item in sublist]
    tup = tuple(lst)
    #print tup
    return tup


def gen_set(all_possibilities):
    all_sets = set()

    for poss in all_possibilities:
        #print poss
        tup = conv_to_tup(poss)
        all_sets.add(tup)

    return all_sets


def remove_illegals(all_possibilities):
    new_list = []
    for idx, arrangement in enumerate(all_possibilities):
        #print arrangement
        if is_illegal(arrangement) is False:
            #print arrangement
            new_list.append(arrangement)

    return new_list
'''
t = [
    ['1', '2t','1'],
    ['1', '1', '1']
]


if is_illegal(t) is False:
    print "False"
'''

'''
x = conv_to_tup([[1,2],[3,4]])
s = set()
s.add(x)
x = conv_to_tup([[1,2],[3,5]])
s.add(x)

print s
'''

generate_block(0, tray, block_possibilities, all_possibilities)

res = remove_illegals(all_possibilities)

res_sets = gen_set(res)

for p in res_sets:
    print p

print len(res_sets)

#res = remove_illegals(all_possibilities)
#print res
#x = gen_set(all_possibilities)

#for line in all_possibilities:
#    print line
