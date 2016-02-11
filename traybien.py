import copy

class TrayBien:
    def __init__(self, depth, width, *args):
        self.depth = depth
        self.width = width
        self.max_block_num = depth * width - 1
        self.num_unique_valid_arrangements = 0
        self.tray = [[None for w in range(width)] for d in range(depth)]
        self.block_possibilities = ['1', '2t', '2b', '2l', '2r']
        self.all_arrangements = []
        self.all_arrangements_set = set()


    def get_coords(self, count):
        x = count % self.width
        y = count // self.width
        return x,y

    def generate_block(self, tray, block_num):
        tray_copy = copy.deepcopy(tray)
        x,y = self.get_coords(block_num)

        for symbol in self.block_possibilities:
            tray_copy[y][x] = symbol
            if block_num != self.max_block_num:
                self.generate_block(tray_copy, block_num + 1)
            self.all_arrangements.append(tray_copy)
            tray_copy = copy.deepcopy(tray)

    def is_legal(self, tray):
        for y in range(self.depth):
            for x in range(self.width):
                if tray[y][x] is None:
                    return False

        for y in range(self.depth):
            if tray[y][0] == '2r':
                return False
            if tray[y][self.width - 1] == '2l':
                return False

        for x in range(self.width):
            if tray[self.depth - 1][x] == '2t':
                return False
            if tray[0][x] == '2b':
                return False
            for y in range(self.depth - 1):
                if tray[y + 1][x] == '2b' and tray[y][x] != '2t':
                    return False
                if tray[y][x] == '2t' and tray[y + 1][x] != '2b':
                    return False

        for x in range(self.width - 1):
            for y in range(self.depth):
                if tray[y][x] == '2l' and tray[y][x + 1] != '2r':
                    return False
                if tray[y][x + 1] == '2r' and tray[y][x] != '2l':
                    return False
        return True

    def conv_to_tup(self, lst):
        lst = [item for sublist in lst for item in sublist]
        tup = tuple(lst)
        return tup

    def gen_set(self):
        for tray in self.all_arrangements:
            temp_tray = self.conv_to_tup(tray)
            self.all_arrangements_set.add(temp_tray)
        self.num_unique_valid_arrangements = len(self.all_arrangements_set)


    def remove_illegal_trays(self):
        temp_all_arrangements = []
        for arrangement in self.all_arrangements:
            if self.is_legal(arrangement) is True:
                temp_all_arrangements.append(arrangement)
        self.all_arrangements = temp_all_arrangements


new_tray = TrayBien(2,5)

new_tray.generate_block(new_tray.tray, 0)

new_tray.remove_illegal_trays()
new_tray.gen_set()



for i in range(len(new_tray.all_arrangements_set)):
    print new_tray.all_arrangements_set.pop()

print new_tray.num_unique_valid_arrangements